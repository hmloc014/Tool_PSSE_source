# -*- coding: utf-8 -*-
"""Low-risk wxPython performance helpers used by the dashboard.

The module is intentionally compatible with Python 2.7 and wxPython 3.0.
It does not change PSS/E calculation or save behavior.
"""

from __future__ import print_function

import functools
import os
import time

import wx


SEARCH_DEBOUNCE_MS = 200
_GRID_BATCH_DEPTH = {}


class _DeferredEvent(object):
    """Minimal event used after the original wx event has gone out of scope."""

    def Skip(self):
        pass


def _resolve_attr(instance, path):
    value = instance
    for part in path.split('.'):
        value = getattr(value, part)
    return value


def _profile_enabled():
    return os.environ.get('PSSE_TOOL_PROFILE', '0').lower() in (
        '1', 'true', 'yes', 'on')


def _write_profile(label, elapsed_ms):
    if not _profile_enabled():
        return

    line = '[PERF] {0}: {1:.1f} ms'.format(label, elapsed_ms)
    log_path = os.environ.get('PSSE_TOOL_PROFILE_LOG', 'performance.log')
    try:
        with open(log_path, 'a') as log_file:
            log_file.write(line + os.linesep)
    except Exception:
        print(line)


def profiled(label):
    """Time a function when PSSE_TOOL_PROFILE=1 is enabled."""

    def decorate(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            if not _profile_enabled():
                return function(*args, **kwargs)

            started = time.time()
            try:
                return function(*args, **kwargs)
            finally:
                _write_profile(label, (time.time() - started) * 1000.0)
        return wrapper
    return decorate


class _GridBatch(object):
    def __init__(self, grids):
        self.grids = []
        self.started = []
        seen = set()
        for grid in grids:
            if grid is None or not hasattr(grid, 'GetNumberRows'):
                continue
            grid_id = id(grid)
            if grid_id not in seen:
                seen.add(grid_id)
                self.grids.append(grid)

    def __enter__(self):
        for grid in self.grids:
            grid_id = id(grid)
            depth = _GRID_BATCH_DEPTH.get(grid_id, 0)
            _GRID_BATCH_DEPTH[grid_id] = depth + 1
            if depth != 0:
                continue

            began_batch = False
            froze = False
            try:
                grid.BeginBatch()
                began_batch = True
            except Exception:
                pass
            try:
                grid.Freeze()
                froze = True
            except Exception:
                pass
            self.started.append((grid, began_batch, froze))
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        for grid in reversed(self.grids):
            grid_id = id(grid)
            depth = _GRID_BATCH_DEPTH.get(grid_id, 1) - 1
            if depth > 0:
                _GRID_BATCH_DEPTH[grid_id] = depth
            else:
                _GRID_BATCH_DEPTH.pop(grid_id, None)

        for grid, began_batch, froze in reversed(self.started):
            if began_batch:
                try:
                    grid.EndBatch()
                except Exception:
                    pass
            if froze:
                try:
                    grid.Thaw()
                except Exception:
                    pass
        return False


def batched_grid_update(*grid_paths):
    """Freeze and batch the named grid attributes for one method call."""

    def decorate(function):
        @functools.wraps(function)
        def wrapper(instance, *args, **kwargs):
            grids = []
            for path in grid_paths:
                try:
                    grids.append(_resolve_attr(instance, path))
                except (AttributeError, TypeError):
                    continue
            with _GridBatch(grids):
                return function(instance, *args, **kwargs)
        return wrapper
    return decorate


def clear_grid(grid, column_count=None):
    """Clear a whole grid in one wx call, or a protected column subset."""

    rows = grid.GetNumberRows()
    columns = grid.GetNumberCols()
    if rows == 0 or columns == 0:
        return

    if column_count is None or column_count >= columns:
        try:
            grid.ClearGrid()
            return
        except Exception:
            pass

    columns_to_clear = min(columns, column_count or columns)
    for row in range(rows):
        for column in range(columns_to_clear):
            grid.SetCellValue(row, column, '')


def cancel_debounced(owner, key):
    calls = getattr(owner, '_psse_debounced_calls', None)
    if not calls:
        return
    call = calls.pop(key, None)
    if call is not None:
        try:
            call.Stop()
        except Exception:
            pass


def _call_if_alive(owner, callback):
    try:
        if hasattr(owner, 'IsBeingDeleted') and owner.IsBeingDeleted():
            return
    except Exception:
        return
    callback()


def debounce_call(owner, key, callback, delay_ms=SEARCH_DEBOUNCE_MS):
    """Restart a one-shot wx callback identified by owner and key."""

    calls = getattr(owner, '_psse_debounced_calls', None)
    if calls is None:
        calls = {}
        owner._psse_debounced_calls = calls

    cancel_debounced(owner, key)
    calls[key] = wx.CallLater(
        delay_ms, _call_if_alive, owner, callback)


def debounced_search(key, control_path, priority=None,
                     delay_ms=SEARCH_DEBOUNCE_MS):
    """Debounce a wx text handler while keeping programmatic refresh immediate."""

    def decorate(function):
        @functools.wraps(function)
        def wrapper(instance, event):
            if priority is not None:
                instance.priority = priority

            try:
                value = _resolve_attr(instance, control_path).GetValue()
            except Exception:
                value = ''

            immediate = (not value or getattr(instance, 'onUpdate', 0) == 1)
            if immediate:
                cancel_debounced(instance, key)
                return function(instance, event)

            def invoke():
                calls = getattr(instance, '_psse_debounced_calls', {})
                calls.pop(key, None)
                function(instance, _DeferredEvent())

            debounce_call(instance, key, invoke, delay_ms)
            if event is not None:
                event.Skip()
        return wrapper
    return decorate

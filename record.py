# -*- coding: utf-8 -*-
"""PSSE command recording support for the dashboard Record button.

The recorder uses PSSE's native Python recording format so operations made by
the tool are written as psspy commands to the selected automation file.
"""

import os
import re

import wx


try:
    text_type = unicode
except NameError:  # pragma: no cover - keeps the module importable on Python 3
    text_type = str


class RecorderError(Exception):
    """Raised when a PSSE recording session cannot be started or stopped."""


_ALWAYS_REMOVED_COMMANDS = (
    b'psspy.save(',
    b'psspy.case(',
    b'psspy.bsys(',
)

_SOLUTION_COMMANDS = (
    b'psspy.flat_2(',
    b'psspy.fdns(',
    b'psspy.fnsl(',
)

_PSSPY_CALL_RE = re.compile(
    br'^\s*(?:[A-Za-z_][A-Za-z0-9_]*\s*=\s*)?'
    br'psspy\.([A-Za-z0-9_]+)\s*\((.*)$'
)
_INTEGER_RE = re.compile(br'(?<![\w.])-?\d+(?![\w.])')
_STRING_RE = re.compile(
    br"(?:[rRuU]{0,2})?(?:\"\"\"([^\"]*)\"\"\"|'''([^']*)'''|"
    br"\"([^\"]*)\"|'([^']*)')"
)


def _contains_command(line, commands):
    """Return True when a recorded line contains one of ``commands``."""
    return any(command in line for command in commands)


def _last_solution_group(lines):
    """Return indexes for the final flat/fdns/fnsl solution command group."""
    last_flat_index = None
    for index, line in enumerate(lines):
        if b'psspy.flat_2(' in line:
            last_flat_index = index

    if last_flat_index is None:
        solution_indexes = [
            index for index, line in enumerate(lines)
            if _contains_command(line, _SOLUTION_COMMANDS)
        ]
        if not solution_indexes:
            return set()

        group_start = solution_indexes[-1]
        while (group_start > 0 and
               _contains_command(lines[group_start - 1], _SOLUTION_COMMANDS)):
            group_start -= 1
    else:
        group_start = last_flat_index

    kept_indexes = set()
    for index in range(group_start, len(lines)):
        line = lines[index]
        if _contains_command(line, _SOLUTION_COMMANDS):
            kept_indexes.add(index)
        elif b'psspy.' in line:
            break
    return kept_indexes


def _parse_psspy_call(line):
    """Return a recorded command name, integer arguments, and string arguments."""
    match = _PSSPY_CALL_RE.match(line)
    if match is None:
        return None

    arguments = match.group(2)
    integers = [int(value) for value in _INTEGER_RE.findall(arguments)]
    strings = []
    for string_match in _STRING_RE.finditer(arguments):
        for value in string_match.groups():
            if value is not None:
                strings.append(value)
                break
    return match.group(1), integers, strings


def _output_bytes(value):
    """Convert a PSSE label to safe UTF-8 bytes for a Python comment."""
    if isinstance(value, text_type):
        value = value.encode('utf-8')
    elif not isinstance(value, bytes):
        value = str(value)
    return value.replace(b'\r', b' ').replace(b'\n', b' ').strip()


def _bus_label(psspy_module, bus_number):
    """Return ``BUS NAME [number]`` using the active case when available."""
    number_text = str(bus_number).encode('ascii')
    bus_name = b''
    if psspy_module is not None and hasattr(psspy_module, 'notona'):
        try:
            result = psspy_module.notona(int(bus_number))
            if isinstance(result, tuple) and len(result) >= 2 and not result[0]:
                bus_name = _output_bytes(result[1]).replace(b'\x00', b'')
        except Exception:
            bus_name = b''

    if bus_name:
        return bus_name + b' [' + number_text + b']'
    return b'bus ' + number_text


def _bus_argument(integers, position, psspy_module):
    """Resolve a positional bus number or return a readable placeholder."""
    if len(integers) <= position:
        return b'unknown bus'
    return _bus_label(psspy_module, integers[position])


def _recorded_bus_label(integers, strings, psspy_module):
    """Prefer a bus name recorded directly by bus_data/bus_chng calls."""
    if integers and strings:
        recorded_name = _output_bytes(strings[0])
        if recorded_name:
            return (recorded_name + b' [' +
                    str(integers[0]).encode('ascii') + b']')
    return _bus_argument(integers, 0, psspy_module)


def _id_suffix(strings):
    """Return a short circuit/machine/load ID suffix when one was recorded."""
    if not strings:
        return b''
    identifier = _output_bytes(strings[0])
    if not identifier:
        return b''
    return b' (ID ' + identifier + b')'


def _step_note(line, psspy_module):
    """Build a concise human-readable note for a primary recorded PSSE call."""
    parsed = _parse_psspy_call(line)
    if parsed is None:
        return None

    command, integers, strings = parsed
    if command.startswith(b'seq_'):
        return None
    if command in (b'fdns', b'fnsl'):
        return None
    if command == b'flat_2':
        return b'# Solve power flow'

    if command.startswith(b'bus_data'):
        return b'# Add substation ' + _recorded_bus_label(
            integers, strings, psspy_module
        )
    if command.startswith(b'bus_chng'):
        return (b'# Adjust substation ' +
                _recorded_bus_label(integers, strings, psspy_module) +
                b' parameters')
    if command == b'bus_number':
        return (b'# Renumber substation ' +
                _bus_argument(integers, 0, psspy_module) + b' to ' +
                _bus_argument(integers, 1, psspy_module))
    if command == b'dscn':
        return b'# Disconnect substation ' + _bus_argument(integers, 0, psspy_module)
    if command == b'extr':
        return b'# Delete substation ' + _bus_argument(integers, 0, psspy_module)

    if command in (b'branch_data', b'branch_chng', b'purgbrn', b'movebrn'):
        if command == b'branch_data':
            action = b'Add'
        elif command == b'purgbrn':
            action = b'Delete'
        else:
            action = b'Adjust'
        return (b'# ' + action + b' line from ' +
                _bus_argument(integers, 0, psspy_module) + b' to ' +
                _bus_argument(integers, 1, psspy_module) +
                _id_suffix(strings))

    if command.startswith(b'machine_') or command == b'purgmac':
        if command.startswith(b'machine_data'):
            action = b'Add'
        elif command == b'purgmac':
            action = b'Delete'
        else:
            action = b'Adjust'
        return (b'# ' + action + b' generator at ' +
                _bus_argument(integers, 0, psspy_module) +
                _id_suffix(strings))
    if command.startswith(b'plant_'):
        action = b'Add' if command.startswith(b'plant_data') else b'Adjust'
        return (b'# ' + action + b' generator plant at ' +
                _bus_argument(integers, 0, psspy_module))

    if command.startswith(b'load_') or command == b'purgload':
        if command.startswith(b'load_data'):
            action = b'Add'
        elif command == b'purgload':
            action = b'Delete'
        else:
            action = b'Adjust'
        return (b'# ' + action + b' load at ' +
                _bus_argument(integers, 0, psspy_module) +
                _id_suffix(strings))

    if command.startswith(b'shunt_') or command == b'purgshunt':
        if command.startswith(b'shunt_data'):
            action = b'Add'
        elif command == b'purgshunt':
            action = b'Delete'
        else:
            action = b'Adjust'
        return (b'# ' + action + b' shunt at ' +
                _bus_argument(integers, 0, psspy_module) +
                _id_suffix(strings))

    if command.startswith(b'two_winding_'):
        action = b'Add' if b'_data' in command else b'Adjust'
        return (b'# ' + action + b' two-winding transformer from ' +
                _bus_argument(integers, 0, psspy_module) + b' to ' +
                _bus_argument(integers, 1, psspy_module) +
                _id_suffix(strings))

    if command.startswith(b'three_wnd_') or command == b'purg3wnd':
        if b'_data' in command and not command.startswith(b'three_wnd_winding'):
            action = b'Add'
        elif command == b'purg3wnd':
            action = b'Delete'
        else:
            action = b'Adjust'
        return (b'# ' + action + b' three-winding transformer ' +
                _bus_argument(integers, 0, psspy_module) + b' / ' +
                _bus_argument(integers, 1, psspy_module) + b' / ' +
                _bus_argument(integers, 2, psspy_module) +
                _id_suffix(strings))

    readable_command = command.replace(b'_', b' ')
    return b'# Run PSSE step: ' + readable_command


def _add_step_notes(lines, psspy_module):
    """Insert idempotent comments immediately before recorded primary calls."""
    line_ending = b'\r\n' if any(line.endswith(b'\r\n') for line in lines) else b'\n'
    annotated_lines = []
    for line in lines:
        note = _step_note(line, psspy_module)
        if note is not None:
            note_line = note + line_ending
            if not annotated_lines or annotated_lines[-1] != note_line:
                annotated_lines.append(note_line)
        annotated_lines.append(line)
    return annotated_lines


def clean_recorded_macro(output_path, psspy_module=None):
    """Remove dashboard-only PSSE noise from a completed recording.

    All save, case, and subsystem-selection commands are removed. Of the
    flat/fdns/fnsl solution sequences, only the final group is retained and
    duplicate fnsl calls in that group are collapsed to one. Other recorded
    commands are preserved and annotated with short human-readable step notes.
    """
    with open(output_path, 'rb') as recording_file:
        lines = recording_file.readlines()

    kept_solution_indexes = _last_solution_group(lines)
    cleaned_lines = []
    fnsl_kept = False
    for index, line in enumerate(lines):
        if _contains_command(line, _ALWAYS_REMOVED_COMMANDS):
            continue
        if (_contains_command(line, _SOLUTION_COMMANDS) and
                index not in kept_solution_indexes):
            continue
        if b'psspy.fnsl(' in line:
            if fnsl_kept:
                continue
            fnsl_kept = True
        cleaned_lines.append(line)

    removed_line_count = len(lines) - len(cleaned_lines)
    cleaned_lines = _add_step_notes(cleaned_lines, psspy_module)

    with open(output_path, 'wb') as recording_file:
        recording_file.writelines(cleaned_lines)

    return removed_line_count


def _normalise_automation_name(name):
    """Return a safe Python filename entered by the user."""
    if name is None:
        raise RecorderError("Please enter an automation file name.")

    name = text_type(name).strip()
    if not name:
        raise RecorderError("Please enter an automation file name.")

    invalid_characters = u'<>:"/\\|?*'
    if (name in (u'.', u'..') or
            name != os.path.basename(name) or
            any(character in name for character in invalid_characters) or
            name.endswith((u'.', u' '))):
        raise RecorderError(
            "Enter a file name only, without a folder or invalid Windows characters."
        )

    if not name.lower().endswith(u'.py'):
        name += u'.py'
    return name


def prompt_automation_path(parent, default_directory, default_name=u'auto1.py'):
    """Ask for an automation name and return its full path, or None on cancel."""
    if not default_directory or not os.path.isdir(default_directory):
        default_directory = os.getcwd()

    proposed_name = default_name
    while True:
        dialog = wx.TextEntryDialog(
            parent,
            u"Enter the automation file name (for example: auto1.py)",
            u"Start PSSE command recording",
            defaultValue=proposed_name,
        )
        result = dialog.ShowModal()
        entered_name = dialog.GetValue()
        dialog.Destroy()

        if result != wx.ID_OK:
            return None

        try:
            automation_name = _normalise_automation_name(entered_name)
        except RecorderError as error:
            wx.MessageBox(
                text_type(error),
                u"Invalid automation name",
                wx.OK | wx.ICON_WARNING,
                parent,
            )
            proposed_name = entered_name
            continue

        output_path = os.path.abspath(
            os.path.join(default_directory, automation_name)
        )
        if not os.path.exists(output_path):
            return output_path

        confirm = wx.MessageDialog(
            parent,
            u"The file already exists:\n%s\n\nOverwrite it?" % output_path,
            u"Confirm overwrite",
            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION,
        )
        overwrite = confirm.ShowModal() == wx.ID_YES
        confirm.Destroy()
        if overwrite:
            return output_path
        proposed_name = automation_name


class PsseCommandRecorder(object):
    """Small stateful wrapper around psspy.startrecording/stoprecording."""

    PYTHON_FORMAT = 1

    def __init__(self, psspy_module):
        self._psspy = psspy_module
        self._active = False
        self._output_path = None

    @property
    def is_recording(self):
        return self._active

    @property
    def output_path(self):
        return self._output_path

    def start(self, output_path):
        if self._active:
            raise RecorderError("A PSSE command recording is already active.")
        if not output_path:
            raise RecorderError("No automation file was selected.")

        output_path = os.path.abspath(output_path)
        output_directory = os.path.dirname(output_path)
        if not os.path.isdir(output_directory):
            raise RecorderError("The automation output folder does not exist.")

        ierr = self._psspy.startrecording(self.PYTHON_FORMAT, output_path)
        if ierr:
            raise RecorderError(
                "PSSE could not start recording (error code %s)." % ierr
            )

        self._active = True
        self._output_path = output_path
        return output_path

    def stop(self):
        if not self._active:
            return None

        output_path = self._output_path
        ierr = self._psspy.stoprecording()
        self._active = False
        self._output_path = None
        if ierr:
            raise RecorderError(
                "PSSE could not finish recording (error code %s)." % ierr
            )

        try:
            clean_recorded_macro(output_path, self._psspy)
        except (IOError, OSError) as error:
            raise RecorderError(
                "PSSE recording stopped, but the automation file could not "
                "be cleaned: %s" % error
            )
        return output_path

# -*- coding: utf-8 -*-
"""Resolve and apply one-element N-1 outages for the SAV-file generator."""
import re


def as_text(value):
    """Return a clean unicode string for PSS/E and ACC values."""
    if isinstance(value, (list, tuple)):
        value = ' '.join([as_text(item) for item in value])
    try:
        return unicode(value).strip()
    except NameError:
        return str(value).strip()


def _compact_id(value):
    return as_text(value).strip().strip('"').strip("'")


def _hyphen_parts(value):
    return [part.strip() for part in as_text(value).split('-') if part.strip()]


def _has_three_winding_words(value):
    text = as_text(value).upper()
    return ('3W' in text or '3-W' in text or 'THREE WIND' in text or
            '3 WIND' in text or '3WIND' in text)


def _branch_candidates(label, description):
    candidates = []
    for value in (label, description):
        parts = _hyphen_parts(value)
        if len(parts) == 3 and parts[0].isdigit() and parts[1].isdigit():
            candidates.append((int(parts[0]), int(parts[1]), _compact_id(parts[2])))

        matches = re.findall(r'(\d+)\s*-\s*(\d+)\s*-\s*([A-Za-z0-9_]+)',
                             as_text(value))
        for from_bus, to_bus, circuit_id in matches:
            candidates.append((int(from_bus), int(to_bus), _compact_id(circuit_id)))

    unique = []
    for candidate in candidates:
        if candidate not in unique:
            unique.append(candidate)
    return unique


def _three_winding_candidates(label, description):
    candidates = []
    for value in (label, description):
        parts = _hyphen_parts(value)
        if (len(parts) == 4 and parts[0].isdigit() and parts[1].isdigit() and
                parts[2].isdigit()):
            candidates.append((int(parts[0]), int(parts[1]), int(parts[2]),
                               _compact_id(parts[3])))

        if _has_three_winding_words(value):
            matches = re.findall(r'(\d+)\s*-\s*([A-Za-z0-9_]+)', as_text(value))
            for bus, circuit_id in matches:
                candidates.append((int(bus), None, None, _compact_id(circuit_id)))

    # ACC network labels for a 3-winding transformer are commonly BUS-ID,
    # without the text "3W".  Treat that form as a 3-winding candidate too.
    for value in (label, description):
        parts = _hyphen_parts(value)
        if len(parts) == 2 and parts[0].isdigit():
            candidates.append((int(parts[0]), None, None, _compact_id(parts[1])))

    unique = []
    for candidate in candidates:
        if candidate not in unique:
            unique.append(candidate)
    return unique


def three_winding_inventory(psspy):
    """Read all three-winding transformer identities in the loaded SAV case."""
    fields = ['WIND1NUMBER', 'WIND2NUMBER', 'WIND3NUMBER', 'STATUS']
    try:
        ierr, values = psspy.atr3int(-1, 1, 3, 2, 1, fields)
        if ierr:
            return []
        ierr, char_values = psspy.atr3char(-1, 1, 3, 2, 1, ['ID'])
        if ierr:
            return []
    except Exception:
        return []

    inventory = []
    try:
        count = len(values[0])
    except (IndexError, TypeError):
        return inventory

    for index in range(count):
        try:
            inventory.append({
                'from_bus': int(values[0][index]),
                'to_bus': int(values[1][index]),
                'third_bus': int(values[2][index]),
                'status': int(values[3][index]),
                'circuit_id': _compact_id(char_values[0][index]),
            })
        except (IndexError, TypeError, ValueError):
            pass
    return inventory


def _resolve_branch(psspy, candidates):
    for from_bus, to_bus, circuit_id in candidates:
        ierr, status = psspy.brnint(from_bus, to_bus, circuit_id, 'STATUS')
        if not ierr:
            return {
                'state': 'ready',
                'kind': 'line',
                'from_bus': from_bus,
                'to_bus': to_bus,
                'circuit_id': circuit_id,
                'display_name': '%s-%s-%s' % (from_bus, to_bus, circuit_id),
                'status': status,
            }
        ierr, status = psspy.brnint(to_bus, from_bus, circuit_id, 'STATUS')
        if not ierr:
            return {
                'state': 'ready',
                'kind': 'line',
                'from_bus': to_bus,
                'to_bus': from_bus,
                'circuit_id': circuit_id,
                'display_name': '%s-%s-%s' % (to_bus, from_bus, circuit_id),
                'status': status,
            }
    return None


def _resolve_three_winding(inventory, candidates):
    for from_bus, to_bus, third_bus, circuit_id in candidates:
        matches = []
        for item in inventory:
            same_id = item['circuit_id'].upper() == circuit_id.upper()
            if not same_id:
                continue
            if to_bus is None:
                if from_bus in (item['from_bus'], item['to_bus'], item['third_bus']):
                    matches.append(item)
            elif set((from_bus, to_bus, third_bus)) == set((item['from_bus'], item['to_bus'], item['third_bus'])):
                matches.append(item)
        if len(matches) == 1:
            item = matches[0]
            item = item.copy()
            item['state'] = 'ready'
            item['kind'] = 'three_winding_transformer'
            item['display_name'] = '%s-%s-%s-%s' % (
                item['from_bus'], item['to_bus'], item['third_bus'],
                item['circuit_id'])
            return item
        if len(matches) > 1:
            return {
                'state': 'unresolved',
                'reason': 'More than one 3-winding transformer matches %s.' % circuit_id,
            }
    return None


def resolve_contingency(psspy, label, description, inventory):
    """Resolve a single ACC contingency to an in-service SAV element."""
    label = as_text(label)
    description = as_text(description)
    branch_candidates = _branch_candidates(label, description)
    three_candidates = _three_winding_candidates(label, description)
    is_three_winding = (_has_three_winding_words(label) or
                        _has_three_winding_words(description) or
                        any(candidate[1] is not None for candidate in three_candidates))

    if is_three_winding:
        result = _resolve_three_winding(inventory, three_candidates)
        if result:
            return result
    else:
        result = _resolve_branch(psspy, branch_candidates)
        if result:
            return result
        # A short BUS-ID label is ambiguous until the original SAV is checked.
        result = _resolve_three_winding(inventory, three_candidates)
        if result:
            return result

    return {
        'state': 'unresolved',
        'reason': 'Could not map ACC contingency to one line or 3-winding transformer.',
    }


def apply_outage(psspy, element):
    """Switch off exactly the one resolved network element."""
    if element['kind'] == 'line':
        return psspy.branch_chng(element['from_bus'], element['to_bus'],
                                 element['circuit_id'], INTGAR1=0)
    return psspy.three_wnd_imped_chng_3(
        element['from_bus'], element['to_bus'], element['third_bus'],
        element['circuit_id'], INTGAR8=0)


def safe_filename(value):
    name = as_text(value)
    name = re.sub(r'[\\/:*?"<>|]+', '_', name)
    name = re.sub(r'\s+', ' ', name).strip().rstrip('.')
    return name or 'contingency'

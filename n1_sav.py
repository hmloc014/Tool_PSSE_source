# -*- coding: utf-8 -*-
"""Resolve and apply one-element N-1 outages for the SAV-file generator."""
import io
import os
import re
import tempfile


def as_text(value):
    """Return a clean unicode string for PSS/E and ACC values."""
    if isinstance(value, (list, tuple)):
        value = ' '.join([as_text(item) for item in value])
    try:
        return unicode(value).strip()
    except NameError:
        return str(value).strip()


def _normalized_acc_key(value):
    return ' '.join(as_text(value).split()).upper()


def _parse_available_capacity_rows(report_text):
    """Extract monitored-element and contingency columns in report row order."""
    rows = []
    contingency_start = None
    others_start = None
    header_found = False

    for line in report_text.splitlines():
        if ('CONTINGENCY LABEL' in line and 'OTHERS' in line and
                'AVAILABLE' in line):
            header_found = True
            contingency_start = line.index('<----- CONTINGENCY')
            others_start = line.index('OTHERS')
            continue
        if contingency_start is None:
            continue

        monitored_element = ' '.join(line[:contingency_start].split())
        contingency = ' '.join(line[contingency_start:others_start].split())
        numeric_tokens = line[others_start:].split()
        if monitored_element and contingency and len(numeric_tokens) == 7:
            rows.append((monitored_element, contingency))

    if not header_found:
        raise RuntimeError(
            'PSS/E report does not contain the available-capacity table header.')
    return rows


def _order_capacity_rows_by_sequence(rows, summary):
    """Order report rows by the ACC Flow Element Seq# column."""
    element_order = {}
    for index, element in enumerate(getattr(summary, 'melement', [])):
        element_order.setdefault(_normalized_acc_key(element), index)

    fallback_element = len(element_order) + len(rows)
    ordered_rows = []
    for original_index, row in enumerate(rows):
        monitored_element = row[0]
        ordered_rows.append((
            element_order.get(_normalized_acc_key(monitored_element),
                              fallback_element + original_index),
            original_index,
            row,
        ))
    # Python's stable sort plus original_index preserves report order when two
    # rows have the same Seq#.  No contingency-label sorting is applied.
    ordered_rows.sort(key=lambda item: (item[0], item[1]))
    return [item[2] for item in ordered_rows]


def available_capacity_contingencies(psspy, acc_path, summary=None):
    """Read the Flow Element/Available Capacity contingency column from ACC."""
    handle, report_path = tempfile.mkstemp(prefix='n1-capacity-', suffix='.txt')
    os.close(handle)
    default_integer = getattr(psspy, '_i', -999)
    default_float = getattr(psspy, '_f', -999.0)
    status = [2, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    intval = [0, 0, 0, 0, default_integer]
    realval = [0.5, 5.0, 100.0, 0.0, 0.0, 0.0, default_float]

    try:
        ierr = psspy.report_output(2, report_path, [1, 0])
        if ierr:
            raise RuntimeError(
                'PSS/E could not open its temporary ACC report (error %s).' % ierr)
        try:
            report_function = getattr(
                psspy, 'accc_single_run_report_3',
                getattr(psspy, 'accc_single_run_report_2', None))
            if report_function is None:
                raise RuntimeError(
                    'This PSS/E version has no supported ACC report API.')
            ierr = report_function(status, intval, realval, acc_path)
        finally:
            psspy.report_output(1, '', [0, 0])
        if ierr:
            raise RuntimeError(
                'PSS/E could not read the available-capacity report (error %s).'
                % ierr)

        with io.open(report_path, 'r', encoding='utf-8',
                     errors='ignore') as report_file:
            rows = _parse_available_capacity_rows(report_file.read())
        if summary is not None:
            rows = _order_capacity_rows_by_sequence(rows, summary)
        return [row[1] for row in rows]
    finally:
        try:
            os.remove(report_path)
        except OSError:
            pass


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

        # ACC network labels are normally written as SINGLE BUS1-BUS2(CKT).
        matches = re.findall(r'(\d+)\s*-\s*(\d+)\s*\(\s*([A-Za-z0-9_]+)\s*\)',
                             as_text(value))
        for from_bus, to_bus, circuit_id in matches:
            candidates.append((int(from_bus), int(to_bus), _compact_id(circuit_id)))

        # Full PSS/E contingency descriptions use words instead of hyphens:
        # OPEN LINE FROM BUS 176203 [...] TO BUS 176441 [...] CKT 1.
        matches = re.findall(
            r'FROM\s+BUS\s+(\d+).*?TO\s+BUS\s+(\d+).*?CKT\s+([A-Za-z0-9_]+)',
            as_text(value), re.IGNORECASE)
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

        # ACC network labels are normally written as SINGLE BUS1-BUS2-BUS3(CKT).
        matches = re.findall(
            r'(\d+)\s*-\s*(\d+)\s*-\s*(\d+)\s*\(\s*([A-Za-z0-9_]+)\s*\)',
            as_text(value))
        for from_bus, to_bus, third_bus, circuit_id in matches:
            candidates.append((int(from_bus), int(to_bus), int(third_bus),
                               _compact_id(circuit_id)))

        # Three-winding event descriptions contain three consecutive BUS
        # clauses followed by one circuit identifier.
        matches = re.findall(
            r'FROM\s+BUS\s+(\d+).*?TO\s+BUS\s+(\d+).*?TO\s+BUS\s+(\d+).*?CKT\s+([A-Za-z0-9_]+)',
            as_text(value), re.IGNORECASE)
        for from_bus, to_bus, third_bus, circuit_id in matches:
            candidates.append((int(from_bus), int(to_bus), int(third_bus),
                               _compact_id(circuit_id)))

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
            # Use PSS/E's inventory order for the API call, but retain the
            # ACC/network-label bus order in the generated filename.
            if to_bus is not None and third_bus is not None:
                display_buses = (from_bus, to_bus, third_bus)
            else:
                display_buses = (item['from_bus'], item['to_bus'],
                                 item['third_bus'])
            item['display_name'] = '%s-%s-%s-%s' % (
                display_buses[0], display_buses[1], display_buses[2],
                circuit_id)
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
    result = psspy.three_wnd_imped_chng_3(
        element['from_bus'], element['to_bus'], element['third_bus'],
        element['circuit_id'], INTGAR8=0)
    # PSS/E 33 returns (ierr, values) for this API, whereas branch_chng
    # returns only ierr.  Expose one consistent error code to the caller.
    if isinstance(result, tuple):
        return result[0]
    return result


def safe_filename(value):
    name = as_text(value)
    name = re.sub(r'[\\/:*?"<>|]+', '_', name)
    name = re.sub(r'\s+', ' ', name).strip().rstrip('.')
    return name or 'contingency'

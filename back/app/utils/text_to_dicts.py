import re

from ..utils.terms import decompose, find_functors, sort_functors, replace_functors
from ..utils.table import decomposed_term_to_table


def text_to_dicts(text):
    """
    LINE refers to the entered text, while ROW refers to the generated matrix.
    Each line contains ACT (call, fail...), COL (the number in brackets) and TERM (the complex term).

    It is assumed that the terms have a form like 'a', 'a(b, c)', 'a(b(c))', but not 'a( b, c )', '(a, b)' or 'a()'.
    One space after each comma is assumed. (No spaces in ALL terms would also be ok, but not in SOME.)

    The big matrix of terms is not to be confused with the small tables created below, each of which describes one term.
    """

    # remove any whitespace before and after the text
    text = re.sub('^\s+', '', text)
    text = re.sub('\s+$', '', text)

    # START `lines`
    raw_lines = text.split('\n')  # '\n' with Vue, would be '\r\n' with POST from HTML form
    lines = []
    acts = {'Call': 'c', 'Redo': 'r', 'Fail': 'f', 'Exit': 'e'}
    cols = set()  # For each line the parenthesised number between action and term will be added to this set.
    terms = set()
    for line in raw_lines:
        match = re.search('^\s*(\w*): \((\d+)\) (.+) \? creep$', line)
        act, col, term = acts[match.group(1)], int(match.group(2)), match.group(3)
        cols.add(col)
        terms.add(term)
        lines.append({'act': act, 'col': col, 'term': term})

    min_col = min(cols)
    max_col = max(cols)
    number_of_cols = max_col - min_col + 1
    terms = sorted(terms)

    for line in lines:
        line['col'] -= min_col  # enumerate columns from 0
        line['term'] = terms.index(line['term'])  # replace term string with index of `terms`

    opening_acts, closing_acts = ['c', 'r'], ['f', 'e']
    lines_to_be_deleted = []
    last_row, last_col, last_act, last_term = -1, 0, None, None
    for i, line in enumerate(lines):
        col, act, term = line['col'], line['act'], line['term']
        if col > last_col:
            row = last_row
        elif col == last_col and term == last_term and last_act in opening_acts and act in closing_acts:
            row = last_row
            line['act'] = last_act + act  # letter combination, e.g. 'cf' for call and fail
            lines_to_be_deleted.append(i-1)
        else:
            row = last_row + 1
        line['row'] = row
        last_row, last_col, last_act, last_term = row, col, line['act'], term
    number_of_rows = last_row + 1

    for i in lines_to_be_deleted[::-1]:
        lines.pop(i)
    # FINISH `lines`

    matrix = [[None for c in range(number_of_cols)] for r in range(number_of_rows)]
    for d in lines:
        r, c = d['row'], d['col']
        a, t = d['act'], d['term']
        matrix[r][c] = {'act': a, 'term': t}

    raw_deco_terms = []
    for term in terms:
        deco = decompose(term)
        raw_deco_terms.append(deco)

    raw_functors = set()
    for d in raw_deco_terms:
        raw_functors = raw_functors.union(find_functors(d))  # each functor found in `d` added as pair of its name and arity
    functors = sort_functors(raw_functors)

    # Each dict in `raw_deco_terms` contains the functor names directly as `functor`.
    # Each dict in `deco_terms` contains two dicts: The equivalent of the old dict as `tree` and the new list `knots`.
    # `tree` has `knot` where the old dict had `functor`. `knots` assigns these numbers to indices of `functors`.
    deco_terms = []
    for old in raw_deco_terms:
        knot_to_functor = []
        new = replace_functors(old, functors, knot_to_functor)
        deco_terms.append({
            'tree': new,
            'knots': knot_to_functor
        })

    term_tables = []
    for d in deco_terms:
        table = decomposed_term_to_table(d['tree'])
        term_tables.append(table)

    return {
        'matrix': matrix,
        'rows': number_of_rows,
        'cols': number_of_cols,
        'mincol': min_col,
        'terms': deco_terms,
        'tables': term_tables,
        'functors': functors
    }

import re

from ..utils.terms import decompose, find_functors, sort_functors, replace_functors


def decomposed_term_to_table(d):
    table = []
    table_maker(d, table)
    width = table[0][0]['span']
    table_filler(table, width)
    return table


def table_maker(d, table, col=0):
    # Creates an array that can be used to build an HTML table illustrating the tree stucture of the root term `d`.
    # `d` is the term decomposed to a dict.
    # `table` is the array of (rank) rows and (knot) cells. It is empty at the beginning.
    # `col` is the column index of the table cell. It is only passed as an argument to be passed on to `cell`.
    # Returns number of leafs of knot `d`, which is the colspan of the table cell corresponding to `d`.
    if type(d) is dict:
        row = d['rank']
        if len(table) == row:  # if no row for current rank yet (but only those for the ranks before)
            table.append([])   # add new row
        if d['ary'] > 0:
            span = table_maker(d['arg'], table, col)
        else:
            span = 1
        cell = {'col': col, 'span': span, 'entry': d['knot']}
        table[row].append(cell)
        return span
    elif type(d) is list:
        spansum = 0
        for item in d:
            span = table_maker(item, table, col+spansum)
            spansum += span
        return spansum


def table_filler(table, width):
    for row in table:
        spansum = 0
        for cell in row:
            spansum += cell['span']
        if not spansum == width:
            gaps = []
            needed_col = 0
            for index, cell in enumerate(row):
                found_col = cell['col']
                if found_col > needed_col:
                    gap = {'col': needed_col, 'span': found_col-needed_col, 'entry': 'gap'}
                    gaps.append((index, gap))
                needed_col = found_col + cell['span']
            if not needed_col == width:
                gap = {'col': needed_col, 'span': width-needed_col, 'entry': 'gap'}
                gaps.append((index+1, gap))
            for index, gap in gaps[::-1]:  # from right to left, so indices on the left remain correct after changes on the right
                row.insert(index, gap)


def term_to_table(term):
    deco = decompose(term)
    return decomposed_term_to_table(deco)


def term_to_table_fancy(input_term):
    term = re.sub('\s', '', input_term)

    if len(term) > 1000:
        raise ValueError('term with more than 1000 characters')

    deco = decompose(term)
    functors = sort_functors(find_functors(deco))
    knot_to_functor = []
    deco_clean = replace_functors(deco, functors, knot_to_functor)
    table = decomposed_term_to_table(deco_clean)

    return {
        'tree': deco_clean,
        'knots': knot_to_functor,
        'table': table,
        'functors': functors
    }

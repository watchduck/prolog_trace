def decompose(input_term, rank=0):
    term = input_term.replace(' ', '')

    def is_expected(candidate):
        if 'alnum' in expected:
            if not candidate in ['(', ')', ',']:
                return True
        if 'open' in expected:
            if candidate == '(':
                return True
        if 'close' in expected:
            if candidate == ')':
                return True
        if 'comma' in expected:
            if candidate == ',':
                return True
        return False

    level = 0  # position at the beginning is not between any brackets
    commas = [-1]  # positions of commas on level 0
    expected = ['alnum']

    for i, char in enumerate(term):
        if not is_expected(char):
            raise ValueError('wrong sequence of characters')
        if char == '(':
            level += 1
            expected = ['alnum']
        elif char == ')':
            level -= 1
            expected = ['comma', 'close']
        elif char == ',':
            if level == 0:
                commas.append(i)
            expected = ['alnum']
        else:  # alphanumeric
            expected = ['alnum', 'comma', 'open', 'close']

    if level != 0:
        raise ValueError('number of opening and closing brackets not equal')

    if len(commas) == 1:  # SINGLE (only the initial -1 is in `commas`)
        if '(' in term:  # complex
            term = term[:-1]  # remove closing bracket at the end
            split = term.index('(')
            term_fun = term[:split]  # functor
            term_arg = term[split+1:]  # argument(s)
            deco_arg = decompose(term_arg, rank+1)
            arity = len(deco_arg) if type(deco_arg) is list else 1
            return {
                'rank': rank,
                'functor': term_fun,
                'ary': arity,
                'arg': deco_arg
            }
        else:  # atom
            return {
                'rank': rank,
                'functor': term,
                'ary': 0
            }
    else:  # MULTIPLE
        terms = [term[i+1:j] for i,j in zip(commas, commas[1:]+[None])]
        term_dicts = []
        for term in terms:
            term_dicts.append(decompose(term, rank))
        return term_dicts


def recompose(d):
    # the inverse of `decompose`, only used for testing
    if type(d) is dict:
        if d['ary'] > 0:
            return d['functor'] + '(' + recompose(d['arg']) + ')'
        else:
            return d['functor']
    elif type(d) is list:
        results = []
        for item in d:
            results.append(recompose(item))
        return ', '.join(results)  # arguments separated by comma and space


def find_functors(d):
    # find the functors and their arity in a decomposed term, return set of pairs (str name, int arity)
    f = set()
    if type(d) is dict:
        if d['ary'] > 0:
            f.add((d['functor'], d['ary']))
            f = f.union(find_functors(d['arg']))
        else:
            f.add((d['functor'], 0))
    elif type(d) is list:
        for item in d:
            f = f.union(find_functors(item))
    return f


def sort_functors(raw_functors):
    sorted_functors = sorted(
        raw_functors,
        key=lambda tup: (-tup[1], tup[0])  # first descending by arity, then ascending by name
    )
    functors = []
    for name, ary in sorted_functors:
        functors.append({'name': name, 'ary': ary})
    return functors


def replace_functors(d, functors, k2f, parent=None):
    """
    :param d: old dict with functor name as `functor`
    :param functors: list of all functors as dicts of `name` and `ary`, only used to find the index of a pair
    :param k2f: knot to functor, empty when the function is first called, filled with functor index for each knot
    :param parent: current knot index passed down to children
    :return: `new_dict` if `d` is a dict, list of new dicts if `d` is list of old dicts
    """
    if type(d) is dict:
        knot = len(k2f)  # the index of the current knot is the length of the list until now
        new_dict = {
            'parent': parent,
            'rank': d['rank'],
            'ary': d['ary'],
            'knot': knot
        }
        functor = {'name': d['functor'], 'ary': d['ary']}
        k2f.append(functors.index(functor))
        if d['ary'] > 0:
            new_dict['arg'] = replace_functors(d['arg'], functors, k2f, knot)
        return new_dict
    elif type(d) is list:
        results = []
        for i, item in enumerate(d):
            results.append(replace_functors(item, functors, k2f, parent))
        return results

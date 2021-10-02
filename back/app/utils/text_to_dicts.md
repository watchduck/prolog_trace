The variable examples below result from the following example input, which is not a real Prolog trace.

### `text`
```
Redo: (8) a(b, c) ? creep
Call: (9) a(a, a(a)) ? creep
Fail: (9) a(a, a(a)) ? creep
Exit: (8) a(b) ? creep
```

### `acts`
The actions are represented by their first letters: `{'Call': 'c', 'Redo': 'r', 'Fail': 'f', 'Exit': 'e'}`
### `terms`
```python
['a(a, a(a))', 'a(b)', 'a(b, c)']
```

### `lines`
The subsequent text lines with `(9) a(a, a(a))` have been combined in one line dict.
<table><tr><td><pre>
[
    {'act':  'r', 'term': 2, 'row': 0, 'col': 0}, 
    {'act': 'cf', 'term': 0, 'row': 0, 'col': 1}, 
    {'act':  'e', 'term': 1, 'row': 1, 'col': 0}
]

</pre>
<td>
    <table>
        <tr><th>action<th>term
        <tr><td> Redo       <td> <code>a(b, c)</code>
        <tr><td> Call+Fail  <td> <code>a(a, a(a))</code>
        <tr><td> Exit       <td> <code>a(b)</code>
    </table>
</table>

### `matrix`
<table><tr><td><pre>
[
    [{'act': 'r', 'term': 2}, {'act': 'cf', 'term': 0}],
    [{'act': 'e', 'term': 1},           None          ]
]
</pre>
<td>
    <table>
        <tr>
            <td>Redo <code>a(b, c)</code>
            <td>Call+Fail <code>a(a, a(a))</code>
        <tr>
            <td>Exit <code>a(b)</code>
            <td>
    </table>
</table>

### `raw_deco_terms`
```python
[
    {'rank': 0, 'functor': 'a', 'ary': 2, 'arg': [{'rank': 1, 'functor': 'a', 'ary': 0}, {'rank': 1, 'functor': 'a', 'ary': 1, 'arg': {'rank': 2, 'functor': 'a', 'ary': 0}}]}, 
    {'rank': 0, 'functor': 'a', 'ary': 1, 'arg': {'rank': 1, 'functor': 'b', 'ary': 0}}, 
    {'rank': 0, 'functor': 'a', 'ary': 2, 'arg': [{'rank': 1, 'functor': 'b', 'ary': 0}, {'rank': 1, 'functor': 'c', 'ary': 0}]}
]
```

### `functors`
(First generated as the set `raw_functors`: `{('a', 1), ('b', 0), ('a', 0), ('a', 2), ('c', 0)}`)
```python
[
    {'name': 'a', 'ary': 2},   # 0
    {'name': 'a', 'ary': 1},   # 1
    {'name': 'a', 'ary': 0},   # 2
    {'name': 'b', 'ary': 0},   # 3
    {'name': 'c', 'ary': 0}    # 4
]
```

### `deco_terms`
In `tree` the `knot` numbers simply assign a unique number to each knot in the tree.<br>
In `knots` each knot is assigned its functor as an index number of `functors`.<br>
E.g. in the first term knots 1 and 3 are both functor 2, namely the `a` with arity 0.
```python
[
    {
        'tree': {'parent': None, 'rank': 0, 'ary': 2, 'knot': 0, 'arg': [{'parent': 0, 'rank': 1, 'ary': 0, 'knot': 1}, {'parent': 0, 'rank': 1, 'ary': 1, 'knot': 2, 'arg': {'parent': 2, 'rank': 2, 'ary': 0, 'knot': 3}}]}, 
        'knots': [0, 2, 1, 2]
    }, 
    {
        'tree': {'parent': None, 'rank': 0, 'ary': 1, 'knot': 0, 'arg': {'parent': 0, 'rank': 1, 'ary': 0, 'knot': 1}}, 
        'knots': [1, 3]
    }, 
    {
        'tree': {'parent': None, 'rank': 0, 'ary': 2, 'knot': 0, 'arg': [{'parent': 0, 'rank': 1, 'ary': 0, 'knot': 1}, {'parent': 0, 'rank': 1, 'ary': 0, 'knot': 2}]}, 
        'knots': [0, 3, 4]
    }
]
```

### `term_tables`
Each entry describes an HTML table describing the tree corresponding to this term. (Shown on the right.)<br>
The `entry` in the dict of a knot cell is an index of the term's `knots` list (not of `functors`!).<br>
In case the cell is just a filler between knot cells the entry is `'gap'`.
<table><tr><td rowspan="3"><pre>
[
    [
        [{'col': 0, 'span': 2, 'entry': 0}], 
        [{'col': 0, 'span': 1, 'entry': 1}, {'col': 1, 'span': 1, 'entry': 2}], 
        [{'col': 0, 'span': 1, 'entry': 'gap'}, {'col': 1, 'span': 1, 'entry': 3}]
    ],
    [
        [{'col': 0, 'span': 1, 'entry': 0}], 
        [{'col': 0, 'span': 1, 'entry': 1}]
    ], 
    [
        [{'col': 0, 'span': 2, 'entry': 0}], 
        [{'col': 0, 'span': 1, 'entry': 1}, {'col': 1, 'span': 1, 'entry': 2}]
    ]
]</pre>
<td>
    <table>
        <tr><td colspan="2"> a
        <tr><td> a <td> a
        <tr><td> (gap) <td> a
    </table>
<tr><td>
    <table>
        <tr><td>a
        <tr><td>b
    </table>
<tr><td>
    <table>
        <tr><td colspan="2">a
        <tr><td>b<td>c
    </table>
</table>

### returned dict converted to JSON
```json
{
    "matrix": [[{"act": "r", "term": 2}, {"act": "cf", "term": 0}], [{"act": "e", "term": 1}, null]], 
    "rows": 2, 
    "cols": 2, 
    "mincol": 8, 
    "terms": [{"tree": {"parent": null, "rank": 0, "ary": 2, "knot": 0, "arg": [{"parent": 0, "rank": 1, "ary": 0, "knot": 1}, {"parent": 0, "rank": 1, "ary": 1, "knot": 2, "arg": {"parent": 2, "rank": 2, "ary": 0, "knot": 3}}]}, "knots": [0, 2, 1, 2]}, {"tree": {"parent": null, "rank": 0, "ary": 1, "knot": 0, "arg": {"parent": 0, "rank": 1, "ary": 0, "knot": 1}}, "knots": [1, 3]}, {"tree": {"parent": null, "rank": 0, "ary": 2, "knot": 0, "arg": [{"parent": 0, "rank": 1, "ary": 0, "knot": 1}, {"parent": 0, "rank": 1, "ary": 0, "knot": 2}]}, "knots": [0, 3, 4]}], 
    "tables": [[[{"col": 0, "span": 2, "entry": 0}], [{"col": 0, "span": 1, "entry": 1}, {"col": 1, "span": 1, "entry": 2}], [{"col": 0, "span": 1, "entry": "gap"}, {"col": 1, "span": 1, "entry": 3}]], [[{"col": 0, "span": 1, "entry": 0}], [{"col": 0, "span": 1, "entry": 1}]], [[{"col": 0, "span": 2, "entry": 0}], [{"col": 0, "span": 1, "entry": 1}, {"col": 1, "span": 1, "entry": 2}]]], 
    "functors": [{"name": "a", "ary": 2}, {"name": "a", "ary": 1}, {"name": "a", "ary": 0}, {"name": "b", "ary": 0}, {"name": "c", "ary": 0}]
}
```
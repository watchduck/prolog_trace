This app converts the trace of [SWI-Prolog](https://en.wikipedia.org/wiki/SWI-Prolog) into a readable interactive table.
The following screenshots show a console output and the two versions of the corresponding table in the app.
(This is the second example shown on the page.)

<table>
    <tr>
    <td><img src=".img/jealous_table_brackets.png">
    <td rowspan="2"><img src=".img/jealous_table_trees.png">
    <tr>
    <td><img src=".img/jealous_console.png">
</table>

The app is not quite ready for use in [RL](https://en.wikipedia.org/wiki/Real_life), because it does not recognize
infix operators.<br>E.g. `alice\=clara` has been converted to `\=(alice, clara)` to make the example above work.

The backend uses Django REST framework and the frontend is written in Vue.js.

The app can be found at **[prolog-trace.watchduck.net](https://prolog-trace.watchduck.net)**.<br>
(The backend API is [backend.prolog-trace.watchduck.net/trace](https://backend.prolog-trace.watchduck.net/trace).) 

An important part of the backend is
[text_to_dicts.py](back/app/utils/text_to_dicts.py),
which is explained in
[text_to_dicts.md](back/app/utils/text_to_dicts.md).

The formulas in the table cells can be represented in two ways:<br>Linear formulas with parentheses,
and little tables representing the [tree structure](https://en.wikipedia.org/wiki/Tree_structure).

The following screenshot shows the tree structure for a result in a common Prolog example about travel routes,<br>
namely the question how to get from Valmont to Bangkok. (This is the fourth example shown on the page.)
<table>
    <tr>
        <td><img src=".img/travel_result_tree.png">
        <td>
            <a href="https://commons.wikimedia.org/wiki/File:Prolog_travel_graph.svg">
                <img width="200px" src=".img/travel_graph.svg">
            </a>
</table>

A proof of concept for these little tables is the separate [tree_table](https://github.com/watchduck/tree_table) app,
which uses the same backend.<br>
It can be found at **[tree-table.watchduck.net](https://tree-table.watchduck.net)**.

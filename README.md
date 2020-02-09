This app converts the trace of [SWI-Prolog](https://en.wikipedia.org/wiki/SWI-Prolog) into a readable interactive table.
The following screenshots show a console output and the two versions of the corresponding table in the app.
(This is the second example shown on the page.)

<table>
<tr>
<td>
<img src="https://user-images.githubusercontent.com/8267930/74093601-72eedb80-4ad4-11ea-85c3-42d2ced89025.png">
<td rowspan="2">
<img src="https://user-images.githubusercontent.com/8267930/74093602-77b38f80-4ad4-11ea-918e-bca52adc926f.png">
<tr>
<td><img src="https://user-images.githubusercontent.com/8267930/74093597-6e2a2780-4ad4-11ea-9554-7effe614db51.png">
</table>

The backend uses Django REST framework and the frontend is written in Vue.js.
(Like my [DAG](https://github.com/watchduck/DAG) app.)

The app can be found at **[prologtrace1.watchduck.net](http://prologtrace1.watchduck.net)**.
(The backend API is [back-prologtrace1.watchduck.net/trace](http://back-prologtrace1.watchduck.net/trace).)<br>
An important part of the backend is
[text_to_dicts.py](https://github.com/watchduck/prolog_trace_backend/blob/9c11088d35d9c9e1fd9434c428ca84232331b68b/app/utils/text_to_dicts.py),
which is explained in
[text_to_dicts.md](https://github.com/watchduck/prolog_trace_backend/blob/9c11088d35d9c9e1fd9434c428ca84232331b68b/app/utils/text_to_dicts.md).

For the formulas in the table cells one the choose between two formats: Linear formulas with parentheses,
and [tree structures](https://en.wikipedia.org/wiki/Tree_structure) that are themselves little tables.

The following screenshot shows the tree structure for a result in a
[common Prolog example](https://commons.wikimedia.org/wiki/File:Prolog_travel_graph.svg)
about travel routes,<br>
namely the question how to get from Valmont to Bangkok. (This is the fourth example shown on the page.)
![travel_result_table](https://user-images.githubusercontent.com/8267930/74094413-15ad5700-4ae1-11ea-8fd3-64cca8be47fd.png)


A proof of concept for these little tables is the separate [tree_table](https://github.com/watchduck/tree_table) app,
which uses the same backend.<br>
It can be found at **[treetable.watchduck.net](http://treetable.watchduck.net)**.

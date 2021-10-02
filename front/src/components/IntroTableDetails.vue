<template>
  <td colspan="5">


    <template v-if="id==0">
      <p>
        The knowledge base states that Anna is happy if she is rich and famous,
        and that she is in fact rich.<br>
        It also states that Bob is famous, so Prolog will not complain about the undefined <code>famous/1</code>.
      </p>
      <pre>{{kb[0]}}</pre>
      <p>
        <code>happy(anna)</code> is false, because Anna is not famous.<br>
        The six rows of the trace correspond to four fields in the resulting 3×2 table,<br>
        because two of them represent both the opening <i>call</i> and the closing <i>exit</i> or <i>fail</i>.</p>
    </template>


    <template v-if="id==1">
      <pre>{{kb[1]}}</pre>
      <p>
        The one answer to <code>jealous(alice, C)</code> is <code>C = clara</code>.<br>
        Bob loves both Alice and Clara, but Alice is only jealous of Clara, not of herself.
      </p>
      <p>
        Actually Prolog shows the comparisons in infix notation,
        which this app does not currently recognize.<br>
        So for this example they have been changed from the form <code>alice\=clara</code> to <code>\=(alice, clara)</code>.
      </p>
    </template>


    <template v-if="id==2">
      <pre>{{kb[2]}}</pre>
      <p>
        <code>descend(a, e)</code> is true, because <i>a</i> is the great-great-grandchild of <i>e</i>.
      </p>
    </template>


    <template v-if="id==3">
      <p>
        <a href="https://commons.wikimedia.org/wiki/File:Prolog_travel_graph.svg">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Prolog_travel_graph.svg/250px-Prolog_travel_graph.svg.png"
               width="250px" align="right">
        </a>
        These travel paths are a
        <a href="http://cs.union.edu/~striegnk/courses/esslli04prolog/practical.day2.php?s=practical.day2.node6">common example</a>
        for recursion in Prolog.
      </p>
      <pre>{{kb[3]}}</pre>
      <p>
        <code>spd(valmont, Path, bangkok)</code> finds two travel routes from Valmont to Bangkok.<br>
        This trace is for the first route via Saarbrücken.
      </p>
      <p>
        The following is the last term in the trace.<br>
        In the middle (marked with <code>% PATH</code>) is the value returned for <code>Path</code>.
      </p>
      <pre>{{path}}</pre>
    </template>


  </td>
</template>

<script>
  import kb0 from './textfiles/kb0.txt';
  import kb1 from './textfiles/kb1.txt';
  import kb2 from './textfiles/kb2.txt';
  import kb3 from './textfiles/kb3.txt';
  import path from './textfiles/path.txt';

  export default {
    data() { return {
      kb: [kb0, kb1, kb2, kb3],
      path: path
    }},
    props: ['id']
  }
</script>

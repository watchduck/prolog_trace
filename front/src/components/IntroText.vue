<template>
  <div id="intro-text">

    <div id="octocat">
      <a href="https://github.com/watchduck/prolog_trace">
        <img src="../../../.img/GitHub-Mark.png" width="40px">
      </a>
    </div>

    <div>
      This app converts the console output of <a href="https://en.wikipedia.org/wiki/SWI-Prolog">SWI-Prolog</a>
      trace into a more readable table.
    </div>

    <div>
      Its columns correspond to the parenthesized numbers in the console lines.<br>
      The actions at the start of each line are expressed by background colors:
      <table id="legend">
        <tr>
          <td class="c">Call</td>
          <td class="r">Redo</td>
          <td class="f">Fail</td>
          <td class="e">Exit</td>
        </tr>
        <tr>
          <th colspan="2">(opening)</th>
          <th colspan="2">(closing)</th>
        </tr>
      </table>
      Often a <i>call</i> is directly followed by <i>fail</i> or <i>exit</i>.
      In the table such a pair is represented by only one cell.<br>
      It has red or green background, and is marked with a blue triangle in the top left corner.
    </div>

    <div>
      Initially the terms are shown with parentheses. They can also be shown as trees (in the form of little tables).<br>
      All functors or atoms are listed in a separate table, where they can be renamed.<br>
    </div>

    <div>
      Here are some examples to see how the app works:<br>
    </div>

    <intro-table></intro-table>

  </div>
</template>

<script>
  import IntroTable from './IntroTable.vue'

  export default {
    components: {IntroTable}
  }
</script>

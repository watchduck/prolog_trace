<template>
  <table id="matrix-table">

    <tr>
      <th></th>  <!-- empty cell to over the row labels -->
      <th v-for="c in o.cols" class="colindex">
        {{c - 1 + o.mincol}}  <!-- c is counted from 1 -->
      </th>
    </tr>

    <tr v-for="(row, rowindex) in o.matrix">
      <th class="rowindex">{{rowindex + 1}}</th>
      <template v-for="(cell, colindex) in row">

        <td v-if="!cell"></td>  <!--entry `null`-->

        <td v-else :class="cell.act">

          <term-table v-if="$store.state.showTermTables"
                      :term="o.terms[cell.term]"
                      :table="o.tables[cell.term]"
                      :matrow="rowindex"
                      :matcol="colindex"></term-table>

          <term-formula v-else
                        :term="o.terms[cell.term]"
                        :row="rowindex"
                        :col="colindex"></term-formula>

        </td>

      </template>
    </tr>

  </table>
</template>

<script>
  import TermFormula from './TermFormula.vue';
  import TermTable from './TermTable.vue';

  export default {
    computed: {
      o() { return this.$store.state.output },

    },
    components: {TermFormula, TermTable}
  }
</script>

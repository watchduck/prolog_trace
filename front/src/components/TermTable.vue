<template>
  <table class="term-table">
    <tr v-for="tabrow in table">

      <template v-for="tabcell in tabrow">

        <term-table-cell
          v-if="tabcell.entry!='gap'"
          :tabcell="tabcell"
          :knot_to_functor="knot_to_functor"
          :matrow="matrow"
          :matcol="matcol"></term-table-cell>

        <td v-else
            class="gap"
            :colspan="tabcell.span"></td>

      </template>

    </tr>
  </table>
</template>

<script>
  import TermTableCell from './TermTableCell.vue';


  export default {
    computed: {
      knot_to_functor() { return this.term.knots }
    },
    props: ['term', 'table', 'matrow', 'matcol'],
    components: {TermTableCell}
  }
</script>

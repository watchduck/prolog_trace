<template>
  <td @mouseover="handleMouseover" @mouseleave="handleMouseleave"
      :colspan="tabcell.span"
      class="term-table-cell" :class="{focus: focused}">
    {{display}}
  </td>
</template>

<script>
  export default {
    computed: {
      functors() {
        return this.$store.state.output.functors
      },
      knot() {
        return this.tabcell.entry
      },
      functor() {
        return this.knot_to_functor[this.knot]
      },
      display() {
        let functor_index = this.knot_to_functor[this.knot];
        let name_or_cname = this.$store.state.showCustomNames ? 'cname' : 'name';
        return this.functors[functor_index][name_or_cname]
      },
      focus() {
        return this.$store.state.focus
      },
      focused() {
        return this.functor == this.focus.functor
      }
    },
    methods: {
      handleMouseover() {
        this.$store.commit('mutFocus', {row: this.matrow, col: this.matcol, knot: this.knot, functor: this.functor})
      },
      handleMouseleave() {
        this.$store.commit('mutUnfocus')
      }
    },
    props: ['tabcell', 'knot_to_functor', 'matrow', 'matcol']
  }
</script>

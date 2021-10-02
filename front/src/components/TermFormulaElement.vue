<template>
  <span @mouseover="handleMouseover" @mouseleave="handleMouseleave"
      class="term-formula-element" :class="highlight">{{display}}</span>
</template>

<script>
  export default {
    computed: {
      what() {
        return this.obj.what
      },
      which() {
        if (this.what=='comma') {
          return null
        } else {
          return this.obj.which
        }
      },
      functors() {
        return this.$store.state.output.functors
      },
      knot() {
        if (this.what=='knot') {
          return this.which
        } else {
          return this.obj.knot
        }
      },
      functor() {
        return this.knot_to_functor[this.knot]
      },
      display() {
        if (this.what=='knot') {
          let name_or_cname = this.$store.state.showCustomNames ? 'cname' : 'name';
          return this.functors[this.functor][name_or_cname]
        } else if (this.what=='bracket') {
          return this.which=='open' ? '(' : ')'
        } else {
          return ', '
        }
      },
      focus() {
        return this.$store.state.focus
      },
      highlight() {
        let isFocused = this.functor == this.focus.functor;
        let isSpecific = this.row == this.focus.row && this.col == this.focus.col && this.knot == this.focus.knot;
        let isText = this.what == 'knot';
        return {
          focus: isFocused,
          specific: isFocused && isSpecific,
          text: isFocused && isText
        }
      }
    },
    methods: {
      handleMouseover() {
        this.$store.commit('mutFocus', {row: this.row, col: this.col, knot: this.knot, functor: this.functor})
      },
      handleMouseleave() {
        this.$store.commit('mutUnfocus')
      }
    },
    props: ['obj', 'knot_to_functor', 'row', 'col']
  }
</script>


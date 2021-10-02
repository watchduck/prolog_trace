<template>
  <span class="term-formula">
    <term-formula-element
      v-for="(obj, i) in reco_list"
      :key="`el-${i}`"
      :obj="obj"
      :knot_to_functor="term.knots"
      :row="row"
      :col="col"></term-formula-element>
  </span>
</template>

<script>
  import TermFormulaElement from './TermFormulaElement.vue';

  export default {
    data() { return {
      reco_list: [],  // elements of the recomposed formula, i.e. knots mapped to functors, brackets and commas
    }},
    methods: {
      recompose(d) {
        if (!Array.isArray(d)) {  // `d` is no array, thus an object ("dictionary")
          this.reco_list.push({'what': 'knot', 'which': d.knot});
          if (d.ary > 0) {
            this.reco_list.push({'what': 'bracket', 'which': 'open', 'knot': d.knot});
            this.recompose(d.arg);
            this.reco_list.push({'what': 'bracket', 'which': 'close', 'knot': d.knot});
          }
        } else {  // `d` is an array ("list")
          for (let item of d) {
            this.recompose(item);
            this.reco_list.push({'what': 'comma', 'knot': item.parent});
          }
          this.reco_list.splice(-1, 1);  // remove comma before closing bracket
        }
      }
    },
    mounted() {
      this.recompose(this.term.tree);
    },
    props: ['term', 'row', 'col'],
    components: {TermFormulaElement}
  }
</script>

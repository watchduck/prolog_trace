<template>
  <div>
    <reset-link></reset-link>

    <matrix-table></matrix-table>

    <div id="opt-fun">
      <options></options>
      <functors-table></functors-table>
    </div>
  </div>
</template>

<script>
  import ResetLink from './ResetLink.vue';
  import MatrixTable from './MatrixTable.vue';
  import FunctorsTable from './FunctorsTable.vue';
  import Options from './Options.vue';

  export default {
    computed: {
      functors() { return this.$store.state.output.functors }
    },
    mounted() {
      for (let [id, functor] of this.functors.entries()) {
        // duplicate name as custom name (and temporary custom name) that can be edited
        this.$store.commit('mutCustomName', {id: id, val: functor.name})
      }
    },
    components: {ResetLink, MatrixTable, FunctorsTable, Options}
  }
</script>

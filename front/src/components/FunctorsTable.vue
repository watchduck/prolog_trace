<template>
  <table id="functors-table">
    <tr>
      <th>name</th>
      <th>arity</th>
      <th>custom name</th>
    </tr>
    <functor-row
      v-for="(functor, id) in functors"
      :key="`fun-${id}`"
      :functor="functor"
      :id="id"></functor-row>
  </table>
</template>

<script>
  import FunctorRow from './FunctorRow.vue';

  export default {
    computed: {
      functors() { return this.$store.state.output.functors }
    },
    components: {FunctorRow}
  }
</script>

<template>
  <div id="app">

    <p v-if="error" class="error">
      {{error}}
    </p>

    <div v-if="!showResults">
      <intro-text></intro-text>
      <textarea rows="20" v-model="input"></textarea>
      <button id="post" @click="post">create table</button>
    </div>
    <results v-else></results>

  </div>
</template>

<script>
  import IntroText from './components/IntroText.vue';
  import Results from './components/Results.vue';

  export default {
    computed: {
      input: {
        get() { return this.$store.state.input },
        set(val) { this.$store.commit('mutInput', val) }
      },
      showResults() { return this.$store.state.showResults },
      output() { return this.$store.state.output },
      error() { return this.$store.state.error }
    },
    methods: {
      post() {
        this.$store.dispatch('actPost', this.input)
      }
    },
    components: {Results, IntroText}
  }
</script>

<style lang="scss">
  @import "~styles/style.scss";
</style>

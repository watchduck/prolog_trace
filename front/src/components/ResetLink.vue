<template>
  <a id="reset" @click="reset">back to input</a>
</template>

<script>
  export default {
    methods: {
      reset() {
        this.$store.commit('mutReset')
      },
    }
  }
</script>

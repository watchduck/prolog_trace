<template>
  <table id="options">
    <tr>
      <td class="left">
        <label>entered names</label>
        <input v-model="showCustomNames" type="radio" :value="false">
      </td>
      <td class="right">
        <input v-model="showCustomNames" type="radio" :value="true">
        <label>custom names</label>
      </td>
    </tr>
    <tr>
      <td class="left">
        <label>term formulas</label>
        <input v-model="showTermTables" type="radio" :value="false">
      </td>
      <td class="right">
        <input v-model="showTermTables" type="radio" :value="true">
        <label>term trees</label>
      </td>
    </tr>
  </table>
</template>

<script>
  export default {
    computed: {
      showCustomNames: {
        get() { return this.$store.state.showCustomNames },
        set(val) { this.$store.commit('mutShowCustomNames', val) }
      },
      showTermTables: {
        get() { return this.$store.state.showTermTables },
        set(val) { this.$store.commit('mutShowTermTables', val) }
      },
    },
  }
</script>

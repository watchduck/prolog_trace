<template>
  <tbody>
    <tr class="permanent" :class="{showDetails: showDetails}">
      <td class="button">
        <button @click="fillInput">use</button>
      </td>
      <td>{{textSize}}</td>
      <td>{{tableSize}}</td>
      <td>{{description}}</td>
      <td class="button">
        <button @click="toggleDetails">{{toggleText}}</button>
      </td>
    </tr>
    <tr class="details" :class="{showDetails: showDetails}">
      <intro-table-details :id="id"></intro-table-details>
    </tr>
  </tbody>
</template>

<script>
  import IntroTableDetails from './IntroTableDetails.vue'

  export default {
    computed: {
      showDetails() {
        return this.id == this.showDetailsVal
      },
      toggleText() {
        return this.showDetails ? 'hide details' : 'show details'
      }
    },
    methods: {
      toggleDetails() {
        let val = this.showDetails ? null : this.id;
        this.$emit('toggle-details-event', val)
      },
      fillInput() {
        this.$store.commit('mutInput', this.inputText);
      }
    },
    props: ['textSize', 'tableSize', 'description', 'id', 'inputText', 'showDetailsVal'],
    components: {IntroTableDetails}
  }
</script>

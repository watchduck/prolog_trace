<template>
  <table id="intro-table">
    <tr>
      <th></th>
      <th>text lines</th>
      <th>table size</th>
      <th>description</th>
    </tr>

    <intro-table-body
      v-for="(dummy, id) in 4"
      :key="`itb-${id}`"
      :textSize="textSizes[id]"
      :tableSize="tableSizes[id]"
      :description="descriptions[id]"
      :id="id"
      :inputText="inputTexts[id]"
      :showDetailsVal="showDetailsVal"
      @toggle-details-event="toggleDetails"></intro-table-body>

  </table>
</template>

<script>
  import trace0 from './textfiles/trace0.txt';
  import trace1 from './textfiles/trace1.txt';
  import trace2 from './textfiles/trace2.txt';
  import trace3 from './textfiles/trace3.txt';

  import IntroTableBody from './IntroTableBody.vue'

  export default {
    data() { return {
      inputTexts: [
        trace0,
        trace1,
        trace2,
        trace3
      ],
      textSizes: [
        '6',
        '12',
        '25',
        '49'
      ],
      tableSizes: [
        '3 × 2',
        '9 × 2',
        '14 × 5',
        '22 × 5'
      ],
      descriptions: [
        'failing conjunction',
        'jealous',
        'descend',
        'travel path'
      ],
      showDetailsVal: null
    }},
    methods: {
      toggleDetails(val) {
        if (this.showDetailsVal == val) {
          this.showDetailsVal = null
        } else {
          this.showDetailsVal = val
        }
      },
      showDetails(n) {
        return n == this.showDetailsVal
      },
      toggleText(n) {
        return n == this.showDetailsVal ? 'hide details' : 'show details'
      },
      fillInput(n) {
        this.$store.commit('mutInput', this.texts[n]);
      }
    },
    components: {IntroTableBody}
  }
</script>

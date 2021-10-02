<template>
  <tr @mouseover="handleMouseover" @mouseleave="handleMouseleave"
    class="functor" :class="{focused: highlight}">

    <td :class="{light: customNameDifferent}">{{name}}</td>

    <td>{{arity}}</td>

    <td class="customName">
      <input type="text" v-model="customName" :class="{red: customNameIllegal}">
    </td>

  </tr>
</template>

<script>
  export default {
    computed: {
      name() {
        return this.functor.name
      },
      arity() {
        return this.functor.ary
      },
      customName: {
        get() {
          return this.functor.tcname
        },
        set(val) {
          this.$store.dispatch('actCustomName', {id: this.id, val: val})
        }
      },
      focus() {
        return this.$store.state.focus
      },
      highlight() {
        return this.id == this.focus.functor
      },
      customNameIllegal() {
        return this.$store.state.errorsCustomName.includes(this.id)
      },
      customNameDifferent() {
        return this.functor.name != this.functor.cname
      }
    },
    methods: {
      handleMouseover() {
        this.$store.commit('mutFocus', {knot: null, functor: this.id})
      },
      handleMouseleave() {
        this.$store.commit('mutUnfocus')
      }
    },
    props: ['functor', 'id']
  }
</script>

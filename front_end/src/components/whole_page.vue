<template>
  <div>
    <MoneyPie :username="test_case"/>
    <TypePie/>
  </div>
</template>

<script>
import mixin from '../test.js'
import MoneyPie from './money_pie.vue'
import TypePie from './type_pie.vue'

export default {
  name: "whole_page",
  mixins: [mixin],
  components: {
    MoneyPie,
    TypePie
  },
  data: () => ({
    test_case: []
  }),
  watch: {
    data(value) {
      console.log('data available!')
      this.test_case = value.money_pie
    },
  },
}
</script>

<style scoped>

</style>
<template>
  <div>
    <MoneyPie :username="test_case"/>
    <TypePie/>
  </div>
</template>

<script>
import pie_data from '../pie.js'
// import stat_data from '../stats.js'
// import wordCloud_data from '../wordCloud.js'
import MoneyPie from './money_pie.vue'
import TypePie from './type_pie.vue'

export default {
  name: "whole_page",
  mixins: [pie_data],
  components: {
    MoneyPie,
    TypePie
  },
  data: () => ({
    test_case: []
  }),
  created() {
    this.pie_url = `https://asoulmonitor.xyz/api/data/2021_9_10_22634198_dm_pie_picture.json`
    this.stats_url = `https://asoulmonitor.xyz/api/data/2021_9_10_22634198_dm_stats_picture.json`
    this.wordCloud_url = `https://asoulmonitor.xyz/api/data/2021_9_10_22634198_dm_word_cloud.json`
  },
  watch: {
    my_pie_data(value) {
      console.log('my_pie_data available!')
      this.test_case = value.money_pie
    },
    // my_stat_data(value) {
    //   console.log('my_stat_data available!' + value)
    // },
    // my_wordCloud_data(value) {
    //   console.log('my_wordCloud_data available!' + value)
    // },
  },
}
</script>

<style scoped>

</style>
<template>
  <div>
    <div v-for="info_str in global_list" :key="info_str">
    <router-link :to="'/' + info_str">
          <div>{{info_str}}</div>
    </router-link>
  </div>
  </div>
</template>

<script>
import mixin from '../global_list_mixin.js'
export default {
  name: "homepage",
  mixins: [mixin],
  data: () => ({
    global_list: []
  }),
  watch: {
    my_global_list(value) {
      // console.log(logs)
      this.global_list = value
      console.log(this.global_list[0])
    }
  },
  created() {
    this.global_list_url = `https://asoulmonitor.xyz/api/data/live_list.json`
  }
}
</script>

<style scoped>

</style>
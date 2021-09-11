export default {
  data: () => ({
    my_stat_data: []
  }),
  methods: {
    async update() {
      try {
        console.log("processed stats url once");
        const { data } = await this.$axios.get(this.stats_url)
        this.my_stat_data = data
        console.log(this.my_stat_data);
      } catch (error) {
        console.error(error)
      }
    },
  },
  mounted() {
    this.update()
  }
}
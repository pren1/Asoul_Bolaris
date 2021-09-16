export default {
  data: () => ({
    my_global_list: [],
    home_chart_list: []
  }),
  methods: {
    async update() {
      try {
        console.log("processed global list url once");
        const { data } = await this.$axios.get(this.global_list_url)
        this.my_global_list = data
        // console.log(this.my_global_list);
      } catch (error) {
        console.error(error)
      }

      try {
        console.log("processed home chart data url once");
        const { data } = await this.$axios.get(this.home_chart_url)
        this.home_chart_list = data
        // console.log(this.home_chart_list);
      } catch (error) {
        console.error(error)
      }
    },
  },
  mounted() {
    this.update()
  }
}
export default {
  data: () => ({
    my_pie_data: [],
    my_wordCloud_data: [],
    my_stat_data: []
  }),
  methods: {
    async update() {
      try {
        console.log("processed pie url once");
        const { data } = await this.$axios.get(this.pie_url)
        this.my_pie_data = data
        console.log(this.my_pie_data);
      } catch (error) {
        console.error(error)
      }

      try {
        console.log("processed wordCloud url once");
        const { data } = await this.$axios.get(this.wordCloud_url)
        this.my_wordCloud_data = data
        console.log(this.my_wordCloud_data);
      } catch (error) {
        console.error(error)
      }

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
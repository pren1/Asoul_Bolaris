export default {
  data: () => ({
    my_wordCloud_data: []
  }),
  methods: {
    async update() {
      try {
        console.log("processed wordCloud url once");
        const { data } = await this.$axios.get(this.wordCloud_url)
        this.my_wordCloud_data = data
        console.log(this.my_wordCloud_data);
      } catch (error) {
        console.error(error)
      }
    },
  },
  mounted() {
    this.update()
  }
}
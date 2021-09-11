export default {
  data: () => ({
    data: []
  }),
  methods: {
    async update() {
      try {
        console.log("update once");
        const { data } = await this.$axios.get(this.url)
        this.data = data
        console.log(this.data);
      } catch (error) {
        console.error(error)
      }
    },
  },
  mounted() {
    this.update()
  }
}

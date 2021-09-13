export default {
  data: () => ({
    my_global_list: []
  }),
  methods: {
    async update() {
      try {
        console.log("processed global list url once");
        const { data } = await this.$axios.get(this.global_list_url)
        this.my_global_list = data
        console.log(this.my_global_list);
      } catch (error) {
        console.error(error)
      }
    },
  },
  mounted() {
    this.update()
  }
}
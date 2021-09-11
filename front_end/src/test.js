// console.log("Process once")
// const data = [{ log1d: 1, logDetail: 'This is some log detail for log 1', logType: 'general', createdBy: 'name', CreatedAt: 'date' },
//             { log1d: 2, logDetail: 'This is some log detail for log 2', logType: 'general', createdBy: 'name2', CreatedAt: 'date2' },
//             { log1d: 3, logDetail: 'This is some log detail for log 3', logType: 'general', createdBy: 'name3', CreatedAt: 'date3' },
//             { log1d: 4, logDetail: 'This is some log detail for log 4', logType: 'general', createdBy: 'name4', CreatedAt: 'date4' }
//             ]
// export default data;

export default {
  data: () => ({
    data: []
  }),
  methods: {
    async update() {
      try {
        console.log("processed once");
        const { data } = await this.$axios.get('https://asoulmonitor.xyz/api/data/2021_9_10_22634198_dm_pie_picture.json')
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
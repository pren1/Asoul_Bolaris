<template>
  <div id="app">
<!--    <img alt="Vue logo" src="./assets/logo.png">-->
    <MoneyPie/>
    <TypePie/>
  </div>
</template>

<script>
import MoneyPie from './components/money_pie.vue'
import TypePie from './components/type_pie.vue'

export default {
  name: 'App',
  components: {
    MoneyPie,
    TypePie
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

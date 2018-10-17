<template>
  <div id="app">
    <router-view/>
  </div>
</template>


<script>
export default {
  name: 'App',
};
</script>

<style>
.header{
  text-align: center;
}
.temp-table{
  text-align: center;
  table-layout: fixed;
  margin: auto;
  width: 20%;
  color: azure;
}
.temp-table-header{
  background-image: linear-gradient(to bottom right, rgba(110, 3, 83, 0.6),rgba(173, 101, 6, 0.6));
}
.temp-alert{
  padding: 10px;
  background-image: linear-gradient(to bottom right,
  rgba(110, 3, 83, 0.6),rgba(173, 101, 6, 0.6));
}
tr:nth-child(even) {
  background-image: linear-gradient(to bottom right, rgba(110, 3, 83, 0.6),rgba(173, 101, 6, 0.6));
}
tr:nth-child(odd) {
  background-image: linear-gradient(to bottom right, rgba(173, 101, 6, 0.6),rgba(110, 3, 83, 0.6));
}
html,body, #app{
  height: 100%;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background:url('assets/img/home-bg.jpg');
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
  color: orange;
  text-align: center;
}
</style>

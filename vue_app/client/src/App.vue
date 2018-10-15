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
body{
  background-color: rgb(13, 152, 170);
}
.header{
  margin: 0px;
  text-align: center;
  background: bisque;
  color: black;
}
.temp-alert{
  padding: 10px;
  color: black;
}
.col-lg-4{
  margin: 10px;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: black;
}
</style>

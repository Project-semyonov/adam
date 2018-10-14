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
.temp-header{
    background: bisque;
    color: black;
  }
.temp-container h1{
  padding: 10px;
}
.homepage-header {
  background: bisque;
  color: black;
}
.homepage-container h1{
  padding: 10px;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: black;
}
</style>

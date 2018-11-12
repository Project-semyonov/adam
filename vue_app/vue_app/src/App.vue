<template>
  <div id="app">
    <div class="header">
      <div class="home-button">
        <router-link to="/home" tag="button" class="btn btn-danger">Homepage</router-link>
      </div>
      <router-link to="/camera" tag="button" class="btn btn-outline-warning"
        >Camera</router-link>
      <router-link to="/temp" tag="button" class="btn btn-outline-warning"
        >Temp Sensor</router-link>
      <div class="github-button">
        <a href="https://github.com/Project-semyonov/adam" tag="button"
        class="btn btn-outline-success">Github Repo</a>
      </div>
    </div>
    <router-view/>
  </div>
</template>

<style>
.header{
  text-align: center;
}
.home-button{
  float: left;
}
.github-button{
  float: right;
}
.temp-table{
  text-align: center;
  table-layout: fixed;
  margin: auto;
  width: 20%;
  color: azure;
}
.home-temp-table-header{
  text-align: left;
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
  background:url('assets/home-bg.jpg');
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
  color: orange;
  text-align: center;
}
</style>

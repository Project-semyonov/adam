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
.temp-output{
  padding: 10px;
  background-color: lightgrey;
  border-radius: 5px;
  background-image: linear-gradient(to bottom right,
  rgba(110, 3, 83, 0.6),rgba(173, 101, 6, 0.6));
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

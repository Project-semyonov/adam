<template>
  <div class="temp-container">
    <link href="https://afeld.github.io/emoji-css/emoji.css" rel="stylesheet">
    <h1>Temp Sensor</h1>
    <div class="temp-output">
      <button type="button" class="btn btn-info btn-sm"
      v-on:click="getTemps">Update Temp</button>
      <alert :message=message v-if="showMessage"></alert>
      <div v-for="temp in tempData">
        <h2>Time: {{temp.Time}}</h2>
        <h2>Temperature: {{temp.Temperature}}</h2>
        <h2>Date: {{temp.Date}}</h2>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Alert from './Alert'

export default {
  data () {
    return {
      tempData: [],
      message: '',
      showMessage: false
    }
  },
  components: {
    alert: Alert
  },
  methods: {
    getTemps () {
      const path = 'http://ec2-3-16-10-155.us-east-2.compute.amazonaws.com:5000/temp'
      // eslint-disable-next-line
      const updateTime = require('time-stamp')
      const currentTime = updateTime('HH:mm:ss')
      this.showMessage = true
      axios.get(path)
        .then((response) => {
          this.tempData = response.data
          // eslint-disable-next-line
          this.message = 'Got temps from the sensor at ' + currentTime + '! 🤘 '
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
          this.message = 'Failed to get temps from the sensor 🚨'
        })
    }
  },
  created () {
    this.getTemps()
  }
}

</script>

<template>
  <div class="homepage-container">
    <h1>Home</h1>
  </div>
</template>

<script>
import axios from 'axios'
import Alert from './Alert'

export default {
  data () {
    return {
      tempData: '',
      message: '',
      showMessage: false
    }
  },
  components: {
    alert: Alert
  },
  methods: {
    getTemps () {
      const path = 'http://localhost:5000/temp/all'
      // eslint-disable-next-line
      const updateTime = require('time-stamp')
      const currentTime = updateTime('HH:mm:ss')
      this.showMessage = true
      axios.get(path)
        .then((res) => {
          this.tempData = res.data
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

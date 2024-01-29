<template>
  <div class="nav-p">

    <div v-for="vehicle in vehicles" :key="vehicle.id">
      <!-- {{ vehicle.Plate }} -->
    </div>

  </div>
</template>

<script>
import { getAPI, getNewAPI } from '../axios'

export default {
  name: 'Home',
  data() {
    return {
      posts: [],
      vehicles: []
    }
  },

  async created() {
    getNewAPI.get('api/v1/vehicle/1')
      .then(response => {
        this.vehicles = response.data

      })
  }
}
</script>

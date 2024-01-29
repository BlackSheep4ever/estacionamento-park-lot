<template>
  <div class="nav-p">
    <div class="header">
      <h2 class="title">Cadastre seu automóvel</h2>
      <h4>Registre seu veículo para entrar numa vaga!</h4>

    </div>

    <div>
      <div class="input">
        <h4>Placa do carro</h4>
        <input v-model="formData.plate" type="text" />
      </div>

      <div class="input">
        <h4>Modelo do carro</h4>
        <input v-model="formData.carModel" type="text" />
      </div>
    </div>

    <div>
      <h4>Descrição</h4>
      <textarea v-model="formData.description" rows="3" style="height: auto;" type="text"></textarea>
    </div>

    <button class="btn" v-on:click="addVehicle()">Salvar</button>

    <h4 class="sub-t">Confirme seus dados pessoais e conclua seu registro!</h4>

    <div class="btn-group">
      <RouterLink class="btn" to="/">Cadastro</RouterLink>
    </div>
  </div>
</template>

<script>
import { getAPI } from '../axios'

export default {
  name: 'Home',
  data() {
    return {
      formData: {
        plate: "",
        carModel: "",
        description: ""
      },

    }
  },

  methods: {
    async addVehicle() {
      getAPI.post('api/v1/vehicle/1',
        this.formData)
        .then(alert("Dados salvos!"))
    },
  }
}

</script>

<template>
  <div class="nav-p">
    <div class="header">
      <h2 class="title">Cadastre-se no Park Roon</h2>
      <h4>Confirme seus dados pessoais e conclua seu registro!</h4>

    </div>

    <div>
      <div class="input">
        <h4>Nome</h4>
        <input v-model="formData.Name" type="text" />
      </div>

      <div class="input">
        <h4>Cartão de crédito</h4>
        <input v-model="formData.Card_id" type="text" />
      </div>
    </div>

    <button class="btn" v-on:click="addClient()">Salvar</button>

    <h4 class="sub-t">Complete seu cadastro e registre um veículo!</h4>

    <div class="btn-group">
      <RouterLink class="btn" to="/vehicle">Veículo</RouterLink>
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
        Name: "",
        Card_id: "",
      },

      posts: []
    }
  },

  methods: {
    async addClient() {
      getAPI.post('api/v1/customer/1',
        this.formData)
        .then(alert("Dados salvos!"))
    },
  }
}

</script>


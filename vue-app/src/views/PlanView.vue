<template>
  <div class="nav-p">
    <div class="header">
      <h2 class="title">Planos Park Roon</h2>
      <h2 class="title">Teste grátis por 7 dias!</h2>
      <h4>Confirme seus dados pessoais e conclua seu registro antes de acionar um plano!</h4>

    </div>

    <div v-for="post in posts" :key="post.id">
      {{ post.Value }}
    </div>

    <div v-for="post in posts" :key="post.id">
      {{ post.Description }}
    </div>


    <h4 class="sub-t">Vamos supor que você teve 300 clientes entrando e saindo durante o dia todo, porém se apenas ficaram parados ao
      mesmo tempo até 10 carros, você está no plano de até 30 veículos.

      Esse modelo de cobrança permite ser mais justo e flexível, pois em época de baixo movimento sua cobrança vem menor.
      E também do que adianta ter um campo de futebol de espaço se a realidade é outra.</h4>

    <div class="btn-group">
      <button class="btn" to="/">Entrar em contato</button>
    </div>
  </div>
</template>

<script>
import { getAPI } from '../axios'

export default {
  name: 'Home',
  data() {
    return {
      posts: [],
    }
  },

  async created() {
    getAPI.get('api/v1/plan/1')
      .then(response => {
        this.posts = response.data
      })
  },
}
</script>
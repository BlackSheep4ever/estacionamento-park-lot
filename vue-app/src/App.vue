<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>


    <div class="">
      <nav class="btn-bg">
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/vehicle">Veículo</RouterLink>
        <RouterLink to="/client">Cliente</RouterLink>
        <RouterLink to="/plan">Plano</RouterLink>
        <RouterLink to="/contract">Contrato</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

nav {
  width: 100%;
  font-size: 18px;
  text-align: center;
  margin-top: 2rem;
  margin-bottom: 2rem;
  border-radius: 10px;
}

nav a.router-link-exact-active {
  color: var(--color-text);
  
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
  
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

.btn-bg {
  border-radius: 10px;
}


</style>

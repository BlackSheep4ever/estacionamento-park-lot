<template>
  <div class="nav-p">
    <div class="header">
      <h2 class="title">Contratos Park Roon</h2>
      <h4>Acompanhe seu tempo estacionado!</h4>

    </div>
    <div>
      <div class="input">
        <h4>Valor</h4>
        <input type="text" />
      </div>

      <div class="input">
        <h4>Valor Máximo</h4>
        <input type="text" />
      </div>

      <div class="input">
        <h4>Tempo</h4>
        <input type="text" />
      </div>
    </div>

    <div>
      <h4>Descrição</h4>
      <textarea rows="3" style="height: auto;" type="text"></textarea>
    </div>

    <h4 class="sub-t">Confirme seus dados pessoais e conclua seu registro!</h4>

    <div class="btn-group">
      <RouterLink class="btn" to="/vehicle">Veículo</RouterLink>
      <RouterLink class="btn" to="/">Buscar Vagas</RouterLink>
    </div>
  </div>
</template>

<script>
</script>
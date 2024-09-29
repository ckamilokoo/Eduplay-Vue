<template>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-24 max-w-4xl">
    <!-- Aumenta el valor de gap -->
    <RouterLink to="/video-historia" class="flex flex-col items-center">
      <!-- Alinea imágenes y títulos -->
      <img
        src="../assets/iconos_inicio/cilindro.png"
        alt="Cilindro"
        class="mb-4"
        height="150px"
        width="150px"
      />
      <h3 class="text-2xl font-bold mb-2 text-center animate-bounce">Empecemos</h3>
      <!-- Elimina pr-6 para centrar -->
    </RouterLink>

    <RouterLink to="/vista-Construtor" class="flex flex-col items-center">
      <img
        src="../assets/iconos_inicio/esfera.png"
        alt="Esfera"
        class="mb-4"
        height="150px"
        width="150px"
      />
      <h3 class="text-2xl font-bold mb-2 text-center animate-bounce">Construyamos</h3>
    </RouterLink>

    <RouterLink to="/vista-ingeniero" class="flex flex-col items-center">
      <img
        src="../assets/iconos_inicio/cuadrangular.png"
        alt="Cuadrangular"
        class="mb-4"
        height="150px"
        width="150px"
      />
      <h3 class="text-2xl font-bold mb-2 text-center animate-bounce">Programemos</h3>
    </RouterLink>

    <RouterLink to="/vista-final" class="flex flex-col items-center">
      <img
        src="../assets/iconos_inicio/piramide.png"
        alt="Pirámide"
        class="mb-4"
        height="150px"
        width="150px"
      />
      <h3 class="text-2xl font-bold mb-2 text-center animate-bounce">Presentemos</h3>
    </RouterLink>
  </div>
</template>

<script setup></script>

<style scoped>
/* Puedes agregar estilos adicionales aquí si lo deseas */
</style>

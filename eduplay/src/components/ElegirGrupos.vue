<template>
  <!-- Main -->
  <main class="flex-1 flex items-center justify-center py-6">
    <div class="text-center">
      <h1 class="text-4xl font-bold tracking-tighter sm:text-5xl mb-24">Elija Su Grupo</h1>

      <!-- Contenedor de las cards -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <!-- Cada tarjeta (card) -->
        <div class="border rounded-lg p-24 shadow-md bg-white max-w-lg">
          <h2 class="text-xl font-bold mb-2">Grupo 1</h2>
          <RouterLink to="/esperandoEquipo"> unirse </RouterLink>
        </div>

        <div class="border rounded-lg p-24 shadow-md bg-white max-w-lg">
          <h2 class="text-xl font-bold mb-2">Grupo 2</h2>
          <RouterLink to="/esperandoEquipo"> unirse </RouterLink>
        </div>

        <div class="border rounded-lg p-24 shadow-md bg-white max-w-lg">
          <h2 class="text-xl font-bold mb-2">Grupo 3</h2>
          <RouterLink to="/esperandoEquipo"> unirse </RouterLink>
        </div>

        <div class="border rounded-lg p-24 shadow-md bg-white max-w-lg">
          <h2 class="text-xl font-bold mb-2">Grupo 4</h2>
          <RouterLink to="/esperandoEquipo"> unirse </RouterLink>
        </div>

        <div class="border rounded-lg p-24 shadow-md bg-white max-w-lg">
          <h2 class="text-xl font-bold mb-2">Grupo 5</h2>
          <RouterLink to="/esperandoEquipo"> unirse </RouterLink>
        </div>

        <div class="border rounded-lg p-24 shadow-md bg-white max-w-lg">
          <h2 class="text-xl font-bold mb-2">Grupo 6</h2>
          <RouterLink to="/esperandoEquipo"> unirse </RouterLink>
        </div>
      </div>
    </div>
  </main>

  <!-- Fin Main -->

  <!-- Footer -->
</template>

<script setup>
import { RouterLink } from 'vue-router';
</script>

<style scoped></style>

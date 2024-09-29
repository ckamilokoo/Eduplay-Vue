<script setup lang="ts">
import { RouterView } from 'vue-router';
</script>

<template>
  <div class="flex h-screen">
    <!-- Sidebar -->
    <aside
      class="w-52 bg-[url('@/assets/fondo/fondo_eduplay.png')] border-r-2 border-orange-500 p-4 flex flex-col items-center"
    >
      <div>
        <RouterLink to="/" class="flex flex-col items-center">
          <img alt="Vue logo" class="logo" src="@/assets/EDUPLAY.png" width="200" height="200" />
        </RouterLink>
      </div>
      <h2 class="font-extrabold text-2xl text-pink-500 mb-6 text-center drop-shadow-lg">
        Grupo 1 🌟
      </h2>
      <ul class="flex flex-col items-center space-y-3">
        <li
          class="mb-2 text-lg text-blue-600 font-semibold hover:text-yellow-400 transition-all transform hover:scale-110"
        >
          👦 Camilo Campos
        </li>
        <li
          class="mb-2 text-lg text-blue-600 font-semibold hover:text-yellow-400 transition-all transform hover:scale-110"
        >
          👦 Camilo Campos
        </li>
        <li
          class="mb-2 text-lg text-blue-600 font-semibold hover:text-yellow-400 transition-all transform hover:scale-110"
        >
          👦 Camilo Campos
        </li>
        <li
          class="mb-2 text-lg text-blue-600 font-semibold hover:text-yellow-400 transition-all transform hover:scale-110"
        >
          👦 Camilo Campos
        </li>
      </ul>

      <button
        class="bg-orange-500 text-white font-bold py-2 px-4 rounded-full hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-orange-300 mt-4"
      >
        Guardar
      </button>
    </aside>

    <div class="flex flex-col flex-1 bg-[url('@/assets/fondo/fondo_eduplay.png')]">
      <!-- Header -->
      <header
        class="flex flex-col items-center h-20 px-4 border-b-2 border-orange-500 sm:h-24 md:px-6 lg:px-8"
      >
        <h1 class="text-center text-2xl font-extrabold text-green-500 shadow-lg">Colegio XXXX</h1>
        <hr class="my-1" />
        <h1 class="text-center text-2xl font-extrabold text-green-500 shadow-lg">2do. grado</h1>
      </header>

      <!-- Main Content -->
      <main class="flex-1 flex items-center justify-center py-6">
        <RouterView />
      </main>
    </div>
  </div>
</template>

<style scoped></style>

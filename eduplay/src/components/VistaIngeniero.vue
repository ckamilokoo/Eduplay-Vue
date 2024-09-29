<template>
  <div class="lego-playground">
    <div class="toy-border">
      <div class="toy-content">
        <h1 class="playground-title"></h1>
        <div v-if="!isConnected" class="connect-container">
          <ButtonConect />
        </div>
        <div v-else class="flex">
          <div class="w-5/5">
            <div class="flex justify-between">
              <button
                id="show-modal-left"
                @click="Instrucciones = true"
                class="bg-blue-400 text-white font-bold py-4 px-6 rounded-full shadow-lg hover:bg-blue-500 transition duration-300 text-2xl w-1/3"
              >
                Instrucciones
              </button>

              <button
                id="show-modal-right"
                @click="comandos = true"
                class="bg-green-400 text-white font-bold py-4 px-6 rounded-full shadow-lg hover:bg-green-500 transition duration-300 text-2xl w-1/3"
              >
                Comandos
              </button>
            </div>
            <!-- Ocupa el 80% -->
            <ButtonConect />
            <DropImagen />
          </div>
        </div>
      </div>

      <Teleport to="body">
        <!-- use the modal component, pass in the prop -->
        <modal :show="Instrucciones" @close="Instrucciones = false">
          <template #header>
            <h3
              class="text-2xl font-extrabold text-purple-500 bg-yellow-300 p-4 rounded-lg shadow-md mb-4"
            >
              El helicóptero debe ser funcional
            </h3>
          </template>

          <template #body>
            <h3 class="text-xl font-bold text-pink-500 mb-4 leading-relaxed">
              Para rescatar a alguien de un incendio el canasto de nuestro helicóptero debe bajar,
              detenerse, luego subir y volver a detenerse. Los recorridos de subida y bajada duran 5
              segundos cada uno, entonces deben ser cuidadosos en no sobrepasar ese tiempo porque el
              motor u otra pieza del helicóptero. Las flechas indican en que dirección se mueve el
              canasto de rescate y los cuadrados rojos.
            </h3>
            <h3 class="text-xl font-bold text-green-500 mb-4 leading-relaxed">
              Programa la secuencia correspondiente arrastrando los objetos a la línea de comandos.
              Observa el número de cada objeto, indica el tiempo que se ejecuta.
            </h3>
          </template>
        </modal>
      </Teleport>
      <Teleport to="body">
        <!-- use the modal component, pass in the prop -->
        <modal :show="comandos" @close="comandos = false">
          <template #header>
            <h3>El helicóptero debe ser funcional</h3>
          </template>
          <template #body>
            <h3>hola</h3>
          </template>
        </modal>
      </Teleport>
    </div>
  </div>
</template>

<script setup>
import DropImagen from '@/components/DragImagen.vue';
import ButtonConect from '@/components/Button_Connect.vue';
import { isConnected } from '../composables/store';
import Modal from './Modal_instrucciones.vue';

import { ref } from 'vue';

const Instrucciones = ref(false);
const comandos = ref(false);
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
  padding: 20px;
  font-family: 'Comic Sans MS', cursive, sans-serif;
}

/* Aplicar una transición suave al cambiar de estado conectado/desconectado */
.container-enter-active,
.container-leave-active {
  transition: opacity 0.5s;
}

.container-enter,
.container-leave-to {
  opacity: 0;
}
</style>

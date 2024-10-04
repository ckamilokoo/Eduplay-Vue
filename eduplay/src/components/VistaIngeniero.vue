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
            <div class="flex justify-between mb-3">
              <button id="show-modal-left" @click="Instrucciones = true" class="instruccion-button">
                Instrucciones
              </button>
              <ButtonConect />
              <button id="show-modal-right" @click="comandos = true" class="comando-button">
                Comandos
              </button>
            </div>
            <!-- Ocupa el 80% -->

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

/* Estilo específico para el botón de instrucciones */
.instruccion-button {
  background-color: green;
  font-weight: bold;
  padding: 10px 20px; /* tamaño de botón por defecto */
  border-radius: 9999px; /* redondear los botones */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s ease;
  font-size: 1.5rem; /* Color específico para Instrucciones */
}

/* Estilo específico para el botón de comandos */
.comando-button {
  background-color: blue;
  font-weight: bold;
  padding: 10px 20px; /* tamaño de botón por defecto */
  border-radius: 9999px; /* redondear los botones */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s ease;
  font-size: 1.5rem;
  /* Color específico para Comandos */
}

/* Efecto hover para Instrucciones */
.instruccion-button:hover {
  background-color: darkgreen; /* Color más oscuro en hover */
}

/* Efecto hover para Comandos */
.comando-button:hover {
  background-color: darkblue; /* Color más oscuro en hover */
}

/* Estilo por defecto para los botones */
.button {
  background-color: #60a5fa; /* color azul */
  color: white;
  font-weight: bold;
  padding: 10px 20px; /* tamaño de botón por defecto */
  border-radius: 9999px; /* redondear los botones */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s ease;
  font-size: 1.5rem; /* tamaño de texto por defecto */
}

/* Efecto hover */
.button:hover {
  background-color: #3b82f6; /* azul más oscuro */
}

/* Pantallas pequeñas */
@media (max-width: 640px) {
  .button {
    width: 80%; /* Botón ocupa el 80% del ancho */
    padding: 12px 0; /* tamaño de botón para pantallas pequeñas */
    font-size: 1.5rem; /* tamaño de texto para pantallas pequeñas */
  }
}

/* Pantallas medianas */
@media (min-width: 641px) and (max-width: 1024px) {
  .button {
    width: 20%; /* Botón ocupa el 60% del ancho */
    padding: 14px 0; /* tamaño de botón para pantallas medianas */
    font-size: 1rem;
    margin-bottom: 10px; /* tamaño de texto para pantallas medianas */
  }

  .instruccion-button {
    background-color: green;
    font-weight: bold;
    padding: 10px 20px; /* tamaño de botón por defecto */
    border-radius: 9999px; /* redondear los botones */
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    transition: background-color 0.3s ease;
    font-size: 1.5rem; /* Color específico para Instrucciones */
  }

  /* Estilo específico para el botón de comandos */
  .comando-button {
    background-color: blue;
    font-weight: bold;
    padding: 7px 15px; /* tamaño de botón por defecto */
    border-radius: 9999px; /* redondear los botones */
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    transition: background-color 0.3s ease;
    font-size: 1.5rem;
    /* Color específico para Comandos */
  }
}

/* Pantallas grandes */
@media (min-width: 1025px) {
  .button {
    width: 40%; /* Botón ocupa el 40% del ancho */
    padding: 16px 0; /* tamaño de botón para pantallas grandes */
    font-size: 2rem; /* tamaño de texto para pantallas grandes */
  }
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

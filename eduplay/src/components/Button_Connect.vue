<template>
  <div class="main-container">
    <div id="indicaciones" v-if="!isConnected" class="text-center">
      <h1 class="text-2xl font-bold text-black rounded-lg shadow-md">
        Conectemos el Helicóptero al tablet
      </h1>

      <h2 class="text-xl font-bold text-black p-1 rounded-lg shadow-md">
        1. Presiona durante 5 segundos el botón superior de tu helicóptero como se muestra en la
        imagen que sigue:
      </h2>
      <img
        src="../assets/hub.png"
        class="mx-auto"
        height="90px"
        width="90px"
        alt="Motor encendido"
      />
      <h2 class="text-xl font-bold text-black p-1 rounded-lg shadow-md">
        2. Activa el bluetooth del Tablet presionando el siguiente ícono:
      </h2>
      <img
        src="../assets/bluethooth.png"
        class="mx-auto"
        width="70px"
        height="70px"
        alt="Bluetooth"
      />
      <h2 class="text-xl font-bold text-black rounded-lg">
        Si se conectó a su modelo correctamente, debería mostrarse la siguiente pantalla
      </h2>
    </div>

    <!-- Aquí se añadió la clase mt-12 para bajar el contenedor -->
    <div :class="['button-container', { centered: !isConnected }]">
      <button
        v-if="!isConnected"
        @click="connectToWeDo"
        :class="{ connect: !isConnected, loading: isLoading }"
        class="mt-52"
        :disabled="isLoading"
      >
        <span v-if="isLoading">Buscando tu MODELO ...</span>
        <span v-else>Conectar MODELO</span>
      </button>

      <button
        v-else
        @click="disconnectFromWeDo"
        class="ml-10"
        :class="{ disconnect: isConnected, loading: isLoading }"
        :disabled="isLoading"
      >
        <span v-if="isLoading">Desconectando...</span>
        <span v-else>Desconectar MODELO</span>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { isConnected } from '../composables/store'; // Importar el estado global

const isLoading = ref(false);

// Variables globales para almacenar el dispositivo y servidor GATT
let device = null;
let server = null;
let motorCharacteristic = null;
let colorCharacteristic = null;

// Función para verificar si el dispositivo está conectado
const checkIfConnected = () => {
  return device && device.gatt && device.gatt.connected;
};

// Función para conectar al dispositivo WeDo usando Web Bluetooth API
const connectToWeDo = async () => {
  isLoading.value = true;
  try {
    device = await navigator.bluetooth.requestDevice({
      filters: [{ services: ['00001523-1212-efde-1523-785feabcd123'] }],
      optionalServices: ['00004f0e-1212-efde-1523-785feabcd123', 'battery_service'], // Servicios opcionales
    });

    server = await device.gatt.connect();

    // Obtener el servicio necesario para motor y color
    const inputService = await server.getPrimaryService('00004f0e-1212-efde-1523-785feabcd123');

    motorCharacteristic = await inputService.getCharacteristic(
      '00001565-1212-efde-1523-785feabcd123',
    );
    colorCharacteristic = await inputService.getCharacteristic(
      '00001565-1212-efde-1523-785feabcd123',
    );

    // Guardar el dispositivo y las características en `window` para asegurarse de que estén disponibles globalmente
    window.device = device;
    window.server = server;
    window.motorCharacteristic = motorCharacteristic;
    window.colorCharacteristic = colorCharacteristic;

    // Marcar como conectado si la conexión ha sido exitosa
    if (checkIfConnected()) {
      isConnected.value = true;
      console.log('Conectado a LEGO WeDo 2.0 con características disponibles.');
    } else {
      console.error('La conexión falló.');
      isConnected.value = false;
    }
  } catch (error) {
    console.error('Error conectando al dispositivo WeDo:', error);
    isConnected.value = false;
  } finally {
    isLoading.value = false;
  }
};

// Función para desconectar del dispositivo WeDo
const disconnectFromWeDo = async () => {
  isLoading.value = true;
  try {
    if (window.device && window.device.gatt.connected) {
      await window.device.gatt.disconnect();
      isConnected.value = false;
      console.log('Desconectado de LEGO WeDo 2.0');

      // Reiniciar las variables de dispositivo, servidor y características
      window.device = null;
      window.server = null;
      window.motorCharacteristic = null;
      window.colorCharacteristic = null;
    } else {
      console.log('No hay dispositivo conectado para desconectar.');
    }
  } catch (error) {
    console.error('Error desconectando del dispositivo WeDo:', error);
  } finally {
    isLoading.value = false;
  }
};
</script>

<style scoped>
.main-container {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

#indicaciones {
  flex: 1;
  max-width: 50%;
  background-color: url('@/assets/fondo/fondo_eduplay.png');
  padding: 3px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.button-container {
  flex: 1;
  max-width: 40%;
}

p {
  font-size: 15px;
}

button {
  padding: 2px 7px;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-bottom: 5px;
  transition: background-color 0.3s ease;
}

button.connect {
  background-color: #28a745;
  font-size: 40px;
}

button.disconnect {
  background-color: #dc3545;
  font-size: 20px;
  padding: 2px 3px;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-bottom: 2px;
  transition: background-color 0.3s ease;
}

button.connect:hover {
  background-color: #218838;
}

button.disconnect:hover {
  background-color: #c82333;
}

button.loading {
  background-color: #ffc107;
  cursor: wait;
}

button.loading:hover {
  background-color: #e0a800;
}
</style>

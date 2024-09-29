<template>
  <div :class="['button-container', { centered: !isConnected }]">
    <button
      v-if="!isConnected"
      @click="connectToWeDo"
      :class="{ connect: !isConnected, loading: isLoading }"
      :disabled="isLoading"
    >
      <span v-if="isLoading">Buscando tu MODELO ...</span>
      <span v-else>Conectar a tu MODELO </span>
    </button>
    <button
      v-else
      @click="disconnectFromWeDo"
      :class="{ disconnect: isConnected, loading: isLoading }"
      :disabled="isLoading"
    >
      <span v-if="isLoading">Desconectando...</span>
      <span v-else>Desconectar de tu MODELO</span>
    </button>
    <p v-if="isConnected">Conectado a tu MODELO</p>
    <p v-else>No está conectado a ningún MODELO</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { isConnected, connectedDevice } from '../composables/store'; // Importar el estado global

const isLoading = ref(false);

const connectToWeDo = async () => {
  isLoading.value = true;
  try {
    // Solicitar el dispositivo Bluetooth
    const device = await navigator.bluetooth.requestDevice({
      acceptAllDevices: true, // Cambia esto si conoces el nombre del dispositivo
      optionalServices: ['00001565-1212-efde-1523-785feabcd123'], // Asegúrate de incluir el UUID correcto
    });

    // Conectar al servidor GATT
    const server = await device.gatt.connect();
    console.log('Conectado a', device.name, 'server :', server);

    // Guardar el dispositivo globalmente
    connectedDevice.value = device;

    // Actualizar el estado a conectado
    isConnected.value = true;
  } catch (error) {
    console.error('Error conectando a WeDo:', error);
    isConnected.value = false; // Asegúrate de actualizar el estado en caso de error
  } finally {
    isLoading.value = false;
  }
};

const disconnectFromWeDo = async () => {
  isLoading.value = true;
  try {
    if (connectedDevice.value && connectedDevice.value.gatt.connected) {
      await connectedDevice.value.gatt.disconnect();
      console.log('Desconectado de', connectedDevice.value.name);

      // Limpiar el dispositivo global
      connectedDevice.value = null;

      // Actualizar el estado a no conectado
      isConnected.value = false;
    } else {
      console.log('No hay ningún dispositivo conectado');
    }
  } catch (error) {
    console.error('Error desconectando:', error);
  } finally {
    isLoading.value = false;
  }
};
</script>

<style scoped>
.button-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start; /* Alinea los botones al lado izquierdo por defecto */
  position: fixed; /* Mantiene la posición fija en la pantalla */
  top: 20px; /* Espacio desde el borde superior */
  left: 20px; /* Espacio desde el borde izquierdo */
  transition: all 0.3s ease; /* Transición para el cambio de ubicación */
}

p {
  font-size: 25px;
}

.button-container.centered {
  align-items: center; /* Centra los botones horizontalmente */
  left: 50%; /* Ajusta horizontalmente para centrar */
  transform: translateX(-50%); /* Ajusta la posición para centrar completamente */
  top: 50%; /* Ajusta verticalmente para centrar */
  transform: translateY(-50%) translateX(-50%); /* Ajusta la posición para centrar completamente */
}

button {
  padding: 10px 20px;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-bottom: 10px; /* Espacio entre botones */
  transition: background-color 0.3s ease; /* Transición para el cambio de color */
}

button.connect {
  background-color: #28a745; /* Verde para conectar */
  font-size: 40px;
}

button.disconnect {
  background-color: #dc3545; /* Rojo para desconectar */
  font-size: 30px;
}

button.connect:hover {
  background-color: #218838;
}

button.disconnect:hover {
  background-color: #c82333;
}

/* Estilos para cuando el botón está en estado de carga */
button.loading {
  background-color: #ffc107; /* Amarillo para indicar carga */
  cursor: wait; /* Cursor de espera */
}

button.loading:hover {
  background-color: #e0a800; /* Cambiar color en hover durante la carga */
}
</style>

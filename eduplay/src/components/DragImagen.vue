<template>
  <div>
    <div
      class="drop-zone"
      :class="{ 'drop-zone-dragging': draggin }"
      @dragover="handleDragOver"
      @dragenter="handleDragEnter"
      @dragleave="handleDragLeave"
      @drop="handleDrop"
    >
      <div v-if="!imagenes.length" class="placeholder">
        {{ draggin ? 'Suelta aquí' : 'Arrastra y suelta las imágenes' }}
      </div>
      <div v-else class="images-container">
        <img
          v-for="(img, index) in imagenes"
          :key="index"
          :src="img"
          class="uploaded-image"
          @click.stop
        />
      </div>
    </div>

    <div class="image-selection">
      <button class="fun-button clearbutton" @click="clearImages">Limpiar Imágenes</button>
      <button class="fun-button sendbutton" @click="sendCommands">Enviar Comandos</button>
      <div class="available-images">
        <img
          v-for="(img, index) in availableImages"
          :key="index"
          :src="img"
          class="selectable-image"
          @click="selectImage(img)"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const imagenes = ref([]);
const draggin = ref(false);
const maxImages = 7;

const availableImages = ref([
  '/src/assets/comandos/celeste.png',
  '/src/assets/comandos/rojo.png',
  '/src/assets/comandos/verde.png',
  '/src/assets/comandos/naranja.png',
  '/src/assets/comandos/izquierda.png',
  '/src/assets/comandos/derecha.png',
  '/src/assets/comandos/off.png',
]);

// Función para calcular el comando del motor en base a la velocidad
const getMotorCommand = (speed) => {
  let speedByte;
  if (speed < 0) {
    speedByte = 0x100 + speed; // Velocidad negativa (giro hacia atrás)
  } else {
    speedByte = speed; // Velocidad positiva (giro hacia adelante)
  }

  const command = new Uint8Array([0x01, 0x01, 0x01, speedByte]);
  return command;
};

// Lógica para controlar la duración del giro y cuántos giros hacer
const runMotorForTime = async (command, duration) => {
  if (window.motorCharacteristic) {
    try {
      await window.motorCharacteristic.writeValue(command);
      console.log(`Motor encendido con comando: ${command}`);

      // Detener el motor después de un tiempo
      return new Promise((resolve) => {
        setTimeout(async () => {
          const stopCommand = getMotorCommand(0); // Comando para detener el motor
          await window.motorCharacteristic.writeValue(stopCommand);
          console.log('Motor detenido.');
          resolve(); // Finaliza cuando el motor se detiene
        }, duration); // Detener el motor después del tiempo especificado
      });
    } catch (error) {
      console.error('Error enviando comando al motor:', error);
    }
  }
};

// Mapear imágenes a comandos de colores y motores
const colorMap = {
  '/src/assets/comandos/celeste.png': new Uint8Array([0x06, 0x04, 0x01, 0x03]),
  '/src/assets/comandos/rojo.png': new Uint8Array([0x06, 0x04, 0x01, 0x09]),
  '/src/assets/comandos/verde.png': new Uint8Array([0x06, 0x04, 0x01, 0x06]),
  '/src/assets/comandos/naranja.png': new Uint8Array([0x06, 0x04, 0x01, 0x08]),
  '/src/assets/comandos/off.png': new Uint8Array([0x06, 0x04, 0x01, 0x00]), // Apagar
};

// Usar la función `runMotorForTime` para controlar la duración del motor
const motorMap = {
  '/src/assets/comandos/izquierda.png': async () => {
    const command = getMotorCommand(-50); // Velocidad menor (-50)
    const duration = 700; // Duración en milisegundos para dos giros
    await runMotorForTime(command, duration);
  },
  '/src/assets/comandos/derecha.png': async () => {
    const command = getMotorCommand(50); // Velocidad menor (50)
    const duration = 700; // Duración en milisegundos para dos giros
    await runMotorForTime(command, duration);
  },
};

// Función para ejecutar comandos secuenciales
const executeSequentially = async (commands) => {
  for (const command of commands) {
    await command(); // Ejecutar cada comando y esperar a que termine antes de continuar
  }
};

// Enviar comandos de color y motor al dispositivo
const sendCommands = async () => {
  if (!window.motorCharacteristic || !window.colorCharacteristic) {
    console.log('No hay conexión con el dispositivo WeDo.');
    return;
  }

  const commands = []; // Almacenar los comandos a ejecutar

  try {
    for (const img of imagenes.value) {
      if (colorMap[img]) {
        console.log(`Enviando comando de color para: ${img}`);
        commands.push(async () => {
          await window.colorCharacteristic.writeValue(colorMap[img]);
        });
      } else if (motorMap[img]) {
        console.log(`Enviando comando de motor para: ${img}`);
        commands.push(motorMap[img]); // Agregar el comando del motor a la lista
      }
    }
    await executeSequentially(commands); // Ejecutar todos los comandos en secuencia
    console.log('Comandos enviados con éxito.');
  } catch (error) {
    console.error('Error enviando los comandos:', error);
  }
};

// Otros métodos...
const selectImage = (img) => {
  if (imagenes.value.length < maxImages) {
    imagenes.value.push(img);
  }
};

const clearImages = () => {
  imagenes.value = [];
};

const handleDragOver = (event) => {
  event.preventDefault();
};

const handleDragEnter = () => {
  draggin.value = true;
};

const handleDragLeave = () => {
  draggin.value = false;
};

const handleDrop = (event) => {
  event.preventDefault();
  draggin.value = false;
};
</script>

<style scoped>
.playful-container {
  position: relative;
  min-height: 100vh;
  background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
  padding: 20px;
  font-family: 'Comic Sans MS', cursive, sans-serif;
}

.title {
  text-align: center;
  font-size: 2.5rem;
  color: #ff6b6b;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
}

.drop-zone {
  background-color: rgba(255, 255, 255, 0.7);
  border: 4px dashed #4ecdc4;
  border-radius: 20px;
  padding: 20px;
  min-height: 200px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.drop-zone-dragging {
  background-color: rgba(255, 255, 255, 0.9);
  border-color: #ff6b6b;
  transform: scale(1.05);
}

.placeholder {
  font-size: 1.5rem;
  color: #4ecdc4;
  text-align: center;
}

.placeholder-highlight {
  color: #ff6b6b;
  font-weight: bold;
}

.images-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 15px;
}

.image-wrapper {
  transition: all 0.3s ease;
}

.uploaded-image {
  width: 80px;
  height: 80px;
  object-fit: contain;
  cursor: pointer;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.uploaded-image:hover {
  transform: scale(1.1);
}

.uploaded-image.dragged {
  opacity: 0.5;
  border: 2px solid #ff6b6b;
}

.image-selection {
  margin-top: 30px;
  display: flex;
  flex-direction: row;
  align-items: center;
}

.available-images {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
  margin-top: 20px;
}

.selectable-image-wrapper {
  transition: all 0.3s ease;
}

.selectable-image {
  width: 70px;
  height: 70px;
  object-fit: contain;
  cursor: pointer;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.selectable-image:hover {
  transform: scale(1.1);
}

.selectable-image.selected {
  border: 3px solid #ff6b6b;
}

.fun-button {
  padding: 10px 20px;
  font-size: 1rem;
  font-family: 'Comic Sans MS', cursive, sans-serif;
  border: none;
  border-radius: 50px;
  cursor: pointer;
  transition: all 0.3s ease;
  margin: 10px;
}

.clearbutton {
  background-color: #ff6b6b;
  color: white;
}

.sendbutton {
  background-color: #4ecdc4;
  color: white;
}

.fun-button:hover {
  transform: scale(1.1);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
}

.image-list-enter-active,
.image-list-leave-active {
  transition: all 0.5s ease;
}

.image-list-enter-from,
.image-list-leave-to {
  opacity: 0;
  transform: translateY(30px);
}
</style>

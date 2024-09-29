<template>
  <div class="playful-container">
    <h1 class="title">¡Juega con las imágenes!</h1>

    <div
      class="drop-zone"
      :class="{ 'drop-zone-dragging': draggin }"
      @dragover="handleDragOver"
      @dragenter="handleDragEnter"
      @dragleave="handleDragLeave"
      @drop="handleDrop"
    >
      <div
        v-if="!imagenes.length"
        class="placeholder"
        :class="{ 'placeholder-highlight': draggin }"
      >
        {{ draggin ? '¡Suéltalo aquí!' : '¡Arrastra y suelta las imágenes aquí!' }}
      </div>
      <div v-else class="images-container">
        <TransitionGroup name="image-list">
          <div
            v-for="(img, index) in imagenes"
            :key="index"
            class="image-wrapper"
            :style="randomRotation()"
          >
            <img
              :src="img"
              class="uploaded-image"
              @dragstart="handleDragStart(index, $event)"
              @dragover="handleDragOverImage($event, index)"
              @drop="handleDropOnImage(index)"
              :class="{ dragged: index === draggedItemIndex }"
              draggable="true"
              @click.stop
            />
          </div>
        </TransitionGroup>
      </div>
    </div>

    <div class="image-selection">
      <button @click="clearImages" class="fun-button clear-button">¡Borrar todo!</button>
      <button @click="connectAndSendCommands" class="fun-button send-button">
        ¡Enviar comandos!
      </button>
      <div class="available-images">
        <TransitionGroup name="image-list">
          <div
            v-for="(img, index) in availableImages"
            :key="index"
            class="selectable-image-wrapper"
            :style="randomPosition()"
          >
            <img
              :src="img"
              class="selectable-image"
              @click="selectImage(img)"
              :class="{ selected: isImageSelected(img) }"
            />
          </div>
        </TransitionGroup>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { connectedDevice } from '../composables/store';

// Array para almacenar imágenes seleccionadas
const imagenes = ref([]);
const draggin = ref(false);
const draggedItemIndex = ref(null);
const maxImages = 42; // Máximo número de imágenes permitidas

// Mapear las imágenes a comandos de colores y motores
const colorMap = {
  '/src/assets/celeste.png': 'light_blue',
  '/src/assets/rojo.png': 'red',
  '/src/assets/verde.png': 'green',
  '/src/assets/naranja.png': 'orange',
};

const giros = {
  '/src/assets/izquierda.png': '-1',
  '/src/assets/derecha.png': '1',
};

const convertImagesToCommands = () => {
  return imagenes.value
    .map((img) => {
      if (colorMap[img]) {
        return {
          type: 'color',
          value: colorMap[img],
        };
      } else if (giros[img]) {
        return {
          type: 'motor',
          value: parseInt(giros[img]),
        };
      } else {
        return null; // En caso de que la imagen no coincida con ningún comando conocido
      }
    })
    .filter((command) => command !== null); // Filtra los comandos nulos
};

const connectAndSendCommands = async (event) => {
  event.preventDefault();
  console.log(connectedDevice);

  try {
    if (!connectedDevice.value) {
      console.error('No hay dispositivo conectado.');
      return;
    }

    // Conectar al servicio GATT
    const server = await connectedDevice.value.gatt.connect();

    // Obtener todos los servicios disponibles y mostrarlos
    const services = await server.getPrimaryServices();
    services.forEach((service) => {
      console.log(`Servicio encontrado: ${service.uuid}`);
    });

    const serviceUUID = '00001565-1212-efde-1523-785feabcd123'; // Verifica que sea el UUID correcto

    try {
      const service = await server.getPrimaryService(serviceUUID);
      if (!service) {
        console.error(`No se encontró el servicio con UUID ${serviceUUID}`);
        return;
      }

      // Obtener todas las características del servicio
      const characteristics = await service.getCharacteristics();
      characteristics.forEach((characteristic) => {
        console.log(`Característica encontrada: ${characteristic.uuid}`);
      });

      const characteristicUuid = 'UUID_CORRECTO'; // Asegúrate de que este sea el UUID correcto de la característica
      const characteristic = await service.getCharacteristic(characteristicUuid);

      // Convertir imágenes a comandos y enviar secuencialmente
      const commandsList = convertImagesToCommands();

      for (let i = 0; i < commandsList.length; i++) {
        const command = commandsList[i];

        if (command.type === 'motor') {
          const speed = command.value > 0 ? 33 : -33;
          const motorCommand = new Uint8Array([0x01, 0x01, 0x01, speed]);

          console.log(`Ejecutando comando de motor: ${command.value} giros`);
          await characteristic.writeValue(motorCommand);

          const timePerRotation = 3.5 / Math.abs(command.value);
          await new Promise((resolve) => setTimeout(resolve, timePerRotation * 1000));

          const stopCommand = new Uint8Array([0x01, 0x01, 0x01, 0]);
          await characteristic.writeValue(stopCommand);
        } else if (command.type === 'color') {
          const colorCommand = colors[command.value];
          const colorChangeCommand = new Uint8Array([0x06, 0x04, 0x01, colorCommand]);

          console.log(`Cambiando color a: ${command.value}`);
          await characteristic.writeValue(colorChangeCommand);

          await new Promise((resolve) => setTimeout(resolve, 2000));
        }
      }

      const stopCommand = new Uint8Array([0x01, 0x01, 0x01, 0]);
      await characteristic.writeValue(stopCommand);

      console.log('Todos los comandos se ejecutaron exitosamente.');
    } catch (error) {
      console.error('Error al obtener el servicio o característica:', error);
    }
  } catch (error) {
    console.error('Error al enviar comandos:', error);
  }
};

// Imágenes disponibles para seleccionar
const availableImages = ref([
  '/src/assets/celeste.png',
  '/src/assets/rojo.png',
  '/src/assets/verde.png',
  '/src/assets/naranja.png',
  '/src/assets/izquierda.png',
  '/src/assets/derecha.png',
  // Añadir el "off" a las imágenes disponibles
]);

const selectImage = (img) => {
  if (imagenes.value.length < maxImages) {
    imagenes.value.push(img);
  } else {
    alert('Has alcanzado el máximo de imágenes permitidas.');
  }
};

const isImageSelected = (img) => imagenes.value.includes(img);

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

const handleDragStart = (index, event) => {
  event.dataTransfer.setData('text/plain', index);
  draggedItemIndex.value = index;
};

const handleDragOverImage = (event, index) => {
  event.preventDefault();
};

const handleDropOnImage = (index) => {
  const draggedIndex = draggedItemIndex.value;
  if (draggedIndex !== null && draggedIndex !== index) {
    const draggedItem = imagenes.value.splice(draggedIndex, 1)[0];
    imagenes.value.splice(index, 0, draggedItem);
  }
  draggedItemIndex.value = null;
};

const clearImages = () => {
  imagenes.value = [];
};

const randomRotation = () => {
  const rotation = Math.random() * 20 - 10; // Random rotation between -10 and 10 degrees
  return `transform: rotate(${rotation}deg);`;
};

const randomPosition = () => {
  const x = Math.random() * 40 - 20; // Random X position between -20px and 20px
  const y = Math.random() * 40 - 20; // Random Y position between -20px and 20px
  return `transform: translate(${x}px, ${y}px);`;
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
  min-height: 300px;
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
  flex-direction: column;
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
  width: 80px;
  height: 80px;
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

.clear-button {
  background-color: #ff6b6b;
  color: white;
}

.send-button {
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

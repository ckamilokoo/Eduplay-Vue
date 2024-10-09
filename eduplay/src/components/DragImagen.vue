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
          src="/src/assets/comandos/celeste.png"
          class="selectable-image"
          img="/src/assets/comandos/celeste.png"
          @click="selectImage('/src/assets/comandos/celeste.png')"
        />
        <img
          src="/src/assets/comandos/naranja.png"
          class="selectable-image"
          @click="selectImage('/src/assets/comandos/naranja.png')"
        />
        <img
          src="/src/assets/comandos/rojo.png"
          class="selectable-image"
          @click="selectImage('/src/assets/comandos/rojo.png')"
        />
        <img
          src="/src/assets/comandos/verde.png"
          class="selectable-image"
          @click="selectImage('/src/assets/comandos/verde.png')"
        />
        <img
          src="/src/assets/comandos/izquierda.png"
          class="selectable-image"
          @click="selectImage('/src/assets/comandos/izquierda.png')"
        />
        <img
          src="/src/assets/comandos/derecha.png"
          class="selectable-image"
          @click="selectImage('/src/assets/comandos/derecha.png')"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import { useNivelesStore } from '@/almacenamiento/Niveles.store';
import { useRouter } from 'vue-router';
const nivelStorage = useNivelesStore();
const router = useRouter();

const imagenes = ref([]);
const draggin = ref(false);
const maxImages = 7;
const isOrderCorrect = ref(false);

// Observa cambios en claseActual
watch(isOrderCorrect, (correctorder) => {
  if (correctorder === true) {
    // Redirige después de 10 segundos
    nivelStorage.agregarNivel('Ingeniero');
    setTimeout(() => {
      router.push('/');
    }, 5000);
  }
});

const expectedOrder = [
  '/src/assets/comandos/derecha.png',
  '/src/assets/comandos/derecha.png',
  '/src/assets/comandos/rojo.png',
  '/src/assets/comandos/verde.png',
  '/src/assets/comandos/izquierda.png',
  '/src/assets/comandos/izquierda.png',
];

// Función para verificar si el orden de los comandos es correcto
const checkCommandOrder = (sentCommands) => {
  // Crear un arreglo con los comandos enviados en el mismo orden
  const sentImages = sentCommands;

  // Comparar el orden de comandos enviados con el orden esperado
  const isCorrectOrder = sentImages.every((img, index) => img === expectedOrder[index]);

  if (isCorrectOrder) {
    console.log('Orden correcto de comandos.');
    isOrderCorrect.value = true;
  } else {
    console.log('Orden incorrecto de comandos.');
  }
};

console.log(imagenes);

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

// Función para esperar un tiempo específico
const wait = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

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
          await wait(1000); // Esperar 1 segundo antes de enviar el próximo comando de color
        });
      } else if (motorMap[img]) {
        console.log(`Enviando comando de motor para: ${img}`);
        commands.push(motorMap[img]); // Agregar el comando del motor a la lista
      }
    }

    await executeSequentially(commands);
    // Ejecutar todos los comandos en secuencia
    console.log('Comandos enviados con éxito.');
    checkCommandOrder(imagenes.value);
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
  padding: 10px;
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
  width: 70px;
  height: 70px;
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
  margin-top: 10px;
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
  padding: 7px 12px;
  font-size: 1rem;
  font-family: 'Comic Sans MS', cursive, sans-serif;
  border: none;
  border-radius: 30px;
  cursor: pointer;
  transition: all 0.3s ease;
  margin: 7px;
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

/* Pantallas medianas */
/* Pantallas medianas */
@media (min-width: 641px) and (max-width: 1024px) {
  .title {
    font-size: 2rem; /* Tamaño de fuente medio */
  }

  .uploaded-image {
    width: 70px; /* Tamaño de imagen medio */
    height: 70px;
  }

  .selectable-image {
    width: 60px; /* Tamaño de imagen seleccionable medio */
    height: 60px;
  }

  .fun-button {
    font-size: 0.9rem; /* Tamaño de botón medio */
    width: 100%; /* Asegúrate de que los botones ocupen todo el ancho */
    margin: 10px 0; /* Espaciado vertical entre los botones */
  }

  .image-selection {
    flex-direction: column; /* Cambiar a columna en pantallas medianas */
    align-items: center; /* Alinear los botones a todo el ancho del contenedor */
  }

  .drop-zone {
    background-color: rgba(255, 255, 255, 0.7);
    border: 4px dashed #4ecdc4;
    border-radius: 20px;
    padding: 10px;
    min-height: 100px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    transition: all 0.3s ease;
  }
}
</style>

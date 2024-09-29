<template>
  <div class="flex flex-col items-center">
    <div v-if="claseActual && claseActual.id === 1" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>
      <img
        src="../assets/bosque/imagen_1.jfif"
        alt="Imagen 1"
        class="mb-4"
        height="600px"
        width="400px"
      />
    </div>
    <div
      v-if="claseActual && claseActual.id === 2"
      class="flex flex-row items-center justify-between"
    >
      <img
        src="../assets/bosque/imagen_2.jpg"
        alt="Imagen 1"
        class="mr-4"
        height="700px"
        width="700px"
      />
      <h3 class="text-xl font-bold text-right">
        {{ claseActual.contenido }}
      </h3>
    </div>

    <div
      v-if="claseActual && claseActual.id === 3"
      class="flex flex-row items-center justify-between"
    >
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>
      <img
        src="../assets/bosque/imagen_3.jfif"
        alt="Imagen 1"
        class="mb-4"
        height="500px"
        width="490px"
      />
    </div>
    <div
      v-if="claseActual && claseActual.id === 4"
      class="flex flex-row items-center justify-between"
    >
      <img
        src="../assets/bosque/imagen_4.jpg"
        alt="Imagen 1"
        class="mb-4"
        height="650px"
        width="650px"
      />

      <!-- Contenedor para el texto y los botones -->
      <div class="flex flex-col items-center pr-6">
        <!-- Texto -->
        <h3 class="text-xl font-bold mb-6 text-center">
          {{ claseActual.contenido }}
        </h3>

        <!-- Botones -->
        <div class="flex flex-col items-center space-y-4">
          <button
            class="bg-yellow-400 text-white font-bold py-3 px-6 rounded-lg shadow-lg hover:bg-yellow-500 transition duration-300"
            @click="seleccionarOpcion('A')"
          >
            {{ claseActual.OpcionA }}
          </button>

          <button
            class="bg-green-400 text-white font-bold py-3 px-6 rounded-lg shadow-lg hover:bg-green-500 transition duration-300"
            @click="seleccionarOpcion('B')"
          >
            {{ claseActual.OpcionB }}
          </button>

          <button
            class="bg-blue-400 text-white font-bold py-3 px-6 rounded-lg shadow-lg hover:bg-blue-500 transition duration-300"
            @click="seleccionarOpcion('C')"
          >
            {{ claseActual.OpcionC }}
          </button>
        </div>
      </div>
    </div>

    <div
      v-if="claseActual && claseActual.id === 5"
      class="flex flex-row-reverse items-center justify-between w-full"
    >
      <!-- Imagen a la derecha, ocupa el 40% del espacio -->
      <img
        src="../assets/bosque/imagen_5.jfif"
        alt="Imagen 1"
        class="w-3/6 mb-4"
        height="400px"
        width="300px"
      />

      <!-- Texto a la izquierda, ocupa el 60% del espacio -->
      <h3 class="w-3/6 text-xl font-bold mb-2 text-left">
        {{ claseActual.contenido }}
      </h3>
    </div>

    <div
      v-if="claseActual && claseActual.id === 6"
      class="flex flex-row-reverse items-center justify-between w-full"
    >
      <h3 class="w-3/6 text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>
      <img
        src="../assets/bosque/imagen_6.jfif"
        alt="Imagen 1"
        class="w-3/6 mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div
      v-if="claseActual && claseActual.id === 7"
      class="flex flex-row-reverse items-center justify-between w-full"
    >
      <h3 class="w-3/6 text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>
      <img
        src="../assets/bosque/imagen_7.jpg"
        alt="Imagen 1"
        class="w-3/6 mb-4"
        height="400px"
        width="500px"
      />
    </div>
    <div
      v-if="claseActual && claseActual.id === 8"
      class="flex flex-row items-center justify-between"
    >
      <img
        src="../assets/bosque/imagen_4.jpg"
        alt="Imagen 1"
        class="mb-4"
        height="650px"
        width="650px"
      />

      <!-- Contenedor para el texto y los botones -->
      <div class="flex flex-col items-center pr-6">
        <!-- Texto -->
        <h3 class="text-xl font-bold mb-6 text-center">
          {{ claseActual.contenido }}
        </h3>

        <!-- Botones -->
        <div class="flex flex-col items-center space-y-4">
          <button
            class="bg-yellow-400 text-white font-bold py-3 px-6 rounded-lg shadow-lg hover:bg-yellow-500 transition duration-300"
            @click="seleccionarOpcion('A')"
          >
            {{ claseActual.OpcionA }}
          </button>

          <button
            class="bg-green-400 text-white font-bold py-3 px-6 rounded-lg shadow-lg hover:bg-green-500 transition duration-300"
            @click="seleccionarOpcion('B')"
          >
            {{ claseActual.OpcionB }}
          </button>

          <button
            class="bg-blue-400 text-white font-bold py-3 px-6 rounded-lg shadow-lg hover:bg-blue-500 transition duration-300"
            @click="seleccionarOpcion('C')"
          >
            {{ claseActual.OpcionC }}
          </button>
        </div>
      </div>
    </div>
    <div
      v-if="claseActual && claseActual.id === 9"
      class="flex flex-row-reverse items-center justify-between w-full"
    >
      <h3 class="w-3/6 text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>
      <img
        src="../assets/bosque/imagen_9.jpeg"
        alt="Imagen 1"
        class="w-3/6 mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div
      v-if="claseActual && claseActual.id === 10"
      class="flex flex-row-reverse items-center justify-between w-full"
    >
      <img
        src="../assets/bosque/imagen_10.jpeg"
        alt="Imagen 1"
        class="w-3/6 mb-4"
        height="400px"
        width="400px"
      />
      <h3 class="w-3/6 text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>
    </div>
    <div v-if="claseActual && claseActual.id === 11" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>
      <img
        src="../assets/bosque/imagen_11.jfif"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 12" class="flex flex-col items-center">
      <img
        src="../assets/bosque/imagen_8.jpg"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
      <h3 class="text-xl font-bold mb-2 text-center pr-6">
        {{ claseActual.contenido }}
      </h3>
      <div class="flex flex-col items-center space-y-4">
        <button
          class="bg-yellow-400 text-white font-bold py-3 px-6 rounded-lg shadow-lg hover:bg-yellow-500 transition duration-300"
          @click="seleccionarOpcion('A')"
        >
          {{ claseActual.OpcionA }}
        </button>

        <button
          class="bg-green-400 text-white font-bold py-3 px-6 rounded-lg shadow-lg hover:bg-green-500 transition duration-300"
          @click="seleccionarOpcion('B')"
        >
          {{ claseActual.OpcionB }}
        </button>

        <button
          class="bg-blue-400 text-white font-bold py-3 px-6 rounded-lg shadow-lg hover:bg-blue-500 transition duration-300"
          @click="seleccionarOpcion('C')"
        >
          {{ claseActual.OpcionC }}
        </button>
      </div>
    </div>
    <div v-if="claseActual && claseActual.id === 13" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>
      <img
        src="../assets/bosque/imagen_13.jfif"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 14" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>
      <img
        src="../assets/bosque/imagen_14.jfif"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="325px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 15" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>
      <img
        src="../assets/bosque/imagen_15.jfif"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="350px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 16" class="flex flex-col items-center">
      <img
        src="../assets/bosque/imagen_8.jpg"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
      <h3 class="text-xl font-bold mb-2 text-center pr-6">
        {{ claseActual.contenido }}
      </h3>
      <div class="flex flex-col items-center space-y-4">
        <button
          class="bg-yellow-400 text-white font-bold py-3 px-6 rounded-lg shadow-lg hover:bg-yellow-500 transition duration-300"
          @click="seleccionarOpcion('A')"
        >
          {{ claseActual.OpcionA }}
        </button>

        <button
          class="bg-green-400 text-white font-bold py-3 px-6 rounded-lg shadow-lg hover:bg-green-500 transition duration-300"
          @click="seleccionarOpcion('B')"
        >
          {{ claseActual.OpcionB }}
        </button>

        <button
          class="bg-blue-400 text-white font-bold py-3 px-6 rounded-lg shadow-lg hover:bg-blue-500 transition duration-300"
          @click="seleccionarOpcion('C')"
        >
          {{ claseActual.OpcionC }}
        </button>
      </div>
    </div>
    <div v-if="claseActual && claseActual.id === 17" class="flex flex-col items-center">
      <RouterLink to="/" class="flex flex-col items-center">
        <img
          src="../assets/iconos_inicio/icosaedro.png"
          alt="Esfera"
          class="mb-4"
          height="200px"
          width="200px"
        />
        <h3 class="text-xl font-bold mb-2 text-center">Volver al Menu Principal</h3>
      </RouterLink>
    </div>
  </div>
  <div class="flex justify-between items-center space-x-4 mt-4">
    <button
      @click="decrementarClase"
      :hidden="claseActualId === 1"
      class="bg-pink-400 text-white font-bold py-3 px-4 rounded-full shadow-lg hover:bg-pink-500 transition duration-300 transform hover:scale-90"
    >
      Anterior
    </button>

    <button
      @click="incrementarClase"
      :disabled="
        (claseActualId === 4 && !respuestaCorrecta) ||
        (claseActualId === 8 && !respuestaCorrecta) ||
        (claseActualId === 12 && !respuestaCorrecta) ||
        (claseActualId === 16 && !respuestaCorrecta)
      "
      class="bg-purple-400 text-white font-bold py-3 px-4 rounded-full shadow-lg hover:bg-purple-500 transition duration-300 transform hover:scale-90"
    >
      Siguiente
    </button>
  </div>
</template>

<script lang="ts" setup>
const clases = [
  {
    id: 1,
    contenido:
      'Habia una vez un hermoso lugar llamado "El bosque Encantado" , donde los arboles eran altos y majestuosos , los animales jugaban entre las hojas y todo parecia sacado deun cuento de hadas',
  },
  {
    id: 2,
    contenido:
      'Pero un dia , algo extraño comenzo a suceder. Columnas de humo oscuros comenzaron a elevarse en el cielo , dejando una sombra de tristeza por todo el bosque. Los animales estaban preocupados  asustados. todos se preguntaban que estaba causando tdo ese humo y fuego que estaba poniendo feo su entorno.',
  },
  {
    id: 3,
    contenido:
      'Nuestros valientes amigos , Susy y Freddy , una pareja de conejos, decidieron intentar descubrir el misterio pero necesitaran de tu ayuda, !Vamos a ayudarlos!',
  },
  {
    id: 4,
    contenido: '¿ Como se llama lo que esta sucediendo en el BOSQUE ENCANTADO ?',
    OpcionA: 'Terremoto',
    OpcionB: 'Incendio Forestal',
    OpcionC: 'Tsunami',
  },
  {
    id: 5,
    contenido:
      'Susy y Freddy se enbarcaron en una emocionante aventura, explorando los rincones del Bosque Encantado en busca de pistas',
  },
  {
    id: 6,
    contenido:
      'En su camino, encontraron a Don Mauro, un búho sabio de la comunidad de animales, y le pidieron ayuda.',
  },
  {
    id: 7,
    contenido:
      'Don Mauro les conto que los incendios eran causados por descuidos y que tenian consecuencias muy graves para el bosque.',
  },
  {
    id: 8,
    contenido: '¿ A quien responsabilizo Don Mauro de que ocurran incendios forestales ?',
    OpcionA: 'A los animales',
    OpcionB: 'A los insectos',
    OpcionC: 'A los humanos',
  },
  {
    id: 9,
    contenido:
      'Sentados en un circulo, con los ojos brillantes y las orejas atentas, Don Mauro comenzo a contarles la historia de los incendios forestales y sus consecuencias',
  },
  {
    id: 10,
    contenido:
      'Un incendio forestal es como un mostruo de fuego que se propaga rapidamente por el bosque. Quema los arboles, las plantas y los hogares de los animales. Ademas, el humo negro que sale de los incendios es malo para todos, desde los pajaros hasta nosotros. El bosque pierde su belleza y los animales pierden sus hogares. Es muy triste.',
  },
  {
    id: 11,
    contenido:
      'Susy y Freddy se miraron, asintiendo con tristeza. Querian hacer algo para proteger su hogaar. La conversacion entre los tres continuo y la pareja de conejos le dijo al Don Mauro que tenian una idea para proteger el bosque encantado.',
  },
  {
    id: 12,
    contenido: '¿ Cual crees que es la idea que Susy y Freddy le dijeron a Don Mauro ?',
    OpcionA: 'Dejar el bosque encantado e irse a la nieve',
    OpcionB: 'Una campaña de prevencion',
    OpcionC: 'Hacer un incendio forestal',
  },
  {
    id: 13,
    contenido:
      'Don Mauro les explico como podian ayudar a prevenir los incendios forestales y les dijo, "ustedes son unos heroes y pueden enseñar a todos sobre la importancia de ser cuidadosos en el bosque."',
  },
  {
    id: 14,
    contenido:
      'Despues de escuchar las palabras de Don Mauro, Susy y Freddy escribieron pancartas muy lindas, con muchos colores y dibujos que decian "no dejen basura que pueda causar fuego, no jueguencon cerillas o encendedores y avisen si ven humo o fuego. Ademas, plantar arboles y cuidar las plantas ayuda a mantener el bosque sano y menos propenso a incendios" , y las repartieron a todos los habitantes del bosque encantado.',
  },
  {
    id: 15,
    contenido:
      'Cuando terminaron de repartir las pancartas a todos los animales en un momento pensaron "hemos terminado" pero unos segundos despues se preguntaron, ¿ Que vamos a hacer si por descuido de un animal que esta de visita o un humano comienza un incendio forestal ? . Pensaron un momento y se les ocurrio una idea.',
  },
  {
    id: 16,
    contenido: '¿ Cual crees que es la nueva idea que tienen Susy y Freddy ?',
    OpcionA: 'Que ustedes los ayuden a construir un helicoptero de rescate',
    OpcionB: 'Hacer cuidades en los bosques para que no hallan incendios forestales',
    OpcionC: 'Quemar todos los bosques antes que se puedan incendiar',
  },
  {
    id: 17,
    contenido: '/',
  },
];

import { ref, computed } from 'vue';

const clasesArray = ref(clases);
const claseActualId = ref(1);

const claseActual = computed(() => {
  return clasesArray.value.find((clase) => clase.id === claseActualId.value);
});

const incrementarClase = () => {
  if (claseActualId.value < 17) {
    respuestaCorrecta.value = false;
    claseActualId.value += 1;
  }
};

const decrementarClase = () => {
  if (claseActualId.value > 1) {
    claseActualId.value -= 1;
  }
};

const respuestaCorrecta = ref(false);

// Función para seleccionar opción
const seleccionarOpcion = (opcion: string) => {
  switch (claseActualId.value) {
    case 4:
      respuestaCorrecta.value = opcion === 'B';
      break;
    case 8:
      respuestaCorrecta.value = opcion === 'C';
      break;
    case 12:
      respuestaCorrecta.value = opcion === 'B';
      break;
    case 16:
      respuestaCorrecta.value = opcion === 'A';
      break;
    default:
      respuestaCorrecta.value = false; // Opcional: Por si hay una clase no definida
  }
};
</script>

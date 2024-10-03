<template>
  <div class="flex flex-col items-center">
    <div
      v-if="claseActual && claseActual.id === 1"
      class="flex flex-row items-center justify-center space-x-4"
    >
      <!-- Texto a la izquierda -->
      <h3 class="w-auto sm:w-1/2 md:w-2/4 lg:w-3/6 text-xl font-bold mb-2 text-left">
        {{ claseActual.contenido }}
      </h3>

      <!-- Imagen a la derecha -->
      <img
        src="../assets/bosque/imagen_1.jfif"
        alt="Imagen 1"
        class="w-full sm:w-1/2 md:w-2/4 lg:w-2/6"
      />
    </div>

    <div
      v-if="claseActual && claseActual.id === 2"
      class="flex flex-row items-center justify-between"
    >
      <img
        src="../assets/bosque/imagen_2.jpg"
        alt="Imagen 1"
        class="w-full sm:w-1/2 md:w-2/4 lg:w-2/6"
        height="700px"
        width="700px"
      />
      <h3 class="w-auto sm:w-1/2 md:w-2/4 lg:w-3/6 text-xl font-bold mb-2 text-right">
        {{ claseActual.contenido }}
      </h3>
    </div>

    <div
      v-if="claseActual && claseActual.id === 3"
      class="flex flex-row items-center justify-between"
    >
      <h3 class="w-auto sm:w-1/2 md:w-2/4 lg:w-3/6 text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>
      <img
        src="../assets/bosque/imagen_3.jfif"
        alt="Imagen 1"
        class="mb-4 w-full sm:w-1/2 md:w-2/4 lg:w-2/6"
        height="500px"
        width="490px"
      />
    </div>
    <div
      v-if="claseActual && claseActual.id === 4"
      class="flex flex-row items-start justify-between h-full"
    >
      <!-- Contenedor izquierdo con imagen y texto -->
      <div class="flex flex-col items-start justify-between h-full sm:w-1/2 md:w-2/4 lg:w-2/6">
        <img
          src="../assets/bosque/imagen_4.jpg"
          alt="Imagen 1"
          class="mb-4 w-full"
          height="650px"
          width="650px"
        />

        <h3 class="w-full text-xl font-bold mb-2 text-center">
          {{ claseActual.contenido }}
        </h3>
      </div>

      <!-- Contenedor derecho para los botones -->
      <div class="flex flex-col items-center justify-center pr-6">
        <div class="flex flex-col space-y-4">
          <button
            :class="[
              'bg-blue-400 text-white font-bold py-3 px-6 rounded-lg shadow-lg transition duration-300',
              opcionSeleccionada === 'A'
                ? respuestaCorrecta
                  ? 'bg-green-500'
                  : 'bg-red-500'
                : 'hover:bg-red-500',
            ]"
            @click="seleccionarOpcion('A')"
          >
            {{ claseActual.OpcionA }}
          </button>

          <button
            :class="[
              'bg-blue-400 text-white font-bold py-3 px-6 rounded-lg shadow-lg transition duration-300',
              opcionSeleccionada === 'B'
                ? respuestaCorrecta
                  ? 'bg-green-500'
                  : 'bg-red-500'
                : 'hover:bg-green-500',
            ]"
            @click="seleccionarOpcion('B')"
          >
            {{ claseActual.OpcionB }}
          </button>

          <button
            :class="[
              'bg-blue-400 text-white font-bold py-3 px-6 rounded-lg shadow-lg transition duration-300',
              opcionSeleccionada === 'C'
                ? respuestaCorrecta
                  ? 'bg-green-500'
                  : 'bg-red-500'
                : 'hover:bg-red-500',
            ]"
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
          :class="[
            'bg-blue-400 text-white font-bold py-3 px-6 rounded-lg shadow-lg transition duration-300',
            opcionSeleccionada === 'A'
              ? respuestaCorrecta
                ? 'bg-green-500'
                : 'bg-red-500'
              : 'hover:bg-red-500',
          ]"
          @click="seleccionarOpcion('A')"
        >
          {{ claseActual.OpcionA }}
        </button>

        <button
          :class="[
            'bg-blue-400 text-white font-bold py-3 px-6 rounded-lg shadow-lg transition duration-300',
            opcionSeleccionada === 'B'
              ? respuestaCorrecta
                ? 'bg-green-500'
                : 'bg-red-500'
              : 'hover:bg-green-500',
          ]"
          @click="seleccionarOpcion('B')"
        >
          {{ claseActual.OpcionB }}
        </button>

        <button
          :class="[
            'bg-blue-400 text-white font-bold py-3 px-6 rounded-lg shadow-lg transition duration-300',
            opcionSeleccionada === 'C'
              ? respuestaCorrecta
                ? 'bg-green-500'
                : 'bg-red-500'
              : 'hover:bg-red-500',
          ]"
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

    <!-- Botones debajo del texto e imagen -->
    <div class="flex justify-between items-center space-x-4 mt-4 w-1/2">
      <button
        @click="decrementarClase"
        :hidden="claseActualId === 1"
        class="bg-pink-400 text-white font-bold py-1 px-2 rounded-full shadow-lg hover:bg-pink-500 transition duration-300 transform hover:scale-90"
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
        class="bg-purple-400 text-white font-bold py-1 px-2 rounded-full shadow-lg hover:bg-purple-500 transition duration-300 transform hover:scale-90"
      >
        Siguiente
      </button>
    </div>
  </div>
</template>

<script lang="ts" setup>
const clases = [
  {
    id: 1,
    contenido:
      'Había una vez un hermoso lugar llamado "El Bosque Encantado", donde los árboles eran altos y majestuosos, los animales jugaban entre las hojas y todo parecía sacado de un cuento de hadas.',
  },
  {
    id: 2,
    contenido:
      'Pero un día, algo extraño comenzó a suceder. Columnas de humo oscuros comenzaron a elevarse en el cielo, dejando una sombra de tristeza por todo el bosque. Los animales estaban preocupados y asustados. Todos se preguntaban qué estaba causando todo ese humo y fuego que estaba poniendo feo su entorno.',
  },
  {
    id: 3,
    contenido:
      'Nuestros valientes amigos, Susy y Freddy, una pareja de conejos, decidieron intentar descubrir el misterio, pero necesitarán de tu ayuda. ¡Vamos a ayudarlos!',
  },
  {
    id: 4,
    contenido: '¿Cómo se llama lo que está sucediendo en el Bosque Encantado?',
    OpcionA: 'Terremoto',
    OpcionB: 'Incendio Forestal',
    OpcionC: 'Tsunami',
  },
  {
    id: 5,
    contenido:
      'Susy y Freddy se embarcaron en una emocionante aventura, explorando los rincones del Bosque Encantado en busca de pistas.',
  },
  {
    id: 6,
    contenido:
      'En su camino, encontraron a Don Mauro, un búho sabio de la comunidad de animales, y le pidieron ayuda.',
  },
  {
    id: 7,
    contenido:
      'Don Mauro les contó que los incendios eran causados por descuidos y que tenían consecuencias muy graves para el bosque.',
  },
  {
    id: 8,
    contenido: '¿A quién responsabilizó Don Mauro de que ocurran incendios forestales?',
    OpcionA: 'A los animales',
    OpcionB: 'A los insectos',
    OpcionC: 'A los humanos',
  },
  {
    id: 9,
    contenido:
      'Sentados en un círculo, con los ojos brillantes y las orejas atentas, Don Mauro comenzó a contarles la historia de los incendios forestales y sus consecuencias.',
  },
  {
    id: 10,
    contenido:
      'Un incendio forestal es como un monstruo de fuego que se propaga rápidamente por el bosque. Quema los árboles, las plantas y los hogares de los animales. Además, el humo negro que sale de los incendios es malo para todos, desde los pájaros hasta nosotros. El bosque pierde su belleza y los animales pierden sus hogares. Es muy triste.',
  },
  {
    id: 11,
    contenido:
      'Susy y Freddy se miraron, asintiendo con tristeza. Querían hacer algo para proteger su hogar. La conversación entre los tres continuó y la pareja de conejos le dijo a Don Mauro que tenían una idea para proteger el Bosque Encantado.',
  },
  {
    id: 12,
    contenido: '¿Cuál crees que es la idea que Susy y Freddy le dijeron a Don Mauro?',
    OpcionA: 'Dejar el Bosque Encantado e irse a la nieve',
    OpcionB: 'Una campaña de prevención',
    OpcionC: 'Hacer un incendio forestal',
  },
  {
    id: 13,
    contenido:
      'Don Mauro les explicó cómo podían ayudar a prevenir los incendios forestales y les dijo: "Ustedes son unos héroes y pueden enseñar a todos sobre la importancia de ser cuidadosos en el bosque."',
  },
  {
    id: 14,
    contenido:
      'Después de escuchar las palabras de Don Mauro, Susy y Freddy escribieron pancartas muy lindas, con muchos colores y dibujos que decían "no dejen basura que pueda causar fuego, no jueguen con cerillas o encendedores y avisen si ven humo o fuego. Además, plantar árboles y cuidar las plantas ayuda a mantener el bosque sano y menos propenso a incendios", y las repartieron a todos los habitantes del Bosque Encantado.',
  },
  {
    id: 15,
    contenido:
      'Cuando terminaron de repartir las pancartas a todos los animales, en un momento pensaron "hemos terminado", pero unos segundos después se preguntaron: ¿Qué vamos a hacer si por descuido de un animal que está de visita o un humano comienza un incendio forestal? Pensaron un momento y se les ocurrió una idea.',
  },
  {
    id: 16,
    contenido: '¿Cuál crees que es la nueva idea que tienen Susy y Freddy?',
    OpcionA: 'Que ustedes los ayuden a construir un helicóptero de rescate',
    OpcionB: 'Hacer ciudades en los bosques para que no hayan incendios forestales',
    OpcionC: 'Quemar todos los bosques antes de que se puedan incendiar',
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

const opcionSeleccionada = ref<string | null>(null);

// Función para seleccionar opción
const seleccionarOpcion = (opcion: string) => {
  opcionSeleccionada.value = opcion;

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

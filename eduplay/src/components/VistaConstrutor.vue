<template>
  <div class="flex flex-col items-center">
    <div v-if="claseActual && claseActual.id === 1" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>
      <div class="flex flex-row">
        <img
          src="../assets/bosque/helicoptero1.png"
          alt="Imagen 1"
          class="mb-4 sm:w-1/2 md:w-2/4 lg:w-2/6"
          height="400px"
          width="400px"
        />
        <img
          src="../assets/bosque/sabias.png"
          alt="Imagen 1"
          class="mb-4 sm:w-1/2 md:w-2/4 lg:w-2/6"
          height="400px"
          width="400px"
        />
      </div>
    </div>
    <div v-if="claseActual && claseActual.id === 2" class="flex flex-col items-center">
      <video width="700" controls autoplay muted class="mt-1">
        <source src="../assets/video/eduplayvideo.mp4" type="video/mp4" />
        Tu navegador no soporta la reproducción de videos.
      </video>
    </div>
    <div v-if="claseActual && claseActual.id > 2" class="flex flex-col items-start">
      <h1 class="text-2xl font-extrabold text-center text-white mb-1">
        Observa la imagen y utiliza las piezas indicadas
      </h1>
    </div>
    <div v-if="claseActual && claseActual.id > 2" class="flex flex-col items-start w-full">
      <h3 class="font-extrabold text-4xl text-black w-full ml-0">
        {{ claseActual?.id - 2 }}
      </h3>
    </div>

    <div v-if="claseActual && claseActual.id === 3" class="flex flex-col items-center">
      <img
        src="../assets/helicoptero/1.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="510px"
      />
    </div>

    <div v-if="claseActual && claseActual.id === 4" class="flex flex-col items-center">
      <img
        src="../assets/helicoptero/2.png"
        alt="Imagen 1"
        class="mb-4"
        height="570px"
        width="460px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 5" class="flex flex-col items-center">
      <img
        src="../assets/helicoptero/3.png"
        alt="Imagen 1"
        class="mb-4"
        height="500px"
        width="570px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 6" class="flex flex-col items-center">
      <img
        src="../assets/helicoptero/4.png"
        alt="Imagen 1"
        class="mb-4"
        height="500px"
        width="580px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 7" class="flex flex-col items-center">
      <img
        src="../assets/helicoptero/5.png"
        alt="Imagen 1"
        class="mb-4"
        height="500px"
        width="600px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 8" class="flex flex-col items-center">
      <img
        src="../assets/helicoptero/6.png"
        alt="Imagen 1"
        class="mb-4"
        height="500px"
        width="580px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 9" class="flex flex-col items-center">
      <img
        src="../assets/helicoptero/7.png"
        alt="Imagen 1"
        class="mb-4"
        height="500px"
        width="620px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 10" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/8.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="670px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 11" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/9.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="680px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 12" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/10.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="680px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 13" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/11.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="520px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 14" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/12.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="560px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 15" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/13.png"
        alt="Imagen 1"
        class="mb-4"
        height="490px"
        width="500px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 16" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/14.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="640px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 17" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/15.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="570px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 18" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/16.png"
        alt="Imagen 1"
        class="mb-4"
        height="430px"
        width="570px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 19" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/17.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 20" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/18.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 21" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/19.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 22" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/20.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 23" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/21.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 24" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/22.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 25" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/23.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 26" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/24.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 27" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/25.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 28" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/26.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 29" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/27.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 30" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/28.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 31" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/29.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 32" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/30.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 33" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/31.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 34" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/32.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 35" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/33.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 36" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/34.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 37" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/35.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 38" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/36.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 39" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/37.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 40" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/38.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 41" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/39.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 42" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/40.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 43" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/41.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 44" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/42.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 45" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/43.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 46" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/44.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 47" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/45.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 48" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/46.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 49" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/47.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 50" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/48.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 51" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/49.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 52" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/50.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 53" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/51.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 54" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/52.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 55" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/53.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 56" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/54.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>
    <div v-if="claseActual && claseActual.id === 57" class="flex flex-col items-center">
      <h3 class="text-xl font-bold mb-2 text-center">
        {{ claseActual.contenido }}
      </h3>

      <img
        src="../assets/helicoptero/55.png"
        alt="Imagen 1"
        class="mb-4"
        height="400px"
        width="400px"
      />
    </div>

    <div v-if="claseActual && claseActual.id === 58" class="flex flex-col items-center">
      <RouterLink to="/vista-ingeniero" class="flex flex-col items-center">
        <img
          src="../assets/iconos_inicio/icosaedro.png"
          alt="Esfera"
          class="mb-4"
          height="200px"
          width="200px"
        />
        <h3 class="text-xl font-bold mb-2 text-center">Nivel completado</h3>
      </RouterLink>
    </div>

    <div class="flex justify-between items-center space-x-4 mt-4">
      <button
        @click="decrementarClase"
        :hidden="claseActualId === 1"
        class="bg-pink-400 text-white font-bold py-1 px-2 rounded-full shadow-lg hover:bg-pink-500 transition duration-300 transform hover:scale-90"
      >
        Anterior
      </button>

      <button
        @click="incrementarClase"
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
      'Es normal preguntarse , Como puede un helicoptero puede volar sino tienes alas , El helicoptero vuela con una gran helice que gira muy rapido lo que permite al helicoptero elevarse por el aire y desplazarse . Una pequeña helice en la parte trasera le da equilibrio. Incluso dar marcha atras o girar sobre si mismo ',
  },
  {
    id: 2,
  },
  {
    id: 3,
  },
  {
    id: 4,
  },
  {
    id: 5,
  },
  {
    id: 6,
  },
  {
    id: 7,
  },
  {
    id: 8,
  },
  {
    id: 9,
  },
  {
    id: 10,
  },
  {
    id: 11,
  },
  {
    id: 12,
  },
  {
    id: 13,
  },
  {
    id: 14,
  },
  {
    id: 15,
  },
  {
    id: 16,
  },
  {
    id: 17,
  },
  {
    id: 18,
  },
  {
    id: 19,
  },
  {
    id: 20,
  },
  {
    id: 21,
  },
  {
    id: 22,
  },
  {
    id: 23,
  },
  {
    id: 24,
  },
  {
    id: 25,
  },
  {
    id: 26,
  },
  {
    id: 27,
  },
  {
    id: 28,
  },
  {
    id: 29,
  },
  {
    id: 30,
  },
  {
    id: 31,
  },
  {
    id: 32,
  },
  {
    id: 33,
  },
  {
    id: 34,
  },
  {
    id: 35,
  },
  {
    id: 36,
  },
  {
    id: 37,
  },
  {
    id: 38,
  },
  {
    id: 39,
  },
  {
    id: 40,
  },
  {
    id: 41,
  },
  {
    id: 42,
  },
  {
    id: 43,
  },
  {
    id: 44,
  },
  {
    id: 45,
  },
  {
    id: 46,
  },
  {
    id: 47,
  },
  {
    id: 48,
  },
  {
    id: 49,
  },
  {
    id: 50,
  },
  {
    id: 51,
  },
  {
    id: 52,
  },
  {
    id: 53,
  },
  {
    id: 54,
  },
  {
    id: 55,
  },
  {
    id: 56,
  },
  {
    id: 57,
  },
  {
    id: 58,
  },
];

import { ref, computed, watch } from 'vue';
import { useNivelesStore } from '@/almacenamiento/Niveles.store';
import { useRouter } from 'vue-router';

const nivelStorage = useNivelesStore();
const router = useRouter();
const clasesArray = ref(clases);
const claseActualId = ref(1);

const claseActual = computed(() => {
  return clasesArray.value.find((clase) => clase.id === claseActualId.value);
});

// Observa cambios en claseActual
watch(claseActual, (newClase) => {
  if (newClase && newClase.id === 58) {
    // Redirige después de 10 segundos
    nivelStorage.agregarNivel('Constructor');
    setTimeout(() => {
      router.push('/');
    }, 5000);
  }
});

const incrementarClase = () => {
  if (claseActualId.value < 58) {
    claseActualId.value += 1;
  }
};

const decrementarClase = () => {
  if (claseActualId.value > 1) {
    claseActualId.value -= 1;
  }
};
</script>

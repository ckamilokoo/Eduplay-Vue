<template>
  <div class="flex flex-col items-center justify-center space-y-6">
    <div v-if="PrimeraImagen" class="mt-6" :hidden="currentIndex === 2">
      <img
        src="../assets/bosque/helicoptero1.png"
        alt="Esfera"
        class="mb-4"
        height="150px"
        width="150px"
      />
      <img
        src="../assets/bosque/sabias.png"
        alt="Esfera"
        class="mb-4"
        height="150px"
        width="150px"
      />
    </div>
    <!-- Alinea el contenido en columna -->
    <h1 class="text-4xl font-extrabold text-center text-white mb-10">
      Observa la imagen y utiliza las piezas indicadas
    </h1>
    <!-- Texto centrado -->
    <div class="carousel-container" :hidden="currentIndex === 0">
      <button class="nav-button prev" @click="prevImage" :hidden="currentIndex === 0">Prev</button>
      <div class="carousel">
        <div class="carousel-item" v-if="currentIndex > 0">
          <img :src="images[prevIndex]" alt="Previous Image" class="carousel-img" />
        </div>
        <div class="carousel-item">
          <img :src="images[currentIndex]" alt="Current Image" class="carousel-img current" />
        </div>
        <div class="carousel-item" v-if="currentIndex < images.length - 1">
          <img :src="images[nextIndex]" alt="Next Image" class="carousel-img" />
        </div>
      </div>
      <button class="nav-button next" @click="nextImage" :hidden="isLastImage">Next</button>
    </div>
    <!-- Nuevo elemento para "Volver al Menú Principal" -->
    <div v-if="isLastImage" class="mt-6">
      <RouterLink to="/" class="flex flex-col items-center">
        <img
          src="../assets/iconos_inicio/icosaedro.png"
          alt="Esfera"
          class="mb-4"
          height="150px"
          width="150px"
        />
        <h3 class="text-xl font-bold mb-2 text-center">Volver al Menú Principal</h3>
      </RouterLink>
    </div>
  </div>
</template>
<script lang="ts" setup>
import { ref, computed } from 'vue';

// Import images
import helicoptero from '@/assets/bosque/helicoptero1.png';
import sabias from '@/assets/bosque/sabias.png';
import img1 from '../assets/helicoptero/1.png';
import img2 from '../assets/helicoptero/2.png';
import img3 from '../assets/helicoptero/3.png';
import img4 from '../assets/helicoptero/4.png';
import img5 from '../assets/helicoptero/5.png';
import img6 from '../assets/helicoptero/6.png';
import img7 from '../assets/helicoptero/7.png';
import img8 from '../assets/helicoptero/8.png';
import img9 from '../assets/helicoptero/9.png';
import img10 from '../assets/helicoptero/10.png';
import img11 from '../assets/helicoptero/11.png';
import img12 from '../assets/helicoptero/12.png';
import img13 from '../assets/helicoptero/13.png';
import img14 from '../assets/helicoptero/14.png';
import img15 from '../assets/helicoptero/15.png';
import img16 from '../assets/helicoptero/16.png';
import img17 from '../assets/helicoptero/17.png';
import img18 from '../assets/helicoptero/18.png';
import img19 from '../assets/helicoptero/19.png';
import img20 from '../assets/helicoptero/20.png';
import img21 from '../assets/helicoptero/21.png';
import img22 from '../assets/helicoptero/22.png';
import img23 from '../assets/helicoptero/23.png';
import img24 from '../assets/helicoptero/24.png';
import img25 from '../assets/helicoptero/25.png';
import img26 from '../assets/helicoptero/26.png';
import img27 from '../assets/helicoptero/27.png';
import img28 from '../assets/helicoptero/28.png';
import img29 from '../assets/helicoptero/29.png';
import img30 from '../assets/helicoptero/30.png';
import img31 from '../assets/helicoptero/31.png';
import img32 from '../assets/helicoptero/32.png';
import img33 from '../assets/helicoptero/33.png';
import img34 from '../assets/helicoptero/34.png';
import img35 from '../assets/helicoptero/35.png';
import img36 from '../assets/helicoptero/36.png';
import img37 from '../assets/helicoptero/37.png';
import img38 from '../assets/helicoptero/38.png';
import img39 from '../assets/helicoptero/39.png';
import img40 from '../assets/helicoptero/40.png';
import img41 from '../assets/helicoptero/41.png';
import img42 from '../assets/helicoptero/42.png';
import img43 from '../assets/helicoptero/43.png';
import img44 from '../assets/helicoptero/44.png';
import img45 from '../assets/helicoptero/45.png';
import img46 from '../assets/helicoptero/46.png';
import img47 from '../assets/helicoptero/47.png';
import img48 from '../assets/helicoptero/48.png';
import img49 from '../assets/helicoptero/49.png';
import img50 from '../assets/helicoptero/50.png';
import img51 from '../assets/helicoptero/51.png';
import img52 from '../assets/helicoptero/52.png';
import img53 from '../assets/helicoptero/53.png';
import img54 from '../assets/helicoptero/54.png';
import img55 from '../assets/helicoptero/55.png';

const images = [
  img1,
  img2,
  img3,
  img4,
  img5,
  img6,
  img7,
  img8,
  img9,
  img10,
  img11,
  img12,
  img13,
  img14,
  img15,
  img16,
  img17,
  img18,
  img19,
  img20,
  img21,
  img22,
  img23,
  img24,
  img25,
  img26,
  img27,
  img28,
  img29,
  img30,
  img31,
  img32,
  img33,
  img34,
  img35,
  img36,
  img37,
  img38,
  img39,
  img40,
  img41,
  img42,
  img43,
  img44,
  img45,
  img46,
  img47,
  img48,
  img49,
  img50,
  img51,
  img52,
  img53,
  img54,
  img55,
];

const currentIndex = ref(0);

const prevIndex = computed(() => (currentIndex.value - 1 + images.length) % images.length);
const nextIndex = computed(() => (currentIndex.value + 1) % images.length);

const prevImage = () => {
  currentIndex.value = (currentIndex.value - 1 + images.length) % images.length;
};

const nextImage = () => {
  currentIndex.value = (currentIndex.value + 1) % images.length;
};

// Computado para verificar si estamos en la última imagen
const isLastImage = computed(() => currentIndex.value === images.length - 1);
const PrimeraImagen = computed(() => currentIndex.value === 0);
</script>
<style scoped>
.text-container {
  margin-bottom: 20px; /* Da un margen inferior para separar el texto del carousel */
}

.carousel-container {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  width: 100%;
  margin: auto;
  overflow: hidden;
  border-radius: 10px;

  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.carousel {
  display: flex;
  align-items: center;
  transition: transform 0.5s ease-in-out;
  width: 100%;
}

.carousel-item {
  flex: 0 0 33.33%;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: opacity 0.5s ease-in-out;
}

.carousel-img {
  width: 100%;
  height: auto;
  border-radius: 10px;
}

.carousel-img.current {
  border: 5px solid #ffcc00;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.3);
}

.nav-button {
  background-color: #ff6347;
  border: none;
  color: white;
  padding: 10px;
  font-size: 18px;
  cursor: pointer;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  border-radius: 5px;
}

.nav-button.prev {
  left: 10px;
}

.nav-button.next {
  right: 10px;
}

.nav-button:hover {
  background-color: #ff4500;
}
</style>

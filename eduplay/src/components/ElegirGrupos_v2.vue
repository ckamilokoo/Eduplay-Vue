<template>
  <div id="grid-container" class="grid">
    <RouterLink
      to="/video-historia"
      class="flex flex-col items-center"
      id="link-empecemos"
      :class="getImageClass(0)"
    >
      <img
        src="../assets/iconos_inicio/cilindro.png"
        alt="Cilindro"
        id="img-empecemos"
        class="object-contain"
      />
      <h3 id="title-empecemos" class="animate-bounce">Empecemos</h3>
    </RouterLink>

    <RouterLink
      to="/vista-Construtor"
      class="flex flex-col items-center"
      id="link-construyamos"
      :class="getImageClass(1)"
    >
      <img
        src="../assets/iconos_inicio/esfera.png"
        alt="Esfera"
        id="img-construyamos"
        class="object-contain"
      />
      <h3 id="title-construyamos" class="animate-bounce">Construyamos</h3>
    </RouterLink>

    <RouterLink
      to="/vista-ingeniero"
      @click="nivelStorage.agregarNivel('Ingeniero')"
      class="flex flex-col items-center"
      id="link-programemos"
      :class="getImageClass(2)"
    >
      <img
        src="../assets/iconos_inicio/cuadrangular.png"
        alt="Cuadrangular"
        id="img-programemos"
        class="object-contain"
      />
      <h3 id="title-programemos" class="animate-bounce">Programemos</h3>
    </RouterLink>

    <RouterLink
      to="/vista-final"
      @click="nivelStorage.agregarNivel('Presentacion')"
      class="flex flex-col items-center"
      id="link-presentemos"
      :class="getImageClass(3)"
    >
      <img
        src="../assets/iconos_inicio/piramide.png"
        alt="Pirámide"
        id="img-presentemos"
        class="object-contain"
      />
      <h3 id="title-presentemos" class="animate-bounce">Presentemos</h3>
    </RouterLink>
  </div>
</template>

<script setup lang="ts">
import { watch } from 'vue';
import { useNivelesStore } from '@/almacenamiento/Niveles.store';
import { GrupoElegido } from '../composables/store';

console.log('grupo elegido final', GrupoElegido.value[0].progreso);

const nivelStorage = useNivelesStore();

const manejarProgreso = () => {
  const progreso = GrupoElegido.value[0]?.progreso; // Aquí progreso es de tipo string[]

  // Verificar el valor de progreso y llamar a la función correspondiente
  if (!progreso || progreso.length === 0 || progreso.includes('Sin progreso')) {
    console.log('No hay progreso o progreso está vacío.');
    return; // Salir si no hay progreso
  }

  if (progreso.includes('Historia')) {
    nivelStorage.agregarNivel('Historia');
  }
  if (progreso.includes('Constructor')) {
    nivelStorage.agregarNivel('Historia'); // Agregar historia también
    nivelStorage.agregarNivel('Constructor');
  }
  if (progreso.includes('Ingeniero')) {
    nivelStorage.agregarNivel('Historia'); // Agregar historia también
    nivelStorage.agregarNivel('Constructor');
    nivelStorage.agregarNivel('Ingeniero');
  }
  if (progreso.includes('Presentacion')) {
    nivelStorage.agregarNivel('Historia'); // Agregar historia también
    nivelStorage.agregarNivel('Constructor');
    nivelStorage.agregarNivel('Ingeniero');
    nivelStorage.agregarNivel('Presentacion');
  }

  console.log('Progreso manejado con éxito.');
};

manejarProgreso();
// Computa las clases de opacidad y deshabilitación en función del largo de niveles
const getImageClass = (index: number) => {
  const length = nivelStorage.niveles.length;
  if (length === 0 && index > 0) {
    return 'opacity-50 pointer-events-none'; // Todos menos el primero al 50% de opacidad y deshabilitados
  }
  if (length === 1 && (index === 2 || index === 3)) {
    return 'opacity-50 pointer-events-none'; // El tercer y cuarto al 50% y deshabilitados
  }
  if (length === 2 && index === 3) {
    return 'opacity-50 pointer-events-none'; // Solo el cuarto al 50% y deshabilitado
  }
  return 'opacity-100'; // Todos visibles y habilitados
};

// Observa cambios en la longitud de niveles
watch(
  () => nivelStorage.niveles.length,
  (newLength, oldLength) => {
    console.log(`La longitud de niveles ha cambiado: ${oldLength} -> ${newLength}`);
  },
);
</script>

<style scoped>
.opacity-100 {
  opacity: 1; /* Totalmente visible */
}

.opacity-50 {
  opacity: 0.5; /* 50% de opacidad */
}

.pointer-events-none {
  pointer-events: none; /* Deshabilitar interacción */
}

/* Estilos generales */
#grid-container {
  display: grid;
  grid-template-columns: repeat(1, 1fr);
  gap: 1.5rem; /* Espacio entre elementos */
  margin: 1.5rem; /* Margen alrededor del contenedor */
}

.flex {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.object-contain {
  width: 100%;
  height: auto;
}

/* Estilos específicos para los enlaces */
#link-empecemos,
#link-construyamos,
#link-programemos,
#link-presentemos {
  text-align: center;
}

h3 {
  font-weight: bold;
  margin-bottom: 0.5rem; /* Margen inferior de los títulos */
}

/* Media Queries */
@media (min-width: 640px) {
  #grid-container {
    grid-template-columns: repeat(2, 1fr); /* Dos columnas en pantallas pequeñas */
  }
}

@media (min-width: 768px) {
  #grid-container {
    grid-template-columns: repeat(2, 1fr); /* Tres columnas en pantallas medianas */
  }

  h3 {
    font-size: 1.5rem; /* Aumentar el tamaño del texto en pantallas medianas */
  }

  .object-contain {
    width: 100px;
    height: auto;
  }
}

@media (min-width: 1024px) {
  #grid-container {
    grid-template-columns: repeat(4, 1fr); /* Cuatro columnas en pantallas grandes */
  }

  h3 {
    font-size: 1.75rem; /* Aumentar aún más el tamaño del texto en pantallas grandes */
  }

  .object-contain {
    width: 500px;
    height: auto;
  }
}
</style>

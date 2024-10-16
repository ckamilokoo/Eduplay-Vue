<script lang="ts" setup>
import { computed } from 'vue';
import { RouterView } from 'vue-router';
import Tarjeta from './components/BuscarGrupo.vue';
import { Eleccion, GrupoElegido, Guardado } from './composables/store';

const cambiarvalor = () => {
  Eleccion.value = !Eleccion.value;
};

// Computed para obtener la información del grupo elegido
const grupoSeleccionado = computed(() => {
  return GrupoElegido.value.length > 0 ? GrupoElegido.value[0] : null;
});

const GuardarAlumnos = () => {
  Guardado.value = !Guardado.value;
};

const guardarAlumnos = computed(() => !Guardado.value);

// Hacemos que Eleccion sea reactiva
</script>

<template>
  <div id="app-container" class="flex h-screen">
    <!-- Sidebar -->
    <Tarjeta v-if="!Eleccion" />

    <aside v-if="Eleccion" id="sidebar" class="sidebar">
      <div>
        <RouterLink to="/" class="flex flex-col items-center">
          <img alt="Vue logo" id="logo" src="./assets/steamplay.png" />
        </RouterLink>
      </div>
      <h2 id="group-title" class="group-title">
        {{ grupoSeleccionado ? grupoSeleccionado.nombre : 'Grupo no seleccionado' }} 🌟
      </h2>
      <ul id="members-list" class="members-list">
        <li v-for="alumno in grupoSeleccionado?.alumnos ?? []" :key="alumno.id" class="member-item">
          👦 {{ alumno.nombre }}
        </li>
      </ul>

      <button v-if="guardarAlumnos" id="save-button" @click="GuardarAlumnos" class="save-button">
        Guardar
      </button>
      <button v-if="guardarAlumnos" class="cambiar-button" @click="cambiarvalor">cambiar</button>
    </aside>

    <div v-if="Eleccion" id="main-content" class="flex flex-col flex-1 bg-main">
      <!-- Header -->
      <header id="header" class="header">
        <h1 class="header-title">Colegio : {{ grupoSeleccionado?.colegio }}</h1>
        <hr class="header-divider" />
      </header>

      <!-- Main Content -->
      <main id="router-view" class="main-content">
        <RouterView />
      </main>
    </div>
  </div>
</template>

<style scoped>
/* Estilos generales */
#app-container {
  display: flex;
  height: 100vh; /* Ocupa toda la altura de la pantalla */
}

#sidebar {
  width: 13rem; /* Ancho de la barra lateral */
  background-image: url('@/assets/fondo/fondo_eduplay.png');
  border-right: 2px solid orange;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
}

#logo {
  margin-bottom: 1rem; /* Espacio debajo del logo */
  height: 200px !important;
  width: 300px !important;
}

.group-title {
  font-weight: 800; /* Fuente extra negrita */
  font-size: 1.5rem; /* Tamaño de fuente */
  color: #d2006b; /* Color rosa */
  margin-bottom: 0.5rem; /* Margen inferior */
  text-align: center; /* Centrar texto */
  text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.5); /* Sombra de texto */
}

#members-list {
  display: flex;
  flex-direction: column;
  align-items: center;
  list-style-type: none; /* Sin viñetas */
  padding: 0; /* Sin padding */
}

.member-item {
  margin-bottom: 0.5rem; /* Espacio entre los elementos de la lista */
  font-size: 1.125rem; /* Tamaño de fuente */
  color: #0000ff; /* Color azul */
  font-weight: 600; /* Fuente semi-negrita */
  transition: all 0.3s ease; /* Transición suave */
}

.member-item:hover {
  color: #ffc107; /* Color amarillo en hover */
  transform: scale(1.1); /* Aumentar tamaño en hover */
}

.save-button {
  background-color: #ff5722; /* Color de fondo naranja */
  color: white; /* Color del texto blanco */
  font-weight: bold; /* Texto en negrita */
  padding: 0.5rem 1rem; /* Espaciado interno */
  border-radius: 9999px; /* Bordes redondeados */
  margin-top: 1rem; /* Margen superior */
  border: none; /* Sin borde */
  cursor: pointer; /* Cambiar cursor a mano */
}

.cambiar-button {
  background-color: #2eb60f; /* Color de fondo naranja */
  color: white; /* Color del texto blanco */
  font-weight: bold; /* Texto en negrita */
  padding: 0.5rem 1rem; /* Espaciado interno */
  border-radius: 9999px; /* Bordes redondeados */
  margin-top: 1rem; /* Margen superior */
  border: none; /* Sin borde */
  cursor: pointer;
}

.save-button:hover {
  background-color: #e64a19; /* Color de fondo más oscuro en hover */
}

#main-content {
  flex: 1; /* Toma el espacio restante */
  background-image: url('@/assets/fondo/fondo_eduplay.png'); /* Fondo principal */
}

.header {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 5rem; /* Altura del encabezado */
  padding: 0 1rem; /* Espaciado interno */
  border-bottom: 2px solid orange; /* Borde inferior */
}

.header-title {
  text-align: center; /* Centrar texto */
  font-size: 2rem; /* Tamaño de fuente */
  font-weight: 800; /* Fuente extra negrita */
  color: #4caf50; /* Color verde */
  text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.5); /* Sombra de texto */
}

.header-divider {
  margin: 0.5rem 0; /* Margen superior e inferior */
}

.main-content {
  flex: 1; /* Ocupa el espacio restante */
  display: flex;
  align-items: center; /* Centra verticalmente */
  justify-content: center; /* Centra horizontalmente */
  padding: 0rem; /* Espaciado interno */
}

/* Media Queries */
@media (max-width: 768px) {
  #sidebar > div {
    margin-top: 0; /* Asegurarte de que no haya margen superior en el contenedor del logo */
  }
  #sidebar {
    width: 10rem; /* Reducir ancho de la barra lateral */
  }

  .group-title {
    font-size: 1.25rem; /* Reducir tamaño de fuente */
  }

  .member-item {
    font-size: 0.9rem; /* Reducir tamaño de fuente */
  }

  .header-title {
    font-size: 1.25rem; /* Reducir tamaño de fuente */
  }

  .save-button {
    padding: 0.2rem 0.7rem;
    border-radius: 99px;
    margin-top: 1px;
  }
}

@media (max-width: 480px) {
  #sidebar {
    width: 8rem; /* Ancho más pequeño en pantallas pequeñas */
  }

  .group-title {
    font-size: 1rem; /* Tamaño más pequeño */
  }

  .member-item {
    font-size: 0.875rem; /* Tamaño más pequeño */
  }

  .header-title {
    font-size: 1rem; /* Tamaño más pequeño */
  }
}
</style>

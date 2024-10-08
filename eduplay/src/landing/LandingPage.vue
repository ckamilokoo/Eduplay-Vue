<script lang="ts" setup>
import { RouterView } from 'vue-router';

import Tarjeta from '../components/BuscarGrupo.vue';

let Eleccion = true;
</script>

<template>
  <div id="app-container" class="flex h-screen">
    <!-- Sidebar -->
    <div>
      <aside id="sidebar" class="sidebar">
        <div>
          <RouterLink to="/" class="flex flex-col items-center">
            <img alt="Vue logo" id="logo" src="@/assets/EDUPLAY.png" width="200" height="200" />
          </RouterLink>
        </div>

        <h2 id="group-title" class="group-title">Grupo 1 🌟</h2>
        <ul id="members-list" class="members-list">
          <li class="member-item">👦 Camilo Campos</li>
          <li class="member-item">👦 Camilo Campos</li>
          <li class="member-item">👦 Camilo Campos</li>
        </ul>

        <button id="save-button" class="save-button">Guardar</button>
      </aside>

      <div id="main-content" class="flex flex-col flex-1 bg-main">
        <!-- Header -->
        <header id="header" class="header">
          <h1 class="header-title">Colegio XXXX</h1>
          <hr class="header-divider" />
          <h1 class="header-title">2do. grado</h1>
        </header>

        <!-- Main Content -->
        <main id="router-view" class="main-content">
          <RouterView />
        </main>
      </div>
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
  font-size: 1.5rem; /* Tamaño de fuente */
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

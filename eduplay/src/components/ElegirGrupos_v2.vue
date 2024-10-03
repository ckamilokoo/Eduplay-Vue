<template>
  <div id="grid-container" class="grid">
    <RouterLink to="/video-historia" class="flex flex-col items-center" id="link-empecemos">
      <img
        src="../assets/iconos_inicio/cilindro.png"
        alt="Cilindro"
        id="img-empecemos"
        class="object-contain"
      />
      <h3 id="title-empecemos" class="animate-bounce">Empecemos</h3>
    </RouterLink>

    <RouterLink to="/vista-Construtor" class="flex flex-col items-center" id="link-construyamos">
      <img
        src="../assets/iconos_inicio/esfera.png"
        alt="Esfera"
        id="img-construyamos"
        class="object-contain"
      />
      <h3 id="title-construyamos" class="animate-bounce">Construyamos</h3>
    </RouterLink>

    <RouterLink to="/vista-ingeniero" class="flex flex-col items-center" id="link-programemos">
      <img
        src="../assets/iconos_inicio/cuadrangular.png"
        alt="Cuadrangular"
        id="img-programemos"
        class="object-contain"
      />
      <h3 id="title-programemos" class="animate-bounce">Programemos</h3>
    </RouterLink>

    <RouterLink to="/vista-final" class="flex flex-col items-center" id="link-presentemos">
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

<script setup></script>

<style scoped>
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

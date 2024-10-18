<template>
  <div class="main-container">
    <div class="container">
      <h1 class="title">Presentemos</h1>
      <h2 class="subtitle">
        1. Presenta a cada miembro del equipo con el rol que le tocó en esta oportunidad.
      </h2>
      <h2 class="subtitle">
        2. Indica cual es el personaje más interesante de la historia y por qué.
      </h2>
      <h2 class="subtitle">
        3. Menciona si ustedes como equipo le hubiesen dado más ideas a Susy y Freddy. ¿Podrías
        mencionar una?.
      </h2>
      <h2 class="subtitle">4. ¿Qué fue lo más difícil del proyecto?, ¿Por qué?.</h2>
      <h2 class="subtitle">
        5. ¿Tuvieron que repetir la secuencia de programación o no fue necesario?.
      </h2>
      <h2 class="subtitle">6. Muestra la foto que se tomaron con el equipo.</h2>
    </div>
    <div class="image-container">
      <img class="presentemos-image" src="../assets/presentemos.jpg" alt="Equipo Presentemos" />
      <button class="colorful-button">Terminar</button>
    </div>
  </div>
</template>

<script setup></script>

<style scoped>
/* Contenedor principal para alinear el contenido y la imagen */
.main-container {
  display: flex; /* Hacer un contenedor flex */
  justify-content: space-between; /* Espacio entre contenido y la imagen */
  align-items: flex-start; /* Alinear elementos en la parte superior */
  max-width: 1000px; /* Limitar ancho total del contenedor */
  margin: 0 auto; /* Centrar el contenedor principal */
}

/* Estilo general para el contenedor */
.container {
  padding: 24px; /* Espaciado interno */
  background-color: #ebf8ff; /* Color de fondo similar a bg-blue-100 */
  border-radius: 10px; /* Bordes redondeados */
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1); /* Sombra para el contenedor */
  width: 600px; /* Ancho relativo del contenedor de texto */
  text-align: center; /* Centrar en la página */
  margin-right: 20px; /* Espacio entre contenedor de texto y la imagen */
}

/* Estilo para el contenedor de la imagen y el botón */
.image-container {
  display: flex;
  flex-direction: column; /* Alinear la imagen y el botón en columna */
  align-items: center; /* Centrar la imagen y el botón */
}

/* Estilo para la imagen */
.presentemos-image {
  width: 400px; /* Ancho relativo para la imagen */
  height: 480px; /* Alto relativo para la imagen */
  border-radius: 10px; /* Bordes redondeados */
}

/* Estilo para el botón colorido */
.colorful-button {
  background-color: #ff6f61; /* Color de fondo vibrante */
  color: white; /* Color del texto */
  padding: 12px 24px; /* Tamaño del botón */
  border: none; /* Sin borde */
  border-radius: 9999px; /* Bordes redondeados */
  font-weight: bold; /* Texto en negrita */
  font-size: 1.25rem; /* Tamaño de fuente */
  cursor: pointer; /* Cambia el cursor al pasar sobre el botón */
  transition: background-color 0.3s; /* Transición para el color de fondo */
  margin-top: 16px; /* Espacio entre la imagen y el botón */
}

/* Efecto al pasar el ratón sobre el botón */
.colorful-button:hover {
  background-color: #ff3e30; /* Color más oscuro al pasar el ratón */
}

/* Estilo para el título principal */
.title {
  font-size: 2.5rem; /* Tamaño de fuente similar a text-4xl */
  font-weight: 800; /* Negrita similar a font-extrabold */
  text-align: center; /* Centrar texto */
  color: #d53f8c; /* Color similar a text-pink-500 */
  animation: bounce 1s infinite; /* Animación de rebote */
  margin-bottom: 16px; /* Espacio en la parte inferior */
}

/* Estilo para los subtítulos */
.subtitle {
  font-size: 1.25rem; /* Tamaño de fuente similar a text-xl */
  color: #6b46c1; /* Color similar a text-purple-700 */
  font-weight: 500; /* Peso de fuente similar a font-medium */
  line-height: 1.6; /* Espaciado entre líneas */
  margin-bottom: 12px; /* Espacio en la parte inferior */
}

/* Animación de rebote */
@keyframes bounce {
  0%,
  20%,
  50%,
  80%,
  100% {
    transform: translateY(0);
  }
  40% {
    transform: translateY(-20px);
  }
  60% {
    transform: translateY(-10px);
  }
}

/* Adaptación para pantallas pequeñas */
@media (max-width: 640px) {
  .title {
    font-size: 2rem; /* Tamaño de fuente para pantallas pequeñas */
  }

  .subtitle {
    font-size: 1rem; /* Tamaño de fuente para subtítulos en pantallas pequeñas */
  }
}

/* Adaptación para pantallas medianas */
@media (min-width: 641px) and (max-width: 1024px) {
  .title {
    font-size: 2.25rem; /* Tamaño de fuente para pantallas medianas */
  }

  .subtitle {
    font-size: 1rem; /* Tamaño de fuente para subtítulos en pantallas medianas */
  }

  .container {
    padding: 24px; /* Espaciado interno */
    background-color: #ebf8ff; /* Color de fondo similar a bg-blue-100 */
    border-radius: 10px; /* Bordes redondeados */
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1); /* Sombra para el contenedor */
    max-width: 500px; /* Ancho máximo */
    text-align: center; /* Centrar en la página */
  }
}

/* Adaptación para pantallas grandes */
@media (min-width: 1025px) {
  .title {
    font-size: 2.5rem; /* Tamaño de fuente para pantallas grandes */
  }

  .subtitle {
    font-size: 1.25rem; /* Tamaño de fuente para subtítulos en pantallas grandes */
  }
}
</style>

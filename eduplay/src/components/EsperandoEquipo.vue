<template>
  <div>
    <h1 class="text-center text-3xl font-bold mb-6">Esperando al equipo</h1>

    <!-- Formulario para agregar un alumno -->
    <div class="mb-4">
      <input
        v-model="newAlumno"
        placeholder="Agregar nombre de alumno"
        class="border px-4 py-2 mr-2"
        :disabled="alumnosLlenos"
      />
      <button
        @click="addAlumno"
        class="bg-blue-500 text-white px-4 py-2"
        :disabled="alumnosLlenos"
        :class="{ 'opacity-50 cursor-not-allowed': alumnosLlenos }"
      >
        Agregar
      </button>
      <div v-if="alumnosLlenos" class="mt-10 mb-4 text-center">
        <RouterLink to="/VideoHistoria" class="bg-blue-500 text-white px-10 py-6">
          Iniciar la Aventura
        </RouterLink>
      </div>
    </div>

    <!-- Div grande con un ancho específico y dividido en 4 partes -->
    <div class="grid grid-cols-2 grid-rows-2 gap-4 h-[500px] w-[800px] p-4 mx-auto">
      <!-- Parte 1 -->
      <div class="bg-blue-500 text-white p-4 flex flex-col items-center justify-center">
        <div v-if="parte1" class="text-center">
          <h3 class="text-3xl">{{ parte1 }}</h3>
          <div class="mt-2 flex flex-col items-center">
            <button @click="editAlumno(0, 0)" class="bg-emerald-500 text-white px-2 py-1 mb-1">
              Editar
            </button>
            <button @click="removeAlumno(0, 0)" class="bg-pink-800 text-white px-2 py-1">
              Eliminar
            </button>
          </div>
        </div>
      </div>

      <!-- Parte 2 -->
      <div class="bg-green-500 text-white p-4 flex flex-col items-center justify-center">
        <div v-if="parte2" class="text-center">
          <h3 class="text-3xl">{{ parte2 }}</h3>
          <div class="mt-2 flex flex-col items-center">
            <button @click="editAlumno(0, 1)" class="bg-emerald-500 text-white px-2 py-1 mb-1">
              Editar
            </button>
            <button @click="removeAlumno(0, 1)" class="bg-pink-800 text-white px-2 py-1">
              Eliminar
            </button>
          </div>
        </div>
      </div>

      <!-- Parte 3 -->
      <div class="bg-yellow-500 text-white p-4 flex flex-col items-center justify-center">
        <div v-if="parte3" class="text-center">
          <h3 class="text-3xl">{{ parte3 }}</h3>
          <div class="mt-2 flex flex-col items-center">
            <button @click="editAlumno(0, 2)" class="bg-emerald-500 text-white px-2 py-1 mb-1">
              Editar
            </button>
            <button @click="removeAlumno(0, 2)" class="bg-pink-800 text-white px-2 py-1">
              Eliminar
            </button>
          </div>
        </div>
      </div>

      <!-- Parte 4 -->
      <div class="bg-red-500 text-white p-4 flex flex-col items-center justify-center">
        <div v-if="parte4" class="text-center">
          <h3 class="text-3xl">{{ parte4 }}</h3>
          <div class="mt-2 flex flex-col items-center">
            <button @click="editAlumno(0, 3)" class="bg-emerald-500 text-white px-2 py-1 mb-1">
              Editar
            </button>
            <button @click="removeAlumno(0, 3)" class="bg-pink-800 text-white px-2 py-1">
              Eliminar
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, computed } from 'vue';

// Define un tipo para el array de alumnos
type Alumno = string | null;

// Estado para almacenar los nombres de los alumnos (uno por parte)
const newAlumno = ref<string>('');
const alumnos = ref<Alumno[]>([null, null, null, null]); // Solo un alumno por parte

// Métodos para las partes
const parte1 = ref<Alumno>(alumnos.value[0]);
const parte2 = ref<Alumno>(alumnos.value[1]);
const parte3 = ref<Alumno>(alumnos.value[2]);
const parte4 = ref<Alumno>(alumnos.value[3]);

// Computed para verificar si ya hay 4 alumnos
const alumnosLlenos = computed<boolean>(() => alumnos.value.every((alumno) => alumno !== null));

// Función para agregar un nuevo alumno a la primera parte disponible
function addAlumno(): void {
  if (newAlumno.value.trim() && !alumnosLlenos.value) {
    const indexDisponible = alumnos.value.findIndex((alumno) => alumno === null);
    if (indexDisponible !== -1) {
      alumnos.value[indexDisponible] = newAlumno.value;
      updatePartes();
      newAlumno.value = ''; // Limpiar el input después de agregar
    } else {
      alert('Todas las partes están llenas. Elimina un alumno para agregar otro.');
    }
  }
}

// Función para editar un alumno
function editAlumno(index: number, parte: number): void {
  const nuevoNombre = prompt('Edita el nombre del alumno:', alumnos.value[parte] ?? '');
  if (nuevoNombre !== null && nuevoNombre.trim()) {
    alumnos.value[parte] = nuevoNombre.trim();
    updatePartes();
  }
}

// Función para eliminar un alumno
function removeAlumno(index: number, parte: number): void {
  alumnos.value[parte] = null;
  updatePartes();
}

// Función para actualizar las referencias de partes
function updatePartes(): void {
  parte1.value = alumnos.value[0];
  parte2.value = alumnos.value[1];
  parte3.value = alumnos.value[2];
  parte4.value = alumnos.value[3];
}
</script>

<style scoped>
/* Puedes agregar estilos personalizados aquí */
</style>

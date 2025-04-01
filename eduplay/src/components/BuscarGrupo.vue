<template>
  <div class="flex items-center justify-center h-screen w-screen bg-container">
    <div class="mr-6">
      <img
        src="../assets/steamplay.png"
        alt="Descripción de la imagen"
        class="w-[300px] h-[300px] object-cover rounded-lg mr-10"
      />
    </div>
    <div class="p-6 rounded-xl shadow-xl w-full max-w-[700px]">
      <h1 class="text-2xl font-bold text-center mb-6">Bienvenido a STEAMPLAY 🧱</h1>
      <table class="min-w-full w-[650px] bg-white border border-gray-300 mb-4">
        <thead>
          <tr class="bg-gray-200">
            <th class="py-2 px-4 border-b">Nombre</th>
            <th class="py-2 px-4 border-b">Colegio</th>
            <th class="py-2 px-4 border-b">ID</th>
            <th class="py-2 px-4 border-b">Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="curso in cursos" :key="curso.id">
            <td class="py-2 px-4 border-b">{{ curso.nombre }}</td>
            <td class="py-2 px-4 border-b">{{ curso.colegio }}</td>
            <td class="py-2 px-4 border-b">{{ curso.id }}</td>
            <td class="py-2 px-4 border-b">
              <button
                type="button"
                @click="mostrarGrupos(curso.id)"
                class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-3 rounded focus:outline-none focus:shadow-outline"
              >
                Mostrar Grupos
              </button>
            </td>
          </tr>
        </tbody>
      </table>

      <!-- Tabla de grupos filtrados -->
      <table v-if="grupoSeleccionado" class="min-w-full w-[600px] bg-white border border-gray-300">
        <thead>
          <tr class="bg-gray-200">
            <th class="py-2 px-4 border-b">Nombre del Grupo</th>
            <th class="py-2 px-4 border-b">ID</th>
            <th class="py-2 px-4 border-b">Alumnos</th>
            <th class="py-2 px-4 border-b">Elegir Grupo</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="grupo in gruposFiltrados" :key="grupo.id">
            <td class="py-2 px-4 border-b">{{ grupo.nombre }}</td>
            <td class="py-2 px-4 border-b">{{ grupo.id }}</td>
            <td class="py-2 px-4 border-b">
              {{
                grupo.alumnos
                  ? grupo.alumnos.map((alumno) => alumno.nombre).join(', ')
                  : 'Sin alumnos'
              }}
            </td>
            <td class="py-2 px-4 border-b">
              <button
                type="button"
                @click="elegirGrupo(grupo)"
                class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-3 rounded focus:outline-none focus:shadow-outline"
              >
                Seleccionar
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { GrupoElegido } from '../composables/store';
import { type Curso, type Grupo } from '../interfaces/modelos';
import axios from 'axios';
import { Eleccion } from '../composables/store';

const cursos = ref<Curso[]>([]);
const grupos = ref<Grupo[]>([]);
const gruposFiltrados = ref<Grupo[]>([]);
const grupoSeleccionado = ref<number | null>(null);
const loading = ref<boolean>(false);
const error = ref<string | null>(null);

// Función para obtener cursos y grupos desde el backend
const fetchCursosYGrupos = async () => {
  loading.value = true;
  error.value = null;

  try {
    // Obtener cursos
    const responseCursos = await axios.get('https://paneladmin-a67gr1hs.b4a.run/cursos');
    cursos.value = responseCursos.data;

    // Obtener grupos
    const responseGrupos = await axios.get('https://paneladmin-a67gr1hs.b4a.run/grupos');
    console.log(responseGrupos.data);
    grupos.value = responseGrupos.data;
  } catch (err) {
    error.value = 'Error fetching cursos o grupos';
    console.error(error.value, err);
  } finally {
    loading.value = false;
  }
};

// Función para mostrar grupos asociados al curso seleccionado
const mostrarGrupos = (cursoId: number) => {
  grupoSeleccionado.value = cursoId; // Almacena el ID del curso seleccionado
  gruposFiltrados.value = grupos.value.filter((grupo) => grupo.curso_id === cursoId); // Filtrar los grupos
};

// Función para elegir un grupo
const elegirGrupo = (grupo: Grupo) => {
  // Obtener el curso correspondiente al grupo seleccionado
  const curso = cursos.value.find((c) => c.id === grupo.curso_id);

  // Almacenar la información del grupo y el nombre del colegio
  GrupoElegido.value = [
    {
      id: grupo.id,
      nombre: grupo.nombre,
      curso_id: grupo.curso_id,
      colegio: curso ? curso.colegio : 'Colegio no encontrado', // Obtener el nombre del colegio
      alumnos: grupo.alumnos,
      progreso: grupo.progreso,
    },
  ];
  console.log('Grupo elegido:', GrupoElegido.value); // Verificar en la consola
  Eleccion.value = !Eleccion.value;
};

fetchCursosYGrupos();
// Llamar la función cuando sea necesario, por ejemplo en el montaje del componente
</script>

<style scoped>
.bg-container {
  background-image: url('@/assets/fondo/fondo_eduplay.png');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}
</style>

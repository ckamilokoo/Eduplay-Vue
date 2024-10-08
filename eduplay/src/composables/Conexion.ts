import { onMounted, ref } from 'vue';
import { type Curso, type Alumno, type Grupo } from '../interfaces/modelos';
import axios from 'axios'; // Asegúrate de importar axios para las solicitudes HTTP

export const useInformacion = () => {
  const cursos = ref<Curso[]>([]);
  const alumnos = ref<Alumno[]>([]);
  const grupos = ref<Grupo[]>([]); // Cambiado a un array para reflejar múltiples grupos

  const loading = ref<boolean>(false);
  const error = ref<string | null>(null);

  // Función para obtener cursos desde el backend
  const fetchCursos = async () => {
    loading.value = true;
    error.value = null;

    try {
      const response = await axios.get('http://127.0.0.1:5000/cursos'); // Asegúrate de que esta URL sea correcta
      cursos.value = response.data; // Asumiendo que el backend retorna un array de Cursos
    } catch (err) {
      error.value = 'Error fetching cursos';
      console.error(error.value, err);
    } finally {
      loading.value = false;
    }
  };

  // Función para obtener alumnos desde el backend
  const fetchAlumnos = async () => {
    loading.value = true;
    error.value = null;

    try {
      const response = await axios.get('/api/alumnos'); // Asegúrate de que esta URL sea correcta
      alumnos.value = response.data; // Asumiendo que el backend retorna un array de Alumnos
    } catch (err) {
      error.value = 'Error fetching alumnos';
      console.error(error.value, err);
    } finally {
      loading.value = false;
    }
  };

  // Función para obtener grupos desde el backend
  const fetchGrupos = async () => {
    loading.value = true;
    error.value = null;

    try {
      const response = await axios.get('/api/grupos'); // Asegúrate de que esta URL sea correcta
      grupos.value = response.data; // Asumiendo que el backend retorna un array de Grupos
    } catch (err) {
      error.value = 'Error fetching grupos';
      console.error(error.value, err);
    } finally {
      loading.value = false;
    }
  };

  // Cargar datos al montar el componente
  onMounted(() => {
    fetchCursos();
    fetchAlumnos();
    fetchGrupos();
  });

  return {
    cursos,
    alumnos,
    grupos,
    loading,
    error,
  };
};

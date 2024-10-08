import type { Nivel, Puntaje } from '@/interfaces/modelos';
import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useNivelesStore = defineStore('nivel', () => {
  const niveles = ref<Nivel[]>([]);

  // Función para agregar un nuevo nivel
  const agregarNivel = (nombre: string): boolean => {
    // Verificar si el nivel ya existe
    const existe = niveles.value.some((nivel) => nivel.name === nombre);
    if (existe) {
      console.error(`El nivel "${nombre}" ya existe.`);
      return false; // Retorna false si el nivel ya existe
    }

    const nuevoNivel: Nivel = {
      id: `${niveles.value.length + 1}`, // Generar un ID único (puedes mejorar esta lógica)
      name: nombre,
      puntajes: [],
    };
    niveles.value.push(nuevoNivel);
    return true; // Retorna true si se agregó el nivel exitosamente
  };

  // Función para agregar puntaje a un nivel específico
  const agregarPuntaje = (nivelId: string, nombrePuntaje: string) => {
    const nivel = niveles.value.find((nivel) => nivel.id === nivelId);
    if (nivel) {
      const nuevoPuntaje: Puntaje = {
        id: `${nivel.puntajes.length + 1}`, // Generar un ID único para el puntaje
        name: nombrePuntaje,
        completeAt: new Date(), // O puedes dejarlo como undefined si prefieres
      };
      nivel.puntajes.push(nuevoPuntaje);
    } else {
      console.error(`Nivel con ID ${nivelId} no encontrado.`);
    }
  };

  return { niveles, agregarNivel, agregarPuntaje };
});

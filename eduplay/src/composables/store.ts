// store.js
import { ref } from 'vue';
import { type GrupoSeleccionado } from '../interfaces/modelos';

export const isConnected = ref(false);

// Almacena el dispositivo conectado
export const connectedDevice = ref(null);

export const GrupoElegido = ref<GrupoSeleccionado[]>([]);

export const Eleccion = ref(false);

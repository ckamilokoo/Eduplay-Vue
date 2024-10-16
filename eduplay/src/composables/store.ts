// store.js
import { ref } from 'vue';
import { type Grupo } from '../interfaces/modelos';
import { type GrupoSeleccionado } from '../interfaces/modelos';

export const isConnected = ref(false);

// Almacena el dispositivo conectado
export const connectedDevice = ref(null);

export const GrupoElegido = ref<GrupoSeleccionado[]>([]);

export const Eleccion = ref(false);

export const Guardado = ref(false);

export const grupos = ref<Grupo[]>([]);

export const comandos = ref(false);

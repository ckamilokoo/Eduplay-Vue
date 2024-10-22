import { createRouter, createWebHistory } from 'vue-router';
import ElegirGrupos_2 from '../components/ElegirGrupos_v2.vue';

// Corrige el nombre del componente

const routes = [
  {
    path: '/',
    name: 'home',
    component: ElegirGrupos_2,
  },
  {
    path: '/esperando-equipo',
    name: 'esperandoEquipo',
    component: () => import('../components/EsperandoEquipo.vue'),
  },
  {
    path: '/video-historia',
    name: 'videoHistoria',
    component: () => import('../components/VideoHistoria.vue'),
  },
  {
    path: '/vista-ingeniero',
    name: 'vistaIngeniero',
    component: () => import('../components/VistaIngeniero.vue'),
  },
  {
    path: '/vista-construtor',
    name: 'vistaConstrutor',
    component: () => import('../components/VistaConstrutor.vue'),
  },
  {
    path: '/vista-final',
    name: 'vistaFinal',
    component: () => import('../components/VistaFinal.vue'),
  },
  {
    path: '/siguiente-proyecto',
    name: 'siguienteproyecto',
    component: () => import('../components/SiguienteProyecto.vue'),
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;

<template>
  <div class="overflow-x-auto w-full">
    <table class="table">
      <!-- head -->
      <thead>
        <tr>
          <th></th>
          <th>Proyecto</th>
          <th>Tareas</th>
          <th>avances</th>
        </tr>
      </thead>
      <tbody>
        <!-- row 2 -->
        <tr v-for="(project, index) in projectsStore.projectList" :key="project.id" class="hover">
          <th>{{ index + 1 }}</th>
          <td>{{ project.name }}</td>
          <td>{{ project.tasks.length }}</td>
          <td><progress class="progress progress-primary w-56" value="40" max="100"></progress></td>
        </tr>
        <!-- row 3 -->
      </tbody>
    </table>
  </div>

  <inputModal
    :open="modelOpen"
    @close="modelOpen = false"
    @value="projectsStore.addProject"
    placeholder="Ingrese el nombre del proyecto"
    title="Nuevo Proyecto"
    sub-title="Dale un nombre unico a tu proyecto"
  />

  <Custom-Modal :open="CustomModelOpen">
    <template #header>
      <h1>Titulo</h1>
    </template>
    <template #body>
      <h1>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsa possimus repellendus itaque
        molestiae quas quasi? Consequuntur, autem in. Totam dicta, neque dolore assumenda tenetur
        non labore ratione hic voluptates ea.
      </h1>
    </template>

    <template #footer>
      <div class="flex justify-end">
        <button @click="CustomModelOpen = false" class="btn mr-4">Close</button>
        <button @click="CustomModelOpen = false" class="btn btn-primary">Aceptar</button>
      </div>
    </template>
  </Custom-Modal>

  <FabBoton @click="modelOpen = true">
    <AddCircle />
  </FabBoton>

  <FabBoton @click="CustomModelOpen = true" position="bottom-left">
    <Mymodal />
  </FabBoton>
</template>

<script lang="ts" setup>
import FabBoton from '@/modules/common/components/FabBoton.vue';
import CustomModal from '@/modules/common/components/CustomModal.vue';
import Mymodal from '@/modules/common/icons/ModalIcon.vue';
import AddCircle from '@/modules/common/icons/AddCircle.vue';
import InputModal from '@/modules/common/components/InputModal.vue';
import { ref } from 'vue';
import { useProjectsStore } from '../store/projects.store';

const modelOpen = ref(false);
const CustomModelOpen = ref(false);

const projectsStore = useProjectsStore();
</script>

<style scoped></style>

<template>
  <div class="flex flex-col">
    <topMenu />
    <main class="flex flex-row">
      <side-menu />
      <router-view></router-view>
    </main>
  </div>
</template>

<script lang="ts" setup>
import topMenu from '@/modules/common/components/TopMenu.vue';
import sideMenu from '../components/SideMenu.vue';
</script>
<style scoped></style>

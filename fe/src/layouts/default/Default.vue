<template>
  <v-app class="contents-out">
    <v-card class="border-radius rounded-lg" elevation="0">
      <v-layout class="contents-in">
        <default-view />
        <default-bar />
      </v-layout>
    </v-card>
  </v-app>
</template>

<script setup>
import DefaultBar from "./SideBar.vue";
import DefaultView from "./View.vue";
</script>

<style>
/* body {
  font-family: "Noto Sans KR", sans-serif;
} */

.contents-out {
  padding: 10px;
  border-radius: 10px;
}

.border-radius {
  border-radius: 10px;
}

.contents-in {
  margin: 7px;
  border: 5px solid #ced4f5;
  border-radius: 10px;
  box-shadow: none;
  height: 95vh;
}

.v-divider {
  border: 2.5px solid #ced4f5;
}

.v-navigation-drawer--right {
  border-left: 5px solid #ced4f5;
}
</style>

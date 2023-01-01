<template>
  <!-- <v-responsive>
    <v-text-field dense flat hide-details rounded solo-inverted></v-text-field>
  </v-responsive> -->
  <!-- <v-text-field
    label="Search"
    variant="outlined"
    filled
    prepend-inner-icon="mdi-magnify"
    single-line
  ></v-text-field> -->
  <v-card-text style="margin-bottom: 30px">
    <v-text-field
      class="search"
      :loading="loading"
      density="compact"
      variant="solo"
      label="Search"
      prepend-inner-icon="mdi-magnify"
      single-line
      hide-details
      @click:append-inner="onClick"
    ></v-text-field>
  </v-card-text>
</template>

<script>
export default {
  data: () => ({
    loaded: false,
    loading: false,
  }),
  methods: {
    onClick() {
      this.loading = true;

      setTimeout(() => {
        this.loading = false;
        this.loaded = true;
      }, 2000);
    },
  },
};
</script>

<style>
.search {
  box-shadow: 5px 5px #e6e8f5;
  margin: #e6e8f5;
  background-color: #e6e8f5;
}

.v-text-field .v-field {
  background-color: #fafafd;
}

.v-input .search {
  background-color: #e6e8f5;
}
</style>

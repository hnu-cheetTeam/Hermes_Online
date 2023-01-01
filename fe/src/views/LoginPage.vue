<template>
  <v-app class="contents-out">
    <v-card class="border-radius rounded-lg" elevation="0">
      <v-layout class="contents-in">
        <v-row no-gutters>
          <!-- <v-col align-self="center"> -->
          <!-- <v-col class="mx-auto px-6 py-8"> -->
          <v-col cols="4" offset="4" align-self="center">
            <v-sheet class="pa-2 ma-2">
              <img
                src="../assets/logo.png"
                alt="logo"
                style="width: 100%; text-align: center"
              />
              <br />
              <br />
              <br />
              <v-form v-model="form" @submit.prevent="onSubmit">
                <v-text-field
                  v-model="email"
                  :readonly="loading"
                  :rules="[required]"
                  class="mb-2"
                  clearable
                  label="Email"
                ></v-text-field>

                <v-text-field
                  v-model="password"
                  :readonly="loading"
                  :type="'password'"
                  :rules="[required]"
                  clearable
                  label="Password"
                ></v-text-field>

                <br />

                <v-btn
                  :disabled="!form"
                  :loading="loading"
                  block
                  color="success"
                  size="large"
                  type="submit"
                  variant="elevated"
                >
                  Sign In
                </v-btn>
              </v-form>
            </v-sheet>
          </v-col>
        </v-row>
      </v-layout>
    </v-card>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    form: false,
    email: null,
    password: null,
    loading: false,
  }),
  methods: {
    onSubmit() {
      if (!this.form) return;

      this.loading = true;

      setTimeout(() => (this.loading = false), 2000);
    },
    required(v) {
      return !!v || "Field is required";
    },
  },
};
</script>

<style>
body {
  font-family: "Noto Sans KR", sans-serif;
}

.contents-out {
  padding: 10px;
  border-radius: 10px;
  height: auto;
}

.contents-in {
  margin: 7px;
  border: 5px solid #ced4f5;
  border-radius: 10px;
  box-shadow: none;
  height: 95vh;
}
</style>

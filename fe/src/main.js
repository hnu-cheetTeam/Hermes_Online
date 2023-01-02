// Components
import App from "./App.vue";

// Composables
import { createApp } from "vue";

// Plugins
import { registerPlugins } from "@/plugins";

const app = createApp(App);

registerPlugins(app);

// API URL init here
// 없어도 될 듯;;
// prettier-ignore
// app.config.globalProperties.APIURL = 'localhost'

app.mount("#app");

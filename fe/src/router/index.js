// Composables
import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    component: () => import("@/layouts/default/Default.vue"),
    children: [
      {
        path: "",
        name: "Home",
        component: () => import("@/views/Home.vue"),
      },
      {
        path: "MyPage",
        name: "MyPage",
        component: () => import("@/views/MyPage.vue"),
      },
      {
        path: "Setting",
        name: "Setting",
        component: () => import("@/views/SettingPage.vue"),
      },
    ],
  },
  {
    path: "/Board/",
    component: () => import("@/layouts/default/Default.vue"),
    children: [
      {
        path: "Notice",
        name: "UnivNotice",
        component: () => import("@/views/BoardNotice.vue"),
      },
      {
        path: "Academic",
        name: "AcademicNotice",
        component: () => import("@/views/BoardAcademic.vue"),
      },
      {
        path: "Job",
        name: "JobNotice",
        component: () => import("@/views/BoardJob.vue"),
      },
      {
        path: "Scholarship",
        name: "ScholarshipNotice",
        component: () => import("@/views/BoardScholarship.vue"),
      },
    ],
  },
  {
    path: "/Login",
    name: "Login",
    component: () => import("@/views/LoginPage.vue"),
  },
  {
    path: "/:catchAll(.*)",
    name: "ErrorPage",
    component: () => import("@/views/ErrorPage.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

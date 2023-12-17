import { createRouter, createWebHistory } from "vue-router";
import CreateUser from "@/views/CreateUser.vue";
import Home from "@/views/Home.vue";
import TeamMatch from "@/views/TeamMatch.vue";
import UserPrefer from "@/views/UserPrefer.vue";
import GetAllUsers from '@/views/GetAllUsers.vue';

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home, // Home 컴포넌트를 메인 페이지로 설정
  },
  {
    path: "/CreateUser",
    name: "CreateUser",
    component: CreateUser,
  },
  {
    path: '/TeamMatch',
    name: 'TeamMatch',
    component: TeamMatch
  },
  {
    path: '/UserPrefer',
    name: 'UserPrefer',
    component: UserPrefer
  },
  {
    path: '/GetAllUsers',
    name: 'GetAllUsers',
    component: GetAllUsers
  }, { path: '/', redirect: '/create_user' },
  {
    path: '/UserPrefer',
    name: 'UserPrefer',
    component: UserPrefer
  }
 
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

  


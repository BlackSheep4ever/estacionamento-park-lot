import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/client',
      name: 'client',

      component: () => import('../views/ClientView.vue')
    },
    {
      path: '/vehicle',
      name: 'vehicle',

      component: () => import('../views/VehicleView.vue')
    },
    {
      path: '/contract',
      name: 'contract',

      component: () => import('../views/ContractView.vue')
    },
    {
      path: '/plan',
      name: 'plan',

      component: () => import('../views/PlanView.vue')
    }
  ]
})

export default router

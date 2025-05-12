// router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Dashboard from '../views/Dashboard.vue'
import UpdatePump from '../views/UpdatePump.vue'
import PumpView from '../views/PumpView.vue'
import CreatePumpView from '../views/CreatePumpView.vue'
import { useAuthStore } from '../store/auth'

const routes = [
  { path: '/', component: Login },
  { path: '/dashboard', component: Dashboard, meta: { requiresAuth: true } },
  { path: '/update', component: UpdatePump, meta: { requiresAuth: true } },
  { path: '/pump/:id', component: PumpView, meta: { requiresAuth: true } },
  { path: '/create_pump', component: CreatePumpView, meta: { requiresAuth: true} }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach(async (to, from, next) => {
  const auth = useAuthStore()
  if (auth.token && !auth.user) await auth.fetchUser()

  if (to.meta.requiresAuth && !auth.isAuthenticated()) {
    next('/')
  } else if (to.path === '/' && auth.isAuthenticated()) {
    next('/dashboard')
  } else {
    next()
  }
})

export default router

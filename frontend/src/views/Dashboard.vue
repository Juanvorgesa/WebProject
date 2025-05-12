<template>
  <div>
    <h2>Bienvenido {{ auth.user.username }}</h2>
    <button @click="auth.logout(); router.push('/')">Cerrar sesión</button>
    <PumpCard
      v-for="pump in pumps"
      :key="pump.id"
      :pump="pump"
      @update="goToUpdate(pump)"
      @view="goToView(pump.id)"
    />
    <button @click="router.push('/create_pump')">+</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useAuthStore } from '../store/auth'
import PumpCard from '../components/PumpCard.vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const auth = useAuthStore()
const router = useRouter()
const pumps = ref([])

onMounted(async () => {
  const response = await axios.get('http://127.0.0.1:8000/pumps', {
    headers: { Authorization: `Bearer ${auth.token}` }
  })

  pumps.value = response.data.map(p => ({
    id: p[0],
    name: p[1],
    ubication: p[2],
    min_voltage: p[3],
    max_voltage: p[4],
    min_elec_current: p[5],
    max_elec_current: p[6],
    min_flow: p[7],
    max_flow: p[8],
    state: p[9],
  }))
})

const goToUpdate = (pump) => {
  router.push({ path: '/update', state: pump })
}
const goToView = (id) => {
  router.push(`/pump/${id}`)
}
</script>

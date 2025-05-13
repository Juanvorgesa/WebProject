<template>
  <div class="body">
    <header class="roboto-100">
      <h1>Bienvenido, {{ auth.user.username }}</h1>
      <button class="logout-btn" @click="auth.logout(); router.push('/')">Cerrar sesión</button>
    </header>
    <main>
      <div class="content">
        <div class="grid-container ">
          <PumpCard
            v-for="pump in pumps"
            :key="pump.id"
            :pump="pump"
            @update="goToUpdate(pump)"
            @view="goToView(pump.id)"
          />
        </div>
      </div>
    </main>

    </div>
  
    <button class="fab" @click="router.push('/create_pump')">+</button>
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

<style>


.grid-container {
  margin: 1rem;
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 2rem;
  padding: 16px;
}
.body {
  margin: 0;
  font-family: Arial, sans-serif;
  background: linear-gradient(135deg,rgb(171, 186, 255),rgb(219, 224, 255));
}

header {
  background-color:rgb(100, 123, 224);
  color: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

header h1 {
  margin: 0;
}

.logout-btn {
  background-color: #ef476f;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1rem;
}

.logout-btn:hover {
  background-color: #d93c63;
}

main {
  display: flex;
  justify-content: center;
  align-items: center;
  height: calc(100vh - 80px);
  padding: 1rem;
}

.content {
  width: 100%;
  height: 100%; 
  background: rgba(255,255,255,0.8);
  padding: 0rem;
  box-shadow: 0 4px 8px rgba(0,0,0,0.8);
  border-radius: 10px;
}

.fab {
  position: fixed;
  bottom: 20px;
  left: 20px;
  width: 40px;
  height: 40px;
  background-color:rgb(178, 170, 252);
  color: white;
  border: none;
  border-radius: 40%;
  font-size: 1rem;
  box-shadow: 0 4px 8px rgba(0,0,0,0.2);
  cursor: pointer;
}

.fab:hover {
  background-color: #04b88a;
}
</style>

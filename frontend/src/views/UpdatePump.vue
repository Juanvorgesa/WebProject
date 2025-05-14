<template>
  <div class="container">
    <div class="card">
      <h2>Actualizar bomba</h2>
      <form @submit.prevent="updatePump(pump)">
        <div class="form-group">
          <label for="name">Nombre:</label>
          <input v-model="pump.name" id="name" />
        </div>

        <div class="form-group">
          <label for="ubication">Ubicación:</label>
          <input v-model="pump.ubication" id="ubication" />
        </div>

        <div class="form-group">
          <label for="min_voltage">Voltaje mínimo:</label>
          <input v-model="pump.min_voltage" id="min_voltage" />
        </div>

        <div class="form-group">
          <label for="max_voltage">Voltaje máximo:</label>
          <input v-model="pump.max_voltage" id="max_voltage" />
        </div>

        <div class="form-group">
          <label for="min_elec_current">Corriente mínima:</label>
          <input v-model="pump.min_elec_current" id="min_elec_current" />
        </div>

        <div class="form-group">
          <label for="max_elec_current">Corriente máxima:</label>
          <input v-model="pump.max_elec_current" id="max_elec_current" />
        </div>

        <div class="form-group">
          <label for="min_flow">Flujo mínimo:</label>
          <input v-model="pump.min_flow" id="min_flow" />
        </div>

        <div class="form-group">
          <label for="max_flow">Flujo máximo:</label>
          <input v-model="pump.max_flow" id="max_flow" />
        </div>

        <div class="button-group">
          <button type="submit" class="submit-btn">Guardar cambios</button>
          <button type="button" class="cancel-btn" @click="cancel">Cancelar</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { useRouter, useRoute } from 'vue-router'
import { ref } from 'vue'
import { useAuthStore } from '../store/auth'
import axios from 'axios'

const router = useRouter()
const auth = useAuthStore()
const statePump = history.state
const pump = ref({ ...statePump })


const cancel = () => {
  router.push('/dashboard')
}

const updatePump = async (pump) => {
  const updatedPump = {
    id: pump.id,
    name: pump.name,
    ubication: pump.ubication,
    min_voltage: pump.min_voltage,
    max_voltage: pump.max_voltage,
    min_elec_current: pump.min_elec_current,
    max_elec_current: pump.max_elec_current,
    min_flow: pump.min_flow,
    max_flow: pump.max_flow
  }
  await axios.post('http://127.0.0.1:8000/pumps' ,updatedPump)
  router.push('/dashboard')
}
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f5f5f5;
}

.card {
  background: white;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
  width: 400px;
}

h2 {
  text-align: center;
  margin-bottom: 1.5rem;
  color: #333;
}

.form-group {
  display: flex;
  flex-direction: column;
  margin-bottom: 1rem;
}

label {
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #444;
}

input {
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 1rem;
}

.button-group {
  display: flex;
  justify-content: space-between;
  margin-top: 1.5rem;
}

.submit-btn,
.cancel-btn {
  padding: 0.5rem 1rem;
  font-size: 1rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.submit-btn {
  background-color: #28a745;
  color: white;
}

.cancel-btn {
  background-color: #dc3545;
  color: white;
}
</style>
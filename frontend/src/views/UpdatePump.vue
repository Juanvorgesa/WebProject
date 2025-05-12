<template>
  <form @submit.prevent="updatePump(pump)">
    <label for="name">Nombre: </label>
    <input v-model="pump.name" id="name"/><br>
    <label for="ubication">Ubicación: </label>
    <input v-model="pump.ubication" id="ubication"/><br>
    <label for="min_voltage">Voltaje mínimo: </label>
    <input v-model="pump.min_voltage" id="min_voltage"/><br>
    <label for="max_voltage">Voltaje máximo: </label>
    <input v-model="pump.max_voltage" id="max_voltage"/><br>
    <label for="min_elec_current">Corriente mínima: </label>
    <input v-model="pump.min_elec_current" id="min_elec_current"/><br>
    <label for="max_elec_current">Corriente máxima: </label>
    <input v-model="pump.max_elec_current" id="max_elec_current"/><br>
    <label for="min_flow">Flujo mínimo: </label>
    <input v-model="pump.min_flow" id="min_flow"/><br>
    <label for="max_flow">Flujo máximo: </label>
    <input v-model="pump.max_flow" id="max_flow"/><br>
    <button type="submit">Guardar cambios</button>
    <button @click="cancel">Cancelar</button>
  </form>
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
  const updatedPump ={
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

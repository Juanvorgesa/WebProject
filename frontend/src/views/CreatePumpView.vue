<template>
    <div>
        <h2>Crear nueva bomba</h2>
        <form @submit.prevent="handleSubmit">
            <label for="name">Nombre: </label>
            <input
                id="name"
                type="text"
                required
            /><br>
            <label for="ubication">Ubicación: </label>
            <input
                id="ubication"
                type="text"
                required
            /><br>
            <label for="min_voltage">Voltaje mínimo: </label>
            <input
                id="min_voltage"
                type="number"
                required
            /><br>
            <label for="max_voltage">Voltaje máximo: </label>
            <input
                id="max_voltage"
                type="number"
                required
            /><br>
            <label for="min_elec_current">Corriente mínima: </label>
            <input
                id="min_elec_current"
                type="number"
                required
            /><br>
            <label for="max_elec_current">Corriente máxima: </label>
            <input
                id="max_elec_current"
                type="number"
                required
            /><br>
            <label for="min_flow">Flujo mínimo: </label>
            <input
                id="min_flow"
                type="number"
                required
            /><br>
            <label for="max_flow">Flujo máximo: </label>
            <input
                id="max_flow"
                type="number"
                required
            /><br>
            <button type="submit">Aceptar</button>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const name = ref('')
const ubication = ref('')
const min_voltage = ref('')
const max_voltage = ref('')
const min_elec_current = ref('')
const max_elec_current = ref('')
const min_flow = ref('')
const max_flow = ref('')

const handleSubmit = async () => {
    const pump = {
        name: name,
        ubication: ubication,
        min_voltage: min_voltage,
        max_voltage: max_voltage,
        min_elec_current: min_elec_current,
        max_elec_current: max_elec_current,
        min_flow: min_flow,
        max_flow: max_flow
    }
    console.log(pump)
    try{
        const response = await axios.put('http://127.0.0.1:8000/pumps', pump)
        router.push('/dashboard')

    } catch (err) {
        console.log(err)
    }

}

</script>

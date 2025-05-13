<template>
    <div>
        <h2>Crear nueva bomba</h2>
        <form @submit.prevent="handleSubmit">
            <label for="name">Nombre: </label>
            <input
                id="name"
                type="text"
                v-model="name"
                required
            /><br>
            <label for="ubication">Ubicación: </label>
            <input
                id="ubication"
                type="text"
                v-model="ubication"
                required
            /><br>
            <label for="min_voltage">Voltaje mínimo: </label>
            <input
                id="min_voltage"
                type="number"
                v-model="min_voltage"
                min="0"
                value="0"
                step="0.01"
                required
            /><br>
            <label for="max_voltage">Voltaje máximo: </label>
            <input
                id="max_voltage"
                type="number"
                v-model="max_voltage"
                min="0"
                value="0"
                step="0.01"
                required
            /><br>
            <label for="min_elec_current">Corriente mínima: </label>
            <input
                id="min_elec_current"
                type="number"
                v-model="min_elec_current"
                min="0"
                value="0"
                step="0.01"
                required
            /><br>
            <label for="max_elec_current">Corriente máxima: </label>
            <input
                id="max_elec_current"
                type="number"
                v-model="max_elec_current"
                min="0"
                value="0"
                step="0.01"
                required
            /><br>
            <label for="min_flow">Flujo mínimo: </label>
            <input
                id="min_flow"
                type="number"
                v-model="min_flow"
                min="0"
                value="0"
                step="0.01"
                required
            /><br>
            <label for="max_flow">Flujo máximo: </label>
            <input
                id="max_flow"
                type="number"
                v-model="max_flow"
                min="0"
                value="0"
                step="0.01"
                required
            /><br>
            <button type="submit">Aceptar</button>
        </form>
        <button type="submit" @click="cancel">Cancelar</button>
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
            name: name.value,
            ubication: ubication.value,
            min_voltage: min_voltage.value,
            max_voltage: max_voltage.value,
            min_elec_current: min_elec_current.value,
            max_elec_current: max_elec_current.value,
            min_flow: min_flow.value,
            max_flow: max_flow.value
        }
        try{
            const response = await axios.put('http://127.0.0.1:8000/pumps', pump)
            router.push('/dashboard')

        } catch (err) {
            console.log(err)
        }
    }

    const cancel = () => {
    router.push('/dashboard')
    }

</script>

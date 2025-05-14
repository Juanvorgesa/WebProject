<template>
  <div class="container">
    <div class="card">
      <h2>Crear nueva bomba</h2>
      <form @submit.prevent="handleSubmit">
        <div class="form-group">
          <label for="name">Nombre:</label>
          <input id="name" type="text" v-model="name" required />
        </div>

        <div class="form-group">
          <label for="ubication">Ubicación:</label>
          <input id="ubication" type="text" v-model="ubication" required />
        </div>

        <div class="form-group">
          <label for="min_voltage">Voltaje mínimo:</label>
          <input id="min_voltage" type="number" v-model="min_voltage" min="0" step="0.01" required />
        </div>

        <div class="form-group">
          <label for="max_voltage">Voltaje máximo:</label>
          <input id="max_voltage" type="number" v-model="max_voltage" min="0" step="0.01" required />
        </div>

        <div class="form-group">
          <label for="min_elec_current">Corriente mínima:</label>
          <input id="min_elec_current" type="number" v-model="min_elec_current" min="0" step="0.01" required />
        </div>

        <div class="form-group">
          <label for="max_elec_current">Corriente máxima:</label>
          <input id="max_elec_current" type="number" v-model="max_elec_current" min="0" step="0.01" required />
        </div>

        <div class="form-group">
          <label for="min_flow">Flujo mínimo:</label>
          <input id="min_flow" type="number" v-model="min_flow" min="0" step="0.01" required />
        </div>

        <div class="form-group">
          <label for="max_flow">Flujo máximo:</label>
          <input id="max_flow" type="number" v-model="max_flow" min="0" step="0.01" required />
        </div>

        <div class="button-group">
          <button type="submit" class="submit-btn">Aceptar</button>
          <button type="button" class="cancel-btn" @click="cancel">Cancelar</button>
        </div>
      </form>
    </div>
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
  background-color: #007bff;
  color: white;
}

.cancel-btn {
  background-color: #e74c3c;
  color: white;
}
</style>

<template>
  <div class="container">
    <div v-if="pump" class="card">
      <h2>Detalles de la Bomba: {{ pump.name }}</h2>
      <p><strong>Ubicación:</strong> {{ pump.ubication }}</p>
      <p><strong>Voltaje:</strong> {{ pump.min_voltage }} - {{ pump.max_voltage }} V</p>
      <p><strong>Corriente:</strong> {{ pump.min_elec_current }} - {{ pump.max_elec_current }} A</p>
      <p><strong>Flujo:</strong> {{ pump.min_flow }} - {{ pump.max_flow }} L/min</p>
      <p>
        <strong>Estado:</strong>
        <span :class="pump.state ? 'status green' : 'status red'">
          {{ pump.state ? 'ON' : 'OFF' }}
        </span>
      </p>
      <div class="buttons">
        <button @click="deletePump(pump.id)" class="btn delete">
          <i class="pi pi-trash">&nbsp;Eliminar</i>
        </button>
        <button @click="$emit('update', pump)" class="btn update">
          <i class="pi pi-sync"></i>&nbsp;Actualizar
        </button>
        <button @click="cancel" class="btn cancel"><i class="pi pi-times">&nbsp;Cancelar</i></button>
      </div>
    </div>
    <div v-else class="loading">
      <p>Cargando detalles...</p>
    </div>
  </div>
</template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  import { useRoute, useRouter } from 'vue-router'
  
  const route = useRoute()
  const router = useRouter()
  const pump = ref(null)
  
  const cancel = () => {
    router.push('/dashboard')
  }

  const fetchPumpDetails = async (id) => {
  try {
    const response = await axios.post(`http://127.0.0.1:8000/pump/${id}`);
    pump.value = {
      id: response.data[0],
      name: response.data[1],
      ubication: response.data[2],
      min_voltage: response.data[3],
      max_voltage: response.data[4],
      min_elec_current: response.data[5],
      max_elec_current: response.data[6],
      min_flow: response.data[7],
      max_flow: response.data[8],
      state: response.data[9],
    }
    } catch (error) {
      console.error('Error al obtener los detalles de la bomba:', error)
    }
  }

  
  const deletePump = async (id) => {
    try {
      await axios.delete(`http://127.0.0.1:8000/pumps/${id}`);
      alert("Bomba eliminada correctamente");
      router.push('/dashboard')
    } catch (error) {
      console.error("Error al eliminar la bomba:", error);
    }
  };
  
  onMounted(() => {
    const pumpId = route.params.id
    fetchPumpDetails(pumpId)
  })
  </script>
  
<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 90vh;
  background-color: #f2f4f8;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.card {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  width: 400px;
  max-width: 90%;
}

.card h2 {
  margin-bottom: 1rem;
  color: #333;
}

.card p {
  margin: 0.5rem 0;
  color: #555;
}

.status {
  font-weight: bold;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  margin-left: 0.5rem;
}

.green {
  background-color: #d4edda;
  color: #155724;
}

.red {
  background-color: #f8d7da;
  color: #721c24;
}

.buttons {
  margin-top: 1.5rem;
  display: flex;
  justify-content: space-between;
}

.btn {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.3s ease;
}

.btn.delete {
  background-color: #dc3545;
  color: white;
}

.btn.delete:hover {
  background-color: #c82333;
}

.btn.cancel {
  background-color: #6c757d;
  color: white;
}

.btn.cancel:hover {
  background-color: #5a6268;
}

.loading {
  font-size: 1.2rem;
  color: #666;
}

.btn.update {
  background-color: #17a2b8;
  color: white;
  display: flex;
  align-items: center;
}

.btn.update:hover {
  background-color: #138496;
}

.pi {
  font-size: 1rem;
}
</style>
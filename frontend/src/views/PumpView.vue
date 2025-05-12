<template>
  <div v-if="pump">
    <h2>Detalles de la Bomba: {{ pump.name }}</h2>
    <p><strong>Ubicación:</strong> {{ pump.ubication }}</p>
    <p><strong>Voltaje:</strong> {{ pump.min_voltage }} - {{ pump.max_voltage }} V</p>
    <p><strong>Corriente:</strong> {{ pump.min_elec_current }} - {{ pump.max_elec_current }} A</p>
    <p><strong>Flujo:</strong> {{ pump.min_flow }} - {{ pump.max_flow }} L/min</p>
    <span><strong>Estado:</strong></span>
    <span :class="[pump.state ? 'green' : 'red']">{{ pump.state ? ' ON' : ' OFF' }}</span><br>
    <button @click="deletePump(pump.id)">Eliminar</button><br>
    <button @click="cancel">Cancelar</button>
  </div>
  <div v-else>
     <p>Cargando detalles...</p>
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
    // Aquí creamos un objeto a partir del arreglo recibido
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
    console.log(pump.value) // Verifica que los datos estén correctos
    } catch (error) {
      console.error('Error al obtener los detalles de la bomba:', error)
    }
  }

  
  const deletePump = async (id) => {
    try {
      await axios.delete(`http://127.0.0.1:8000/pump/${id}`, {
        headers: {
          Authorization: `Bearer ${auth.token}`,  // Asegúrate de pasar el token correctamente
        }
      })
      // Redirigir o actualizar la vista después de eliminar
      alert("Bomba eliminada correctamente")
    } catch (error) {
      console.error("Error al eliminar la bomba:", error)
    }
  }
  
  // Obtener el id de la bomba desde la URL (por ejemplo, /pump/:id)
  onMounted(() => {
    const pumpId = route.params.id  // Asumiendo que el id se pasa en la URL, como '/pump/1'
    fetchPumpDetails(pumpId)
  })
  </script>
  
  <style scoped>
  /* Estilos adicionales */
  h2 {
    color: #4CAF50;
  }
  button {
    background-color: #f44336;
    color: white;
    border: none;
    padding: 10px;
    cursor: pointer;
    margin-top: 20px;
  }
  button:hover {
    background-color: #d32f2f;
  }

.red {
  color:rgb(219, 52, 52);
}

.green {
  color: rgb(5, 165, 0)
}
  </style>
  
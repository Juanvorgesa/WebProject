<template>
  <div class="pump-card">
    <h3>{{ pump.id }}. {{pump.name}}</h3>
    <i :class="['pi', 'pi-map-marker']">&nbsp;{{pump.ubication}}</i>
    <br>
    <i :class="['pi', 'pi-circle-fill', pump.state ? 'green' : 'red']" @click="toggleState(pump.id, pump)"></i>
    <button @click="$emit('update', pump)">Actualizar</button>
    <button @click="$emit('view', pump.id)">Ver</button>
  </div>
</template>

<script setup>
defineProps({ pump: Object })
import 'primeicons/primeicons.css'
import axios from 'axios'

const toggleState = async (id, pump) => {
  try {
    const query = {
        id: id
    }
    pump.state = !pump.state
    const response = await axios.post('http://127.0.0.1:8000/pumps/alter', query)
    console.log(response)
  } catch (error) {
    console.error('Error al alterar la bomba:', error)
  }
}
</script>

<style scoped>
.pump-card {
  border: 1px solid #ccc;
  padding: 1rem;
  margin: 1rem 3rem 1rem 3rem;
  border-radius: 5px;
  box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
}

i {
  font-size: 12px;
  padding: 12px
}

.red {
  color:rgb(219, 52, 52);
}

.green {
  color: rgb(5, 165, 0)
}
</style>


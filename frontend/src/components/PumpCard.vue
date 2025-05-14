<template>
  <div class="pump-card">
    <h3>{{ pump.id }}. {{pump.name}}</h3>
    <i :class="['pi', 'pi-map-marker']">&nbsp;</i>{{pump.ubication}}
    <br>
    <i :class="['pi', 'pi-circle-fill', pump.state ? 'green' : 'red']" @click="toggleState(pump.id, pump)"></i>
    <button @click="$emit('update', pump)"><i :class="['pi', 'pi-sync', 'update']"></i>Actualizar&nbsp;</button>
    <button @click="$emit('view', pump.id)"><i :class="['pi', 'pi-eye', 'update']"></i>Ver&nbsp;</button>
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
    const response = await axios.post('http://127.0.0.1:8000/pumps/alter', query)
    pump.state = !pump.state
  } catch (error) {
    console.error('Error al alterar la bomba:', error)
  }
}
</script>

<style scoped>
.pump-card {
  border: 1px solid #ccc;
  padding: 1rem;
  border-radius: 5px;
  box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
  background: white;
}

.update {
  font-size:12px
}

i {
  font-size: 16px;
  padding: 4px
}

.red {
  color:rgb(219, 52, 52);
}

.green {
  color: rgb(5, 165, 0);
}
button {
  margin-left: 0.5rem;
}
</style>


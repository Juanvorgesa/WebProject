<template>
  <div class="pump-card">
    <div class="sticky-header"></div>
    <h3>{{ pump.id }}. {{pump.name}} </h3>
    <i :class="['pi', 'pi-map-marker']">&nbsp;</i>{{pump.ubication}}
    <p class="voltage-text"
    :class="[(voltage <= average+diff && voltage >= average-diff) ? 'green' :
    (voltage <= props.pump.min_voltage + diff/2 || voltage >= props.pump.max_voltage - diff/2) ? 'red' : 'yellow' ]">
      {{ voltage }} V
    </p>
    <br>
    <i :class="['pi', 'pi-circle-fill', pump.state ? 'green' : 'red']" @click="toggleState(pump.id, pump)"></i>
    <button @click="$emit('update', pump)"><i :class="['pi', 'pi-sync', 'update']"></i>Actualizar&nbsp;</button>
    <button @click="$emit('view', pump.id)"><i :class="['pi', 'pi-eye', 'update']"></i>Ver&nbsp;</button>
  </div>
</template>


<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import axios from 'axios'
import 'primeicons/primeicons.css'

const props = defineProps({ pump: Object }) 
const average = (props.pump.max_voltage + props.pump.min_voltage)/2
const diff = (props.pump.max_voltage - props.pump.min_voltage)/4

const voltage = ref('Cargando...')
let intervalId = null

const fetchVoltage = async () => {
  if (props.pump.state == true) {
    try {
      const values = {
        min: props.pump.min_voltage,
        max: props.pump.max_voltage
      }
      const response = await axios.post('http://127.0.0.1:8000/pumps/var', values)
      voltage.value = response.data ?? 'Sin dato'
    } catch (error) {
      voltage.value = 'Error'
      console.error('Error al obtener el voltaje:', error)
    }
  } else {
    voltage.value = 0
  }
  
}

onMounted(() => {
  fetchVoltage()
  intervalId = setInterval(fetchVoltage, 1000)
})

onUnmounted(() => {
  clearInterval(intervalId)
})

const toggleState = async (id, pump) => {
  try {
    const query = { id }
    await axios.post('http://127.0.0.1:8000/pumps/alter', query)
    pump.state = !pump.state
  } catch (error) {
    console.error('Error al alterar la bomba:', error)
  }
}
</script>


<style scoped>
.pump-card {
  background: #fff88b;
  border: 1px solid #e0d96c;
  border-radius: 5px;
  padding: 1rem;
  padding-top: 2.5rem;
  width: 250px;
  box-shadow: 4px 4px 8px rgba(0, 0, 0, 0.15);
  font-family: 'Patrick Hand', 'Comic Sans MS', cursive, sans-serif;
  position: relative;
  transition: transform 0.2s ease-in-out;
}

.voltage-text {
  font-weight: bold;
  font-size: 28px;
  text-shadow:
    -1px -1px 0 #444,  
     1px -1px 0 #444,
    -1px  1px 0 #444,
     1px  1px 0 #444;
}

.sticky-header {
  position: absolute;
  top: 0;
  left: 0;
  height: 35px;
  width: 100%;
  background-color: #f0df61;
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
}

.pump-card::after {
  content: '';
  position: absolute;
  bottom: 0;
  right: 0;
  border-width: 0 0 20px 20px;
  border-style: solid;
  border-color: transparent transparent #f4e66c transparent;
}

.pump-card:hover {
  transform: rotate(-2deg) scale(1.15);
}

button {
  margin-top: 0.5rem;
  margin-left: 0.5rem;
  background-color: #fdf6b2;
  border: 1px solid #e1d46c;
  border-radius: 3px;
  padding: 0.3rem 0.6rem;
  font-size: 12px;
  cursor: pointer;
}

button:hover {
  background-color: #fce96a;
}

.update {
  font-size: 12px;
}

i {
  font-size: 16px;
  padding: 4px;
}

.red {
  color: rgb(219, 52, 52);
}

.green {
  color: rgb(5, 165, 0);
}

.yellow {
  color: rgb(223, 189, 0);
}

</style>


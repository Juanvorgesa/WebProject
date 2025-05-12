<template>
  <div>
    <div>
      <h2>
        {{ isLogin ? 'Iniciar Sesión' : 'Registrarse' }}
      </h2>

      <form @submit.prevent="handleSubmit">
        <div>
          <label for="username">
            Nombre de usuario
          </label>
          <input
            v-model="form.username"
            id="username"
            type="text"
            required
          />
        </div>

        <div class="mb-4">
          <label for="password">
            Contraseña
          </label>
          <input
            v-model="form.password"
            id="password"
            type="password"
            required
          />
        </div>

        <!-- Mostrar campo adicional solo si es registro -->
        <div v-if="!isLogin">
          <label for="email">
            Correo electrónico
          </label>
          <input
            v-model="form.email"
            id="email"
            type="email"
            required
          />
        </div>

        <button
          type="submit"
        >
          {{ isLogin ? 'Iniciar Sesión' : 'Registrarse' }}
        </button>
      </form>

      <p>
        {{ isLogin ? '¿No tienes una cuenta?' : '¿Ya tienes una cuenta?' }}
        <button @click="toggleForm">
          {{ isLogin ? 'Registrarse' : 'Iniciar sesión' }}
        </button>
        
      </p>
      <p v-if="err">{{ err }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '../store/auth'
import { useRouter } from 'vue-router'

const username = ref('')
const password = ref('')
const error = ref(false)
const auth = useAuthStore()
const router = useRouter()
const isLogin = ref(true)
const err = ref('')

const form = ref({
  username: '',
  email: '',
  password: ''
})

const toggleForm = () => {
  isLogin.value = !isLogin.value
  form.value = { username: '', password: '', email: '' }
}

const handleSubmit = async () => {
  err.value = '' // Limpia mensaje anterior
  if (isLogin.value) {
    const success = await auth.login(form.value.username, form.value.password)
    if (success) {
      router.push('/dashboard')
    } else {
      err.value = 'Nombre de usuario o contraseña incorrectos.'
    }
  } else {
    const success = await auth.register(form.value.username, form.value.email, form.value.password)
    if (success) {
      router.push('/dashboard')
    } else {
      err.value = 'Error al registrar. Verifica los datos e inténtalo de nuevo.'
    }
  }
}

</script>

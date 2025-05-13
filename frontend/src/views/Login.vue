<template>
<div class="template">
  <div>
    <div class="login-container">
      <h2>
        {{ isLogin ? 'Iniciar Sesión' : 'Registrarse' }}
      </h2>
      <form @submit.prevent="handleSubmit">
        <div class="form-group">
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

        <div v-if="!isLogin" class="form-group">
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

        <div class="form-group">
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

        <button
          type="submit"
          class="login-btn"
        >
          {{ isLogin ? 'Iniciar Sesión' : 'Registrarse' }}
        </button>
      </form>
      <div class="bottom-text">
        <p>
          {{ isLogin ? '¿No tienes una cuenta?' : '¿Ya tienes una cuenta?' }}
          <a @click="toggleForm">
            {{ isLogin ? 'Registrarse' : 'Iniciar sesión' }}
          </a>
          
        </p>
        <p v-if="err">{{ err }}</p>
      </div>
    </div>
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
  err.value = ''
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

<style>
  .template {
    margin: 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg,rgb(151, 170, 255),rgb(0, 26, 170));
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    }

    .login-container {
      background: white;
      padding: 2.5rem 2rem;
      border-radius: 15px;
      box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
      width: 100%;
      max-width: 400px;
    }

    .login-container h2 {
      text-align: center;
      margin-bottom: 1.5rem;
      color: #333;
    }

    .form-group {
      margin-bottom: 1.2rem;
      margin-right: 1.5rem;
    }

    .form-group label {
      display: block;
      margin-bottom: 0.5rem;
      font-weight: 600;
      color: #444;
    }

    .form-group input {
      width: 100%;
      padding: 0.75rem;
      border: 1px solid #ccc;
      border-radius: 8px;
      font-size: 1rem;
      transition: border-color 0.3s ease;
    }

    .form-group input:focus {
      border-color: #667eea;
      outline: none;
    }

    .login-btn {
      width: 100%;
      padding: 0.8rem;
      background: #667eea;
      color: white;
      border: none;
      border-radius: 8px;
      font-size: 1rem;
      font-weight: bold;
      cursor: pointer;
      transition: background 0.3s ease;
    }

    .login-btn:hover {
      background: #5a67d8;
    }

    .bottom-text {
      text-align: center;
      margin-top: 1rem;
      font-size: 0.9rem;
      color: #555;
    }

    .bottom-text a {
      color: #667eea;
      text-decoration: none;
    }

    .bottom-text a:hover {
      text-decoration: underline;
      color: #5a67d8;
    }
</style>
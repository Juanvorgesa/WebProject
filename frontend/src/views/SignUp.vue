<template>
    <LoginForm @login-success="handleSuccess" />
  </template>
  
  <script setup>
  import LoginForm from '../components/LoginForm.vue'
  import Dashboard from './Dashboard.vue'
  import { ref } from 'vue'
  
  const handleSuccess = () => {
    // Cargar vista de Dashboard tras login exitoso
    window.location.reload() // o redirigir si usas Vue Router
  }
  </script>
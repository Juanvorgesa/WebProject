<template>
    <LoginForm @login-success="handleSuccess" />
  </template>
  
  <script setup>
  import LoginForm from '../components/LoginForm.vue'
  import Dashboard from './Dashboard.vue'
  import { ref } from 'vue'
  
  const handleSuccess = () => {
    window.location.reload()
  }
  </script>
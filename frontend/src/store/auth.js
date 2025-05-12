import { defineStore } from 'pinia'
import axios from 'axios'
import Cookies from 'js-cookie'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: Cookies.get('token') || null,
    user: null,
  }),
  actions: {
    async login(username, password) {
      try {
        const form = new FormData()
        form.append('username', username)
        form.append('password', password)

        const response = await axios.post('http://127.0.0.1:8000/token', form)

        this.token = response.data.access_token
        Cookies.set('token', this.token, { expires: 1 / 24 }) // 1 hora
        await this.fetchUser()
        return true
      } catch (err) {
        console.log(err)
        return false
      }
    },
    async fetchUser() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/user', {
          headers: { Authorization: `Bearer ${this.token}` }
        })
        this.user = response.data
      } catch (err) {
        this.logout()
      }
    },
    logout() {
      this.token = null
      this.user = null
      Cookies.remove('token')
    },
    isAuthenticated() {
      return !!this.token
    },
    async register(username, email, password) {
      try {
        const newUser = {
          username,
          email,
          password
        }
        await axios.put('http://127.0.0.1:8000/new_user', newUser)
        const form = new FormData()
        form.append('username', username)
        form.append('password', password)
    
        const response = await axios.post('http://127.0.0.1:8000/token', form)
    
        this.token = response.data.access_token
        Cookies.set('token', this.token, { expires: 1 / 24 }) // 1 hora
    
        await this.fetchUser()
        return true
      } catch (err) {
        console.error('Error en el registro:', err)
        return false
      }
    }
  }
})

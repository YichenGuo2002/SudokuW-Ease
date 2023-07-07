// stores/counter.js
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => {
    return { 
      name: null,
      id: null,
      email: null
     }
  },
  getters:{
    userObject(state){
        if(state.id && state.email){
            return{
                email:state.email,
                id:state.id,
                name:state.name
            }
        }
        else{
            return null
        }
    },
  },
  // could also be defined as
  // state: () => ({ count: 0 })
  actions: {
    defineName(name) {
      this.name = name
    },
    defineId(id){
      this.id = id
    },
    defineEmail(email){
      this.email = email
    },
  },
})
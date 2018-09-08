import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

global.router = new Router({
  hashbang: false,
  linkActiveClass: 'active',
  routes: [
    // {
    //   path: '/hello',
    //   name: 'hello',
    //   component: require('@/components/HelloWorld')
    // }
  ]
})

export default global.router

import VueRouter from 'vue-router'

import My from './components/my'
import Info from './components/my/Info'
import Home from './components/home'
import Help from './components/help'
import HelpPdf from './components/help/pdf'

const routes = [
  { path: '/', component: Home },
  { path: '/index', component: Home },

  { path: '/my', component: My },
  { path: '/info', component: Info },
  { path: '/help', component: Help },
  { path: '/pdf', component: HelpPdf },
]

const router = new VueRouter({
  mode: 'history',
  routes,
})

export default router

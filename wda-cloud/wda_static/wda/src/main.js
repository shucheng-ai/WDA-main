import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'

import Request from './requests'
import Router from './router'
import store from './store'
import i18n from './locales'

import {
  BackTop,
  Button,
  Breadcrumb,
  Card,
  Collapse,
  Divider,
  Dropdown,
  Empty,
  FormModel,
  Icon,
  Input,
  Layout,
  Menu,
  Modal,
  Pagination,
  Popover,
  Spin,
  Table,
  Tag,
  message,
} from 'ant-design-vue'
import '@/assets/css/base.css'

Vue.config.productionTip = false

const ConfigComponents = [
  BackTop,
  Button,
  Breadcrumb,
  Card,
  Collapse,
  Divider,
  Dropdown,
  Empty,
  FormModel,
  Icon,
  Input,
  Layout,
  Menu,
  Modal,
  Pagination,
  Popover,
  Spin,
  Table,
  Tag,
]

ConfigComponents.forEach((component) => {
  Vue.use(component)
})

Vue.use(VueRouter)

Vue.prototype.$message = message
Vue.prototype.$request = Request

let vue = new Vue({
  el: '#app',
  router: Router,
  store,
  i18n,
  render: (h) => h(App),
})

export default vue

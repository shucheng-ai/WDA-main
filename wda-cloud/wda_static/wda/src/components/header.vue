<template>
  <a-layout-header>
    <div style="position: relative;max-width: 1200px;margin: auto">
      <div
        style="display: inline-block;color: white;cursor: pointer;width: 76px;"
      >
        <a href="http://cloud.shucheng-ai.com">
          <img class="logo-img" src="@/assets/logo.png" alt="" srcset="" />
        </a>
      </div>

      <div
        style="margin-left: 120px; display: inline-block;vertical-align: top"
      >
        <ul class="menu">
          <li @click="jump('/', 1)" :class="activeKey === 1 ? 'active' : ''">
            {{ $t('menu.home') }}
          </li>
          <!-- <li v-if="type === 'home' && is_login"> -->
          <li @click="jump('/my', 2)" :class="activeKey === 2 ? 'active' : ''">
            {{ $t('menu.project') }}
          </li>
          <li
            @click="jump('/help', 3)"
            :class="activeKey === 3 ? 'active' : ''"
          >
            {{ $t('menu.help') }}
          </li>
        </ul>
      </div>

      <div style="position: absolute;top: 0;right: 20px">
        <a-dropdown style="margin-right: 20px;">
          <a class="ant-dropdown-link" @click="(e) => e.preventDefault()">
            <i class="language">
              <svg
                viewBox="0 0 24 24"
                focusable="false"
                width="1em"
                height="1em"
                fill="currentColor"
              >
                <path d="M0 0h24v24H0z" fill="none"></path>
                <path
                  d="M12.87 15.07l-2.54-2.51.03-.03c1.74-1.94 2.98-4.17 3.71-6.53H17V4h-7V2H8v2H1v1.99h11.17C11.5 7.92 10.44 9.75 9 11.35 8.07 10.32 7.3 9.19 6.69 8h-2c.73 1.63 1.73 3.17 2.98 4.56l-5.09 5.02L4 19l5-5 3.11 3.11.76-2.04zM18.5 10h-2L12 22h2l1.12-3h4.75L21 22h2l-4.5-12zm-2.62 7l1.62-4.33L19.12 17h-3.24z "
                ></path>
              </svg>
            </i>
          </a>
          <a-menu slot="overlay">
            <a-menu-item @click="setLang('zh-CN')">
              <a href="javascript:;">
                中文
              </a>
            </a-menu-item>
            <a-menu-item @click="setLang('en-US')">
              <a href="javascript:;">
                English
              </a>
            </a-menu-item>
          </a-menu>
        </a-dropdown>

        <a-dropdown style="margin:0 20px;" v-show="is_login">
          <a class="ant-dropdown-link" @click="(e) => e.preventDefault()">
            <a-icon type="user" />
            {{ user.name }}
            <a-icon type="down" />
          </a>
          <a-menu slot="overlay">
            <a-menu-item>
              <a href="http://auth.shucheng-ai.com/auth/password">
                {{ $t('btn.resetPassword') }}
              </a>
            </a-menu-item>
            <a-menu-item>
              <a @click="info">
                {{ $t('btn.info') }}
              </a>
            </a-menu-item>
            <a-menu-item>
              <a @click="logout">
                {{ $t('btn.logout') }}
              </a>
            </a-menu-item>
          </a-menu>
        </a-dropdown>

        <a-button v-show="!is_login">
          <a :href="login_url">
            {{ $t('menu.user.login') }}
          </a>
        </a-button>

        <Connect />
      </div>
    </div>
  </a-layout-header>
</template>

<script>
import Connect from './connect'
import { setCookie } from '@/utils/util'
export default {
  name: 'base-header',
  props: ['type'],
  components: {
    Connect,
  },
  mounted() {
    this.setActiveKey()
    let config = this.$request.get('/api/config')
    config.then((_config) => {
      let current = location.origin
      let login_url = `${_config.data.data.login_url}?target=${current}`
      let auth = this.$request.get('/api/auth')
      auth.then((_auth) => {
        if (!_auth.data.is_login) {
          this.login_url = login_url
        } else {
          this.is_login = true
          this.user = _auth.data.user
        }
      })
    })
  },
  methods: {
    logout() {
      // sessionid
      this.$request.get('/api/logout').then(() => {
        window.location.href = '/'
      })
    },
    info(){
      this.$router.push("/info")
    },
    jump(url, key) {
      if (url === '/my') {
        if (!this.is_login) {
          this.$message.error('You are not logged in. Please log in first！')
          return
        }
      }
      this.activeKey = key
      this.$router.push(url)
    },
    setActiveKey() {
      let { path } = this.$route
      if (path === '/') {
        this.activeKey = 1
      } else if (path === '/my') {
        this.activeKey = 2
      } else if (path === '/help' || path === '/pdf') {
        this.activeKey = 3
      }
    },
    setLang(lang) {
      this.$store.dispatch('setLang', lang)
      setCookie('lang', lang)
    },
  },
  data() {
    return {
      user: {},
      is_login: false,
      login_url: 'http://auth.shucheng-ai.com/auth/login',
      activeKey: 1,
    }
  },
}
</script>

<style lang="less" scoped>
@import '../assets/css/common.less';
.logo-img {
  width: 108px;
  height: auto;
}
.menu {
  text-align: right;
  overflow: hidden;
  li {
    font-size: 16px;
    cursor: pointer;
    float: left;
    padding: 0px 20px;
    &:hover {
      background: @primary-color;
    }
    a {
      color: #fff;
    }
  }
  li.active {
    background: @primary-color;
  }
  // color: #fff;
  color: #fff;
}
.back {
  color: #fbfbfb;
  // &:link,
  // &:visited {
  //   color: #fbfbfb;
  //   text-decoration: none;
  // }
  &:hover {
    color: @primary-color;
  }
}
.language {
  margin-right: 10px;
  font-size: 14px;
  color: #fff;
}
</style>

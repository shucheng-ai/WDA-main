<template>
  <a-layout id="components-layout-demo-top" class="layout">
    <Header type="home" />

    <section class="home">
      <div class="des">
        <div class="max1200">
          <h1 style="margin-bottom: 10px;margin-top: 10px;">{{ $t('project.title1') }}</h1>
          <p>
            {{ $t('project.des1') }}
          </p>
        </div>
      </div>
      <div class="content">
        <div class="max1200">
          <!-- <p class="title">1111</p> -->
          <div class="item-outer">
            <div class="item" v-for="(item, index) in data" :key="index" style="margin-right: 30px">
              <h1>{{ item.title }}</h1>
              <p style="line-height: 1.6em;">{{ item.data }}</p>
              <div v-if="item.disabled === 0" style="margin: 15px auto;">
                <a-button type="primary" class="mr10" @click="creatProejct(item.id)">
                  {{ $t('btn.createNew') }}
                </a-button>
                <a-button type="link" @click="openMadel(item.id)">
                  {{ $t('btn.details') }}
                </a-button>
              </div>
              <div v-else>
                {{ $t('txt.comingSoon') }}
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="des">
        <div class="max1200">
          <h1 style="margin-bottom: 10px">{{ $t('project.title2') }}</h1>
          <p>
            {{ $t('project.des2') }}
          </p>
        </div>
      </div>

      <div class="content">
        <div class="item-outer item-outer2 max1200">
          <div class="item">
            <h1>Demand Forecast</h1>
            <p>Build your own demand forecast machine learning models</p>
            <!-- <div>
                          <a-button type="primary" class="mr10">
                            {{ $t('btn.createNew') }}
                          </a-button>
                          <a-button type="link">
                            {{$t('btn.details')}}
                          </a-button>
                        </div> -->
            <div>
              {{ $t('txt.comingSoon') }}
            </div>
          </div>
        </div>
      </div>
    </section>
    <a-modal v-model="modal" :footer="null" :width="width" @cancel="cancel">
      <video :src="videoSrc" :width="videoWidth" controls ref="video"></video>
    </a-modal>
    <a-layout-footer style="margin-top: 50px;text-align: center">
      WDA CLOUD ©2020-2030 Shucheng
    </a-layout-footer>
  </a-layout>
</template>

<script>
import Header from '../header';
import { getCookie } from '@/utils/util';
export default {
  name: 'Home',
  components: {
    Header
  },
  mounted() {
    let config = this.$request.get('/api/config');
    config.then((_config) => {
      this.data.forEach((_demo) => {
        _demo.demo_url = _config.data.data.demo[_demo.id];
      });
    });
  },
  data() {
    return {
      data: [
        {
          title: 'Layout Design',
          data: 'A quick tool to generate storage layout automatically with this one click tool',
          disabled: 0,
          id: 'layout',
          demo_url: ''
        },
        {
          title: 'Resource Model',
          data: 'A quick benchmarking tool for labor and cost estimation',
          disabled: 0,
          id: 'resource_model',
          demo_url: ''
        },
        {
          title: 'Data Analytics',
          data: 'Analyzes product volumes to estimate space requirement',
          id: 'data_analytics',
          disabled: 0
        }
      ],
      width: 1200,
      videoWidth: 1150,
      modal: false,
      videoSrc: ''
    };
  },
  methods: {
    creatProejct(key) {
      let formdata = {
        type: key
      };
      let res = this.$request.post('/api/project', formdata);
      res.then((res) => {
        let project = res.data.data;
        let url;
        if (res.data.status !== 1) {
          let msg = res.data.msg ? res.data.msg : 'server error!';
          if (msg === 'permission denied') {
            msg = 'You are not logged in. Please log in first！';
          }
          this.$message.error(msg);
        } else {
          // this.$message.success('success.')

          if (key === 'layout') {
            url = project.layout_url;
            window.open(url, '_blank');
            // window.location.replace(url)
          } else if (key === 'resource_model') {
            url = project.resource_model_url;
            window.open(url, '_blank');
            // window.location.replace(url)
          } else if (key === 'data_analytics') {
            url = project.data_analytics_url;
            window.open(url, '_blank');
          }
        }
      });
    },
    openMadel(id) {
      if (id === 'resource_model') {
        return;
      }
      this.videoSrc =
        getCookie('lang') === 'zh-CN'
          ? require('@/assets/video/layout-Design_CH.mp4')
          : require('@/assets/video/layout-Design_EN.mp4');
      this.modal = true;
      this.$nextTick(function () {
        this.$refs.video.play();
      });
    },
    cancel() {
      this.$nextTick(function () {
        this.$refs.video.pause();
      });
    }
  }
};
</script>

<style>
body {
  background: #f0f2f5 !important;
}

#components-layout-demo-top .logo {
  width: 120px;
  height: 31px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px 24px 16px 0;
  float: left;
}

.title {
  font-size: 2em;
  font-weight: bold;
  color: black;
}

.sub-title {
  font-size: 1.2em;
}
</style>

<style lang="less" scoped>
@import '../../assets/css/common.less';

@padding: 50px;
@padding20: 20px;
.home {
  .max1200 {
    max-width: 1200px;
    margin: auto;
  }

  .mr10 {
    margin-right: 10px;
  }

  .des {
    padding: @padding @padding20 30px;
    background: #fff;

    h1 {
      font-weight: 400;
      font-style: normal;
      font-size: 24px;
      font-kerning: normal;
      color: @primary-color;
      // padding: 0px 0 16px 0;
    }

    p {
      color: #999;
      font-weight: 200;
      font-style: normal;
      font-size: 14px;
      line-height: 26px;
    }
  }

  .content {
    padding: 20px @padding20 10px;

    .title {
      margin: 0;
      font-size: 18px;
      font-weight: 200;
      line-height: 30px;
      color: #333;
    }

    .item-outer {
      display: flex;
      flex-wrap: wrap;
      padding: 20px 0;

      .item {
        border-radius: @border-radius-base;
        transition: all 0.2s linear;
        padding: 20px;
        background: #fff;
        width: 350px;
        // height: 180px;
        margin-right: 10px;
        margin-bottom: 10px;

        &:hover {
          z-index: 2;
          -webkit-box-shadow: 0 0px 10px rgba(0, 0, 0, 0.1);
          box-shadow: 0 0px 10px rgba(0, 0, 0, 0.1);
          -webkit-transform: translate3d(0, -1px, 0);
          transform: translate3d(0, -1px, 0);
        }

        h1 {
          font-size: 18px;
          color: #333;
        }

        p {
          margin: 16px 0;
          // font-size: 12px;
          color: #999999;
          line-height: 20px;
          font-weight: 200;
        }
      }
    }

    .item-outer2 {
      padding-top: 20px;
    }
  }
}
</style>

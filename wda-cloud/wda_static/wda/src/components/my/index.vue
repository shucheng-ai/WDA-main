<template>
  <a-layout id="components-layout-demo-top" class="layout">
    <Header type="project" />

    <section class="project">
      <a-modal title="Project Setting" :visible="showProjectSetting" @ok="setProject(null, 'save')" @cancel="setProject(null, 'cancel')">
        <a-form-model>
          <a-form-model-item layout="horizontal" label="name">
            <a-input placeholder="input project name" v-model="choose_project.name" />
          </a-form-model-item>
          <a-form-model-item layout="horizontal" label="description" style="margin-top: -20px">
            <a-input placeholder="input project description" v-model="choose_project.descript" />
          </a-form-model-item>
        </a-form-model>
      </a-modal>
      <a-modal title="Are you absolutely sure?" :visible="showProjectDelete" @ok="showProjectDelete = false" @cancel="showProjectDelete = false">
        You will delete project 'xxx'. The deletion can not be undone.
      </a-modal>
      <a-dropdown>
        <a-menu slot="overlay" @click="creatProejct">
          <a-menu-item key="layout2">
            Layout V2 Design
          </a-menu-item>
          <a-menu-item key="cad">
            CAD
          </a-menu-item>
          <a-menu-item key="layout">
            {{ $t('project.warehouseLayoutDesign') }}
          </a-menu-item>
          <a-menu-item key="resource_model">
            {{ $t('project.resourceModel') }}
          </a-menu-item>
          <a-menu-item key="data_analytics">
            {{ $t('project.dataAnalytics') }}
          </a-menu-item>
          <a-menu-item key="4" disabled>
            {{ $t('project.demandForecast') }}
          </a-menu-item>
        </a-menu>
        <a-button type="primary">
          <a-icon type="plus" />
          {{ $t('btn.createNew') }}
        </a-button>
      </a-dropdown>
      <div class="content">

        <a-collapse default-active-key="4" :bordered="false" expand-icon-position="right">
          <a-collapse-panel key="4" :style="customStyle">
            <div class="box-hd" slot="header">
              <h2 class="title">Layout V2 Design</h2>
            </div>
            <div class="item-outer" v-if="layout2_data.length">
              <div class="item" v-for="(item, index) in layout2_data" :key="index" @click="goto(item.layout2_url)">
                <div class="img-cover">
                  <span class="mark">{{ item.fileName }}</span>
                </div>
                <h1>
                  <a :href="item.layout2_url" target="_blank">{{ item.name }}</a>
                </h1>
                <p>{{ item.descript || '  ' }}</p>
                <div class="bottom">
                  <span>{{ item.update_date.slice(0, 10) }}</span>
                  <div>
                    <a-button @click.stop="setProject(item, 'copy')" type="link" icon="setting"></a-button>
                  </div>
                </div>
              </div>
            </div>
            <div class="nodata" v-else>
              <a-empty :image="simpleImage" />
            </div>
            <div style="display: block">
              <a-pagination v-model="layout2_page.page" :total="layout2_page.count" :pageSize="layout2_page.limit" @change="getLayout2" show-less-items />
            </div>
          </a-collapse-panel>
        </a-collapse>

        <a-collapse default-active-key="5" :bordered="false" expand-icon-position="right">
          <a-collapse-panel key="5" :style="customStyle">
            <div class="box-hd" slot="header">
              <h2 class="title">CAD</h2>
            </div>
            <div class="item-outer" v-if="cad_data.length">
              <div class="item" v-for="(item, index) in cad_data" :key="index" @click="goto(item.cad_url)">
                <div class="img-cover">
                  <span class="mark">{{ item.fileName }}</span>
                </div>
                <h1>
                  <a :href="item.cad_url" target="_blank">{{ item.name }}</a>
                </h1>
                <p>{{ item.descript || '  ' }}</p>
                <div class="bottom">
                  <span>{{ item.update_date.slice(0, 10) }}</span>
                  <div>
                    <a-button @click.stop="setProject(item, 'copy')" type="link" icon="setting"></a-button>
                  </div>
                </div>
              </div>
            </div>
            <div class="nodata" v-else>
              <a-empty :image="simpleImage" />
            </div>
            <div style="display: block">
              <a-pagination v-model="cad_page.page" :total="cad_page.count" :pageSize="cad_page.limit" @change="getCad" show-less-items />
            </div>
          </a-collapse-panel>
        </a-collapse>


        <a-collapse default-active-key="1" :bordered="false" expand-icon-position="right">
          <a-collapse-panel key="1" :style="customStyle">
            <div class="box-hd" slot="header">
              <h2 class="title">{{ $t('project.warehouseLayoutDesign') }}</h2>
            </div>
            <!-- <a-button type="primary" ghost @click.stop="addProject(1)" size="small" slot="extra">
            + Add project
          </a-button> -->
            <div class="item-outer" v-if="layout_data.length">
              <div class="item" v-for="(item, index) in layout_data" :key="index" @click="goto(item.layout_url)">
                <div class="img-cover">
                  <!--                  <img :src="item.background || noImg" alt="" />-->
                  <span class="mark">{{ item.fileName }}</span>
                </div>
                <h1>
                  <a :href="item.layout_url" target="_blank">{{ item.name }}</a>
                </h1>
                <p>{{ item.descript || '  ' }}</p>
                <div class="bottom">
                  <span>{{ item.update_date.slice(0, 10) }}</span>
                  <div>
                    <a-button @click.stop="setProject(item, 'copy')" type="link" icon="setting"></a-button>
                    <!--                    <a-button-->
                    <!--                      @click="showProjectDelete = true"-->
                    <!--                      type="link"-->
                    <!--                      icon="delete"-->
                    <!--                    ></a-button>-->
                  </div>
                </div>
              </div>
            </div>
            <div class="nodata" v-else>
              <a-empty :image="simpleImage" />
            </div>
            <div style="display: block">
              <a-pagination v-model="layout_page.page" :total="layout_page.count" :pageSize="layout_page.limit" @change="getLayout" show-less-items />
            </div>
          </a-collapse-panel>
        </a-collapse>

        <a-collapse default-active-key="2" :bordered="false" expand-icon-position="right">
          <a-collapse-panel key="2" :style="customStyle">
            <div class="box-hd" slot="header">
              <h2 class="title">
                {{ $t('project.resourceModel') }}
              </h2>
            </div>
            <!-- <a-button type="primary" ghost @click.stop="addProject(2)" size="small" slot="extra">
            + Add project
          </a-button> -->
            <div class="item-outer" v-if="resource_model_data.length">
              <div class="item" v-for="(item, index) in resource_model_data" :key="index" @click="goto(item.resource_model_url)">
                <!-- <div class="img-cover">
                <img :src="item.imgUrl || noImg" alt="" />
                <span class="mark">{{ item.fileName }}</span>
              </div> -->
                <h1>
                  <a :href="item.resource_model_url" target="_blank">{{
                    item.name
                  }}</a>
                </h1>
                <p>Status: {{ item.status || 'doing' }}</p>
                <!-- <p>Status: {{item.status}}</p> -->
                <div class="bottom">
                  <span>{{ item.update_date.slice(0, 10) }}</span>
                  <div>
                    <a-button type="link" icon="setting" @click.stop="setProject(item, 'copy')"></a-button>
                    <!--                    <a-button-->
                    <!--                      @click="showProjectDelete = true"-->
                    <!--                      type="link"-->
                    <!--                      icon="delete"-->
                    <!--                    ></a-button>-->
                  </div>
                </div>
              </div>
            </div>
            <div class="nodata" v-else>
              <a-empty :image="simpleImage" />
            </div>
            <div style="display: block">
              <a-pagination v-model="resource_model_page.page" :total="resource_model_page.count" :pageSize="resource_model_page.limit" @change="getResource" show-less-items />
            </div>
          </a-collapse-panel>
        </a-collapse>

        <a-collapse default-active-key="3" :bordered="false" expand-icon-position="right">
          <a-collapse-panel key="3" :style="customStyle">
            <div class="box-hd" slot="header">
              <h2 class="title"> {{ $t('project.dataAnalytics') }}</h2>
            </div>
            <div class="item-outer" v-if="data_analytics_data.length">
              <div class="item" v-for="(item, index) in data_analytics_data" :key="index" @click="goto(item.data_analytics_url)">
                <!-- <div class="img-cover">
                  <img :src="item.imgUrl || noImg" alt="" />
                  <span class="mark">{{ item.fileName }}</span>
                </div> -->
                <!-- <h1>{{ item.name }}</h1> -->
                <h1>
                  <a :href="item.data_analytics_url" target="_blank">{{
                    item.name
                  }}</a>
                </h1>
                <p>{{ item.descript || '   ' }}</p>
                <!-- <span>{{ item.update_date.slice(0, 10) }}</span> -->

                <div class="bottom">
                  <span>{{ item.update_date.slice(0, 10) }}</span>
                  <div>
                    <a-button type="link" icon="setting" @click.stop="setProject(item, 'copy')"></a-button>
                    <!--                    <a-button-->
                    <!--                      @click="showProjectDelete = true"-->
                    <!--                      type="link"-->
                    <!--                      icon="delete"-->
                    <!--                    ></a-button>-->
                  </div>
                </div>
              </div>
            </div>
            <div class="nodata" v-else>
              <a-empty :image="simpleImage" />
            </div>
            <div style="display: block">
              <a-pagination v-model="data_analytics_page.page" :total="data_analytics_page.count" :pageSize="data_analytics_page.limit" @change="getAnalytics" show-less-items />
            </div>
          </a-collapse-panel>
        </a-collapse>
      </div>
    </section>

    <a-layout-footer style="margin-top: 50px;text-align: center">
      WDA CLOUD ©2020-2030 Shucheng
    </a-layout-footer>
  </a-layout>
</template>

<script>
import Header from '../header';
import { Empty } from 'ant-design-vue';
export default {
  name: 'My',
  components: {
    Header
  },
  beforeCreate() {
    this.simpleImage = Empty.PRESENTED_IMAGE_SIMPLE;
  },
  mounted() {
    let config = this.$request.get('/api/config');
    config.then((_config) => {
      let current = location.origin;
      let login_url = `${_config.data.data.login_url}?target=${current}`;
      let auth = this.$request.get('/api/auth');
      auth.then((_auth) => {
        if (!_auth.data.is_login) {
          //    go to auth
          window.location.replace(login_url);
        } else {
          this.user = _auth.data.user;
          this.getProject(1, 'layout');
          this.getProject(1, 'layout2');
          this.getProject(1, 'resource_model');
          this.getProject(1, 'data_analytics');
          this.getProject(1, 'cad');
        }
      });
    });
  },
  methods: {
    goto(url) {
      window.open(url);
    },
    creatProejct(e) {
      let formdata = {
        type: e.key
      };
      let res = this.$request.post('/api/project', formdata);
      res.then((res) => {
        let project = res.data.data;
        let url;
        if (res.data.status !== 1) {
          let msg = res.data.msg ? res.data.msg : 'server error!';
          this.$message.error(msg);
        } else {
          this.$message.success('success.');
          if (e.key === 'layout') {
            url = project.layout_url;
            window.open(url, '_blank');
            this.getLayout(1);
          } else if (e.key === 'layout2') {
            url = project.layout2_url;
            window.open(url, '_blank');
            this.getLayout2(1);
          } else if (e.key === 'resource_model') {
            url = project.resource_model_url;
            window.open(url, '_blank');
            this.getResource(1);
          } else if (e.key === 'data_analytics') {
            url = project.data_analytics_url;
            window.open(url, '_blank');
            this.getAnalytics(1);
          } else if (e.key === 'cad') {
          url = project.cad_url;
            window.open(url, '_blank');
            this.getCad(1);
        }
        }
      });
    },
    getProject(page, type) {
      page = page ? page : 1;
      let data = this.$request.get(`/api/project?type=${type}&page=${page}`);
      data.then((d) => {
        if (type === 'layout') {
          this.layout_data = d.data.data.project_list.data;
          this.layout_page = d.data.data.project_list.info;
        } else if (type === 'layout2') {
          this.layout2_data = d.data.data.project_list.data;
          this.layout2_page = d.data.data.project_list.info;
        }else if (type === 'resource_model') {
          this.resource_model_data = d.data.data.project_list.data;
          this.resource_model_page = d.data.data.project_list.info;
        } else if (type === 'data_analytics') {
          this.data_analytics_data = d.data.data.project_list.data;
          this.data_analytics_page = d.data.data.project_list.info;
        }else if (type === 'cad') {
          this.cad_data = d.data.data.project_list.data;
          this.cad_page = d.data.data.project_list.info;
        }
      });
    },
    getLayout(page) {
      this.getProject(page, 'layout');
    },
    getLayout2(page) {
      this.getProject(page, 'layout2');
    },
    getCad(page) {
      this.getProject(page, 'cad');
    },
    getResource(page) {
      this.getProject(page, 'resource_model');
    },
    getAnalytics(page) {
      this.getProject(page, 'data_analytics');
    },
    setProject(project, type) {
      console.log(project, type);
      if (type === 'copy') {
        this.choose_project = {
          id: project.id,
          name: project.name,
          descript: project.descript
        };
        this.showProjectSetting = true;
      } else if (type === 'save') {
        this.$request.put('/api/project', this.choose_project).then(() => {
          this.showProjectSetting = false;
          this.layout_data.forEach((item) => {
            if (item.id === this.choose_project.id) {
              item.name = this.choose_project.name;
              item.descript = this.choose_project.descript;
            }
          });
          this.resource_model_data.forEach((item) => {
            if (item.id === this.choose_project.id) {
              item.name = this.choose_project.name;
              item.descript = this.choose_project.descript;
            }
          });
        });
      } else {
        this.showProjectSetting = false;
      }
    }
  },
  data() {
    return {
      text: 'xxx',
      data: [],
      layout_data: [],
      layout_page: {
        page: 1,
        limit: 10,
        count: 0
      },
      layout2_data: [],
      layout2_page: {
        page: 1,
        limit: 10,
        count: 0
      },
      cad_data: [],
      cad_page: {
        page: 1,
        limit: 10,
        count: 0
      },
      resource_model_data: [],
      resource_model_page: {
        page: 1,
        limit: 10,
        count: 0
      },
      data_analytics_data: [],
      data_analytics_page: {
        page: 1,
        limit: 10,
        count: 0
      },
      user: {
        name: '',
        uid: -1
      },
      choose_project: {
        id: null,
        name: '',
        descript: ''
      },
      showProjectSetting: false,
      showProjectDelete: false,
      noImg: require('@/assets/img/nodata.png'),
      customStyle:
        'background: #fff;border-radius: 15px;margin-bottom: 24px;border: 0;overflow: hidden'
    };
  }
};
</script>

<style lang="less" scoped>
.project {
  width: 100%;
  padding: 20px;
  max-width: 1200px;
  margin: auto;
  .create-project {
    margin: 10px 0;
    // display: flex;
    // justify-content: space-between;
  }
  .content {
    margin-top: 20px;
    .box-hd {
      position: relative;
      // height: 58px;
      -webkit-font-smoothing: antialiased;
      .title {
        margin: 0;
        font-size: 18px;
        font-weight: 200;
        line-height: 30px;
        color: #333;
      }
    }
    .item-outer {
      padding: 20px 0;
      display: flex;
      flex-wrap: wrap;
      .item {
        cursor: pointer;
        border-radius: @border-radius-base;
        width: 240px;
        margin: 0 5px 10px;
        transition: all 0.2s linear;
        padding: 10px 10px;
        background: #f3f3f3;
        &:hover {
          z-index: 2;
          -webkit-box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
          box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
          -webkit-transform: translate3d(0, -2px, 0);
          transform: translate3d(0, -2px, 0);
        }
        h1 {
          // text-align: center;
          font-weight: 200;
          padding: 10px 0 0px;
          font-size: 14px;
          // color: #333;
        }
        p {
          font-weight: 200;
        }
        .img-cover {
          width: 220px;
          position: relative;
          img {
            background: #fff;
            width: 100%;
            height: auto;
          }
          .mark {
            display: inline-block;
            position: absolute;
            color: #ccc;
            bottom: 5px;
            right: 5px;
            font-weight: 200;
          }
        }
        .bottom {
          font-size: 12px;
          font-weight: 200;
          // color: #333;
          display: flex;
          align-items: center;
          justify-content: space-between;
        }
      }
    }
    .nodata {
      display: flex;
      width: 100%;
      justify-content: center;
    }
  }
}
</style>

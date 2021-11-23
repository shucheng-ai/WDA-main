<template>
  <div>
    <Header type="help" />
    <div class="contentStyle">
      <p :style="pStyle">{{ $t('txt.helpCenter') }}</p>
      <table style="width: 100%;margin-top: 10px">
        <thead class="ant-table-thead">
          <tr>
            <th
              class="ant-table-column-has-actions ant-table-column-has-sorters"
            >
              <div class="ant-table-column-sorters">
                {{ $t('txt.documnetName') }}
              </div>
            </th>
            <th
              class="ant-table-column-has-actions ant-table-column-has-sorters"
            >
              <div class="ant-table-column-sorters">
                {{ $t('txt.view') }}
              </div>
            </th>
            <th
              class="ant-table-column-has-actions ant-table-column-has-sorters"
            >
              <div class="ant-table-column-sorters">
                {{ $t('txt.download') }}
              </div>
            </th>
          </tr>
        </thead>
        <tbody class="ant-table-tbody" ref="tbody">
          <tr
            class="ant-table-row ant-table-row-level-0"
            :value="item.id"
            :key="item.id"
            v-for="item in data"
          >
            <td>
              <a-button type="link">
                <a :href="item.pdf_url" target="_blank">
                  {{ item.name }}
                </a>
              </a-button>
            </td>
            <td>
              <a-button type="link">
                <a :href="item.pdf_url" target="_blank">
                  {{ $t('btn.view') }}
                </a>
              </a-button>
            </td>
            <td>
              <a-button type="link">
                <a :href="item.url" target="_blank">
                  {{ $t('btn.download') }}
                </a>
              </a-button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!-- <a-card title="帮助中心" style="max-width: 1200px;margin: 20px auto;">
      <table style="width: 100%">
        <thead class="ant-table-thead">
          <tr>
            <th
              class="ant-table-column-has-actions ant-table-column-has-sorters"
            >
              <div class="ant-table-column-sorters">
                文档名称
              </div>
            </th>
            <th
              class="ant-table-column-has-actions ant-table-column-has-sorters"
            >
              <div class="ant-table-column-sorters">
                在线查看
              </div>
            </th>
            <th
              class="ant-table-column-has-actions ant-table-column-has-sorters"
            >
              <div class="ant-table-column-sorters">
                下载文档
              </div>
            </th>
          </tr>
        </thead>
        <tbody class="ant-table-tbody" ref="tbody">
          <tr
            class="ant-table-row ant-table-row-level-0"
            :value="item.id"
            :key="item.id"
            v-for="item in data"
          >
            <td>
              <a-button type="link">
                <a :href="item.pdf_url" target="_blank">
                  {{ item.name }}
                </a>
              </a-button>
            </td>
            <td>
              <a-button type="link">
                <a :href="item.pdf_url" target="_blank">
                  查看
                </a>
              </a-button>
            </td>
            <td>
              <a-button type="link">
                <a :href="item.url" target="_blank">
                  下载
                </a>
              </a-button>
            </td>
          </tr>
        </tbody>
      </table>
    </a-card> -->
  </div>
</template>

<script>
import Header from '../header'

export default {
  name: 'help-index',
  components: {
    Header,
  },
  methods: {
    view(item) {
      console.log(item)
    },
  },
  mounted() {
    this.$request.get('/api/help').then((res) => {
      console.log(res.data)
      this.data = res.data.data
    })
  },
  data() {
    return {
      data: [],
      pStyle: {
        marginTop: '10px',
        fontSize: '18px',
        lineHeight: '30px',
        marginBottom: '5px',
        fontWeight: '200',
      },
    }
  },
}
</script>

<style lang="less">
@import '../../assets/css/common.less';
.contentStyle {
  max-width: 1200px;
  background: #fff;
  padding: 5px 10px 10px 20px;
  margin: 20px auto;
  border-radius: @border-radius-base;
}
.ant-table-column-sorters {
  font-weight: normal;
}
</style>

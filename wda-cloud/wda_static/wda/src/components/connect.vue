<template>
  <div style="position: fixed;right: 50px;bottom: 30px;z-index: 99">
    <a-popover>
      <template slot="content">
        <p style="font-size: 0.9em;">
          {{ $t('txt.tel') }}：(+86) 139 8045 2039
        </p>
        <p style="font-size: 0.9em;">
          {{ $t('txt.email') }}：business@shucheng.ai
        </p>
        <div
          style="font-size: 0.9em;margin-top:5px;line-height: 130px;height: 130px;display: flex;flex-direction: row;"
        >
          <div style="flex: auto;line-height:100%;vertical-align: top;">
            {{ $t('txt.weChat') }}：
          </div>
          <div style="flex: auto;vertical-align: top;padding-bottom: 30px">
            <img :src="wx" alt="weixin" width="120" height="120" />
          </div>
        </div>
      </template>
      <a-button type="dashed">
        <a-icon type="wechat" />
        {{ $t('txt.contactUs') }}
      </a-button>
    </a-popover>
  </div>
</template>

<script>
import wx from '../assets/img/wx.jpeg'

export default {
  name: 'connect',
  data() {
    return {
      wx: wx,
    }
  },
}
</script>

<style scoped></style>

import antd from 'ant-design-vue/es/locale-provider/zh_CN'
import momentCN from 'moment/locale/zh-cn'

const components = {
  antLocale: antd,
  momentName: 'zh-cn',
  momentLocale: momentCN,
}

const locale = {
  message: '-',
  'menu.home': '主页',
  'menu.project': '项目',
  'menu.help': '帮助',
  'menu.user.login': '登录',
  'menu.user.signup': '注册',
  'project.warehouseLayoutDesign': '布局规划',
  'project.resourceModel': '资源计划',
  'project.dataAnalytics': '数据分析',
  'project.warehouseDesign': '仓库设计',
  'project.demandForecast': '需求预测',
  'project.logisticsProcessOptimization': '物流流程优化',
  'project.supplyChainPlanning': '供应链计划',
  'project.report': '报告',
  'btn.createNew': '新建项目',
  'btn.details': '工具简介',
  'btn.setting': '个人设置',
  'btn.logout': '退出',
  'btn.detail': 'Detail',
  'btn.download': '下载',
  'btn.language': '语言',
  'btn.resetPassword': '重置密码',
  'btn.info': 'Info',
  'btn.view': '查看',

  'project.laborDemand': '劳动力',
  'project.machineDemand': '设备',
  'project.title1': '仓储全生命周期决策管理',
  'project.des1':
    '在仓储领域，实现全生命周期的数字化与智能化决策管理：从规划阶段的数据分析、布局规划，到运营阶段的诊断、优化。',
  'project.title2': '供应链计划管理',
  'project.des2':
    '考虑整体供应链全生命周期的特征，并以模型和算法驱动实现从需求预测、库存规划到配送计划的数字化决策。',
  'project.demandForecastDes':
    '建立匹配场景需求的机器学习模型，实现需求精确预测和计划',

  'txt.comingSoon': '即将上线',
  'txt.contactUs': '联系我们',
  'txt.tel': '电话',
  'txt.email': '邮箱',
  'txt.weChat': '微信',
  'txt.helpCenter': '帮助中心',
  'txt.documnetName': '文档名称',
  'txt.view': '在线查看',
  'txt.download': '下载文档',
}

export default {
  ...components,
  ...locale,
}

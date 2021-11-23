import antdEnUS from 'ant-design-vue/es/locale-provider/en_US'
import momentEU from 'moment/locale/eu'

const components = {
  antLocale: antdEnUS,
  momentName: 'eu',
  momentLocale: momentEU,
}

const locale = {
  message: '-',
  'menu.home': 'Home',
  'menu.project': 'Workspace',
  'menu.help': 'Help',
  'menu.user.login': 'Login',
  'menu.user.signup': 'Sign up',
  'project.warehouseLayoutDesign': 'Layout Design',
  'project.resourceModel': 'Resource Model',
  'project.dataAnalytics': 'Data Analytics',
  'project.warehouseDesign': 'Warehouse Design',
  'project.demandForecast': 'Demand Forecast',
  'project.logisticsProcessOptimization': 'Logistics Process Optimization',
  'project.supplyChainPlanning': 'Supply Chain Planning',
  'project.report': 'Report',
  'btn.createNew': 'Create New',
  'btn.details': 'Details',
  'btn.setting': 'setting',
  'btn.logout': 'Logout',
  'btn.info': 'Info',
  'btn.detail': 'Detail',
  'btn.download': 'download',
  'btn.language': 'Language',
  'btn.resetPassword': 'Reset Password',
  'btn.view': 'View',

  'project.laborDemand': 'Labor Demand',
  'project.machineDemand': 'Machine Demand',
  'project.title1': 'Warehouse lifecycle',
  'project.des1':
    'Digitalized and automated process with consideration of holistic warehouse lifecycle from data analytics, layout design, warehouse diagnostics to optimization.',
  'project.title2': 'Supply Chain Planning',
  'project.des2':
    'Models and algorithms with consideration of holistic SCP lifecycle from forecasting, inventory planning to distribution demand planning.',
  'project.demandForecastDes':
    'Build your own demand forecast machine learning models',

  'txt.comingSoon': 'Coming soon',
  'txt.contactUs': 'Contact Us',
  'txt.tel': 'Tel',
  'txt.email': 'E-mail',
  'txt.weChat': 'WeChat',
  'txt.helpCenter': 'Help Center',
  'txt.documnetName': 'Document Name',
  'txt.view': 'View Online',
  'txt.download': 'Document Download',

  'layouts.usermenu.dialog.title': 'Message',
  'layouts.usermenu.dialog.content': 'Do you really log-out.',

  'app.setting.pagestyle': 'Page style setting',
  'app.setting.pagestyle.light': 'Light style',
  'app.setting.pagestyle.dark': 'Dark style',
  'app.setting.pagestyle.realdark': 'RealDark style',
  'app.setting.themecolor': 'Theme Color',
  'app.setting.navigationmode': 'Navigation Mode',
  'app.setting.content-width': 'Content Width',
  'app.setting.fixedheader': 'Fixed Header',
  'app.setting.fixedsidebar': 'Fixed Sidebar',
  'app.setting.sidemenu': 'Side Menu Layout',
  'app.setting.topmenu': 'Top Menu Layout',
  'app.setting.content-width.fixed': 'Fixed',
  'app.setting.content-width.fluid': 'Fluid',
  'app.setting.othersettings': 'Other Settings',
  'app.setting.weakmode': 'Weak Mode',
  'app.setting.copy': 'Copy Setting',
  'app.setting.loading': 'Loading theme',
  'app.setting.copyinfo':
    'copy success，please replace defaultSettings in src/models/setting.js',
  'app.setting.production.hint':
    'Setting panel shows in development environment only, please manually modify',
}

export default {
  ...components,
  ...locale,
}

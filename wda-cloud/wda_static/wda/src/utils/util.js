// 设置cookie
export function setCookie(name, value) {
  // domain=.shucheng-ai.com;写入cookie到主域 子域名都可用    path=/表示本站全部路径都可使用
  const cookie = `${name}=${value};domain=${process.env.VUE_APP_DOMAIN};path=/`
  console.log(cookie)
  document.cookie = cookie
  console.log('set cookie ok')
}
// 获取cookie
export function getCookie(name) {
  var reg = RegExp(name + '=([^;]+)')
  var arr = document.cookie.match(reg)
  if (arr) {
    return arr[1]
  } else {
    return ''
  }
}
// 删除cookie
export function delCookie(name) {
  setCookie(name, null, -1)
}

# 初始部署
```
git clone http://gitlab.shucheng-ai.com/layout/main.git
git submodule init
git submodule update
国内 git submodule foreach bash build.sh
国外 git submodule foreach bash build.sh en
```
# 检查更新
```
git pull
git submodule update 
git submodule foreach bash update.sh
```
# 运行
```
本地部署 bash run.sh
本地测试 bash run.sh dev
服务器部署 bash run.sh nginx
```
# 提交更新
对其中一个子项目进行的修改，如core，并提交到gitlab上
```
git add -A
git commit -m "xxx"
git fetch origin
git merge origin/master
git push
```

## nginx 配置

```
端口：38088
账号：shucheng 
密码：Shucheng@2021Shanghai
```
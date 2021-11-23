### clone和重命名

``` 
git clone http://gitlab.shucheng-ai.com/wda/beaver-cloud.git

mv beaver-cloud wda-cloud
```

**项目结构**

``` 
..|
  -- wda-cloud
  -- wda-auth
  -- wda-auth-decorators
```

### 1.生产环境

#### 1.1 依赖安装

``` 
bash build.sh
```

#### 1.2 运行

``` 
bash start.sh
```

#### 1.3 配置信息

生产环境`bash start.sh`启动后会自动开启数据库、server

- docker 网关: 172.17.0.1
- server监听端口：8083
- PostgreSQL数据库监听端口：15433

### 2. 开发环境

#### 2.1 开发环境：server

##### 2.1.1 依赖安装

``` 
bash start.sh
```

#### 2.1.2 local_config.py

如需修改配置文件则在 `wda_server/config` 目录下添加 `local_config.py` 文件。

``` 
# 修改本地测试登录连接
WDA_AUTH_URL = 'http://127.0.0.1:8081'
WDA_AUTH_LOGIN_URL = 'http://127.0.0.1:8081/auth/login'

# 修改本地测试layout连接
LAYOUT_URL = 'http://127.0.0.1:8085'
LAYOUT_PROJECT_URL = 'http://127.0.0.1:8085/api/check_project?project_id='

# 开发测试project limit 限制
PROJECT_LIMIT = 1000

# 本地测试domain
DOMAIN = "127.0.0.1"
```

#### 2.1.3 运行

``` 
bash start.sh dev
```

#### 2.2 开发环境：static

##### 2.2.1 依赖安装

``` 
bash start.sh

cd wda_static/wda

// npm 模式
npm install

// docker 模式
bash npm_install.sh
```

#### 2.2.2 local.config.js

通过添加 `wda_static/wda/local.config.js` 文件配置修改本地测试server连接

``` 
let localConfig = {
    api: 'http://127.0.0.1:8083/',
    // api: 'http://172.17.0.18083/', // docker 网关
    // api: 'http://testcloud.shucheng-ai.com/',
}

module.exports = localConfig;
```

#### 2.2.3 运行

``` 
bash start.sh 

// npm 模式
cd wda_static/wda
npm run serve

// docker 模式
cd wda_static
bash start.sh
```

#### 2.2.3 编译

```
// npm 模式
cd wda_static/wda
npm run build 

// docker 模式
cd wda_static
bash build.sh
```


#### other

``` 

# reset network
docker system prune

wda-auth 
network: 172.17.0.1
postgresql:15432
server: 8081 
nginx: 39992

wda-cloud postgresql:
network: 172.17.0.1
postgresql:15433
server: 8083
```
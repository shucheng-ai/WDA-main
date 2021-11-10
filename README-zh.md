# Warehouse Design Automation
官网: [IAILabs](http://www.iailabs.com/)

用户手册:

Lisence: [Apache 2.0](https://github.com/shucheng-ai/WDA-main/blob/main/LICENSE)

## Abstract
WDA是一款仓库货架智能设计工具，支持读入dwg及dxf格式的设计图纸，并在智能识别出的仓间中自动生成货架排列。WDA支持多种导出格式，并提供仓间2D及3D可视化。

## 功能特性:
- 仓间解析 - 根据导入的CAD文件，解析并识别出包含墙、立柱、门、消防栓、楼梯障碍物等空间信息
- 用户标注 - 可在解析的基础上对图层内容和空间进行自行规划
- 自定义货架 = 支持的货架模型包括横梁式货架（APR Single/Double Deep）、隔板货架（Carton Shelving）、地堆（Pallet Stack），并可对尺寸参数进行自行设置
- 规划逻辑 - 货架规划可实现避开障碍物、对其货架通道、自定义货架方向等逻辑
- 可视化 - 规划结果以2D及3D的方式呈现


## 安装
```
git clone http://gitlab.shucheng-ai.com/layout/main.git
git submodule init
git submodule update
git submodule foreach bash build.sh
```
## 项目结构
```
.
├── 3d                    
├── cad
├── core
├── database
├── dwg2dxf
├── nginx  
├── tools
├── update
├── wda-auth-decorators      
├── wda-cloud                   
├── web                    
├── web-server                   
└── ...
```
## 运行
本地部署 
```
bash run.sh
```
开发者模式
```
bash run.sh dev
```
服务器部署 
```
bash run.sh nginx
```

### Nginx配置

```
端口：38088
账号：shucheng 
密码：Shucheng@2021Shanghai
```
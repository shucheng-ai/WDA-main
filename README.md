# Warehouse Design Automation
Website: [IAILabs](http://www.iailabs.com/)

User manual:

Lisence: [Apache 2.0](https://github.com/shucheng-ai/WDA-main/blob/main/LICENSE)

## Abstract
An AI tool to generate warehouse layout design in 2D and 3D format. WDA can interpret warehouse structures from CAD drawings, and generate layout designs of inventory.

#### Core feature of WDA:
- CAD interpretation - Identify wall, pillar, door, fire hydrant and other obstacles from the warehouse CAD drawing
- Customize storage type - APR/Double Deep | Pallet Stacking | Carton Shelving types are available and enable customization
- Storage Design - Algorithm avoid obstacles and place the racks with max capacity
- Visualization - Present layout design in 2D CAD drawing and 3D model.

## Installation
```
git clone http://gitlab.shucheng-ai.com/layout/main.git
git submodule init
git submodule update
git submodule foreach bash build.sh en
```
## Project Structure with Submodules
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
## Run
run server
```
bash run.sh
```
developer mode
```
bash run.sh dev
```
nginx mode
```
bash run.sh nginx
```
### Nginx Configuration

```
port：38088
user：shucheng 
password：Shucheng@2021Shanghai
```



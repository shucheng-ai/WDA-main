# Warehouse Design Automation

[EN](https://github.com/shucheng-ai/WDA-main/blob/main/README.md) | [中文](https://github.com/shucheng-ai/WDA-main/blob/main/README-zh.md)

Website: [IAILabs](http://www.iailabs.com/)

Documentation: [User manual](http://www.iailabs.com/manual)

Frequently asked questions: link to be continued

Lisence: [Apache 2.0](https://github.com/shucheng-ai/WDA-main/blob/main/LICENSE)

## Abstract
An AI tool to generate warehouse layout design in 2D and 3D format. WDA can interpret warehouse structures from CAD drawings, and generate layout designs of inventory.
To quickly try WDA use our [demo server](http://67.225.180.60:38088/) which comes with all the features. 
- admin:demo
- pass:demo

### How to Use
The layout design process contains 4 steps:
- Upload a CAD file; both DXF and DWG are acceptable.
- Chose a storage type that is preconfigured with standard specification.
- Drag and drop the storage into a selected region.
- Download the optimized storage layout design and edit in CAD software. Preview in 3D.
   
### Core features of WDA
- CAD interpretation - Identify wall, pillar, door, fire hydrant and other obstacles from the warehouse CAD drawing.
- Customize storage type - APR/Double Deep | Pallet Stacking | Carton Shelving types are available and enable customization.
- Storage Design - Algorithm avoid obstacles and place the racks with max capacity.
- Visualization - Present layout design in 2D CAD drawing and 3D model.


## Installation
We use docker for most of our submodules, the easiest and quickest way to setup WDA is to start at WDA-main and use the docker images we provide. 

**Please make sure [Docker](https://docs.docker.com/get-docker/) is correctly installed.**

Build and update every submodule. (Building dockers for submodules might take a while)
```
git clone https://github.com/shucheng-ai/WDA-main.git
cd WDA-main
git submodule init
git submodule update
git submodule foreach bash build.sh en 
git submodule foreach bash update.sh
```
Note that /database has to be build seperately.
```
cd database
bash build.sh
```
## Project Structure with Submodules
```
.
├── 3d                     # 3d warehouse visualization         
├── cad                    # cad interpretation
├── core                   # warehouse layout design
├── database               # warehouse database
├── dwg2dxf                # convert dwg to dxf format
├── nginx                  # nginx container
├── tools                  # 2d warehouse visualization
├── update                 
├── wda-auth-decorators       
├── wda-cloud                 
├── web                    # frontend 
├── web-server             # web server
└── ...
```
## Run
```
bash run.sh nginx
```
## Nginx Configuration
### Download the latest nginx image
```
docker pull nginx:latest
```
### start container
```
cd nginx
docker-compose up -d
```
### user/password
```
port：38088
user：shucheng 
password：Shucheng@2021Shanghai
```

## Feedback
Questions, bug reports, feature requests, etc. at GitHub Issues:
https://github.com/shucheng-ai/WDA-main/issues


## Contact

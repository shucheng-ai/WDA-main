#!/bin/bash

cd wda_server
pwd
docker build -t wda/cloud .

cd ..
cd wda_static
pwd
docker build -t wda/node14 .

cd ..
cd wda_model
pwd
docker build -t wda/db .

echo "build ok"
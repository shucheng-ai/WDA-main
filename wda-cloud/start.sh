#!/bin/bash

work_path=$(cd "$(dirname "$0")";pwd)
mode="product"
app="all"

echo $work_path
echo "product" > "$work_path/wda_server/server.conf"
echo "product" > "$work_path/wda_static/static.conf"

if [ "$1" == "dev" ]
then
  echo "dev mode"
  cd wda_model
  docker-compose -f docker-compose.dev.yml up -d
  cd ..
  echo "start dev db ok"
  echo "dev" > "$work_path/wda_server/server.conf"
  echo "dev" > "$work_path/wda_static/static.conf"
  docker-compose -f docker-compose.dev.yml up
else
  echo "product mode"
  cd wda_model
  docker-compose up -d
  cd ..
  echo "start wda db ok"
  docker-compose up -d
  echo "start wda cloud ok"
fi




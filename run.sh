if [ "$1" == "nginx" ]
then
    echo "running nginx"
    docker-compose -f nginx/docker-compose.yml up -d
fi

cd database
bash run.sh
cd ..
cd dwg2dxf
bash run.sh
cd ..
cd web-server
bash run.sh $1

echo "upodateing 1.0"
if [ "$1" == "en" ]
then
  echo "build en docker:"
  docker build -f Dockerfile.en -t cyborg/webserver:1.0 . --no-cache
else
  echo "build cn docker:"
  docker build -f Dockerfile.cn -t cyborg/webserver:1.0 . --no-cache
fi
docker tag cyborg/webserver:1.0 cyborg/webserver:latest

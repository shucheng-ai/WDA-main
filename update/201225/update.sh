echo "building cad"
if [ "$1" == "en" ]
then
  echo "build en docker:"
  docker build -f Dockerfile.en -t cyborg/webserver . --no-cache
else
  echo "build cn docker:"
  docker build -f Dockerfile.cn -t cyborg/webserver . --no-cache
fi

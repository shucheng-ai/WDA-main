# install all
# bash npm_install.sh
# install new lib
# bash npm_install.sh new_name

cd wda

if [ "$1" ]
then
  echo "npm install $1"
  docker-compose run node npm install "$1" --save
else
  echo "npm install"
  docker-compose run node npm install
fi

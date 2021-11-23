rm -rf ./build
rm -rf ./dist
rm -rf ./wda_decorators.egg-info

pip3 uninstall wda_decorators -y

python3 setup.py build

python3 setup.py install

#!/usr/bin/env python3
# coding:utf-8
"""
python3 setup.py bdist_egg
python3 setup.py build
python3 setup.py install
"""
from setuptools import setup, find_packages

setup(
    name="wda_decorators",
    version="0.0.1",
    keywords=("pip"),
    description="wda auth decorators",
    long_description="wda auth decorators for python",
    license="MIT Licence",
    url="http://shucheng.ai",
    author="wangpeifeng",
    author_email="root@arthurnone.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[]
)

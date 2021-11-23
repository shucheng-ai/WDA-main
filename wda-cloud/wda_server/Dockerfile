FROM ubuntu:18.04
USER root
ENV DEBIAN_FRONTEND=noninteractive
ENV LANG C.UTF-8
RUN sed -i s@/archive.ubuntu.com/@/mirrors.ustc.edu.cn/@g /etc/apt/sources.list
RUN sed -i s@/security.ubuntu.com/@/mirrors.ustc.edu.cn/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install -y wget python3 python3-pip libpython3-dev curl vim rsync
RUN mkdir /workspace
COPY requirement.txt /workspace/requirement.txt
RUN pip3 install -i https://mirrors.aliyun.com/pypi/simple -r /workspace/requirement.txt
WORKDIR /root

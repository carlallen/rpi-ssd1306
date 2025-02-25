FROM python:3-slim-bookworm
RUN apt-get update && \
apt-get install -y \
apt-utils \
build-essential \
git \
gcc \
g++ \
make \
autoconf \
automake \
libtool \
libfreetype6-dev \
libjpeg-dev \
libsdl1.2-dev \
libportmidi-dev \
libsdl-ttf2.0-dev \
libsdl-mixer1.2-dev \
libsdl-image1.2-dev \
python3-rpi.gpio \
python3-pip \
procps && \
pip3 install setuptools
WORKDIR /usr/src/app
COPY ./requirements.txt ./
RUN CFLAGS="-fcommon" pip3 install -r requirements.txt
COPY . ./
CMD python3 main.py

FROM --platform=linux/amd64 ubuntu:22.04

RUN apt update -y
RUN apt upgrade -y
RUN apt install -y build-essential zlib1g-dev libsdl2-dev libasound2-dev perl python3 git ffmpeg

RUN mkdir /tools
RUN mkdir /data

WORKDIR /tools
RUN git clone https://github.com/julius-speech/julius.git
WORKDIR /tools/julius
RUN ./configure --enable-words-int
RUN make -j4
RUN make install

WORKDIR /tools
RUN git clone https://github.com/julius-speech/segmentation-kit.git
WORKDIR /tools/segmentation-kit
RUN mv segment_julius.pl segment_julius.pl.old
RUN sed -e 's/$juliusbin=".\/bin\/julius-4.3.1";/$juliusbin="julius";/' -e 's/$datadir = ".\/wav";/$datadir = "\/data";/' segment_julius.pl.old > segment_julius.pl

WORKDIR /

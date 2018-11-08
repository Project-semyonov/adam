#FROM python:3.6-jessie
FROM resin/raspberrypi3-python
ENV INITSYSTEM on
RUN apt update && apt upgrade -y && apt-get install gcc \
    python3 \
    python3-dev \
    python3-pip
#RUN apt-get install -y wget
#RUN apt-get install librasberrypi-bin -y
COPY / /root/
#COPY requirements.txt /
WORKDIR /root/
VOLUME ["/root/videos"]
RUN pip3 install -r requirements.txt
#RUN useradd --no-log-init -m -k -U camera
#USER camera
#COPY / /home/camera/
#WORKDIR /home/camera/
#VOLUME ["/home/camera/videos"]
#RUN pip install --user camera
#RUN pip install -r requirements.txt
#RUN pip3 install -e .
#CMD python3 source_files/myMotion.py

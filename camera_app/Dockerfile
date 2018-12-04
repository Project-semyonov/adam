FROM resin/raspberrypi3-python:3-slim
ENV INITSYSTEM on
RUN apt update && apt upgrade -y && apt-get install gcc g++ 
COPY / /root/
WORKDIR /root/
#RUN pip3 install -r requirements.txt
#RUN pip3 install -e .
#CMD python3 camera_app/source_files/myMotion.py

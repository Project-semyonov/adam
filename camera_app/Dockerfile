FROM resin/raspberrypi3-python
ENV INITSYSTEM on
RUN apt update && apt upgrade -y && apt-get install gcc g++ \
    python3 \
    python3-dev \
    python3-pip
COPY / /root/
WORKDIR /root/
RUN pip3 install -r requirements.txt
RUN pip3 install -e .
CMD python3 source_files/myMotion.py

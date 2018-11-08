FROM python:3.6
RUN apt update -y
RUN apt upgrade -y
#RUN apk add gcc-core libjpeg-devel zlib-devel
#RUN apk add --no-cache python3 && \
#    python3 -m ensurepip && \
#    python3-devel && \
#    rm -r /usr/lib/python*/ensurepip && \
#    pip3 install --upgrade pip setuptools && \
#    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
#    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
#    rm -r /root/.cache
ADD /source_files /camera_service
working_dir /camera_service
RUN pip3 install -r requirements.txt
#RUN pip3 install -e .
#CMD python3 source_files/myMotion.py

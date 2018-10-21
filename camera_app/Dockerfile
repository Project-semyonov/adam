FROM alpine:3.7
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache
ADD /source_files /
RUN pip3 install picamera
RUN pip3 install time
RUN pip3 install Pillow
RUN pip3 datetime
RUN pip3 install io
RUN pip3 install os
CMD python3 mymotion.py 

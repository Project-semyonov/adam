FROM python:3-ubuntu
COPY . /root/
WORKDIR /root/
ENTRYPOINT sh
RUN chmod u+x *.sh && pip3 install awscli && apk add ffmpeg \
            groff \
            less
COPY /main.sh /etc/periodic/15min/
COPY /mp4Deleter.sh /etc/periodic/hourly

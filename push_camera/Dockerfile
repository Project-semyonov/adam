FROM python:3-alpine
COPY . /root/
WORKDIR /root/
ENTRYPOINT sh
RUN chmod u+x *.sh && pip3 install awscli && apk add --no-cache bash \
            ffmpeg \
            groff \
            less
ENTRYPOINT bash
COPY /main.sh /etc/periodic/15min/
COPY /mp4Deleter.sh /etc/periodic/hourly

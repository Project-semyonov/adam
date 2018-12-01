FROM python:3-alpine
COPY . /root/
WORKDIR /root/
ENTRYPOINT sh
RUN apk add ffmpeg
COPY /converter.sh /etc/periodic/15min/
COPY /deleter.sh /etc/periodic/15min/
RUN chmod +x /etc/periodic/15min/*.sh
#RUN crontab delete-cron
#CMD crontab -l
CMD ['sh', 'crond']

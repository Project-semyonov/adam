FROM alpine
COPY . /root/
WORKDIR /root/
ENTRYPOINT sh
COPY /deleter.sh /etc/periodic/hourly/
COPY /converter.sh /etc/periodic/15min/
RUN chmod +x /etc/periodic/hourly/*.sh
RUN chmod +x /etc/periodic/15min/*.sh
#RUN crontab delete-cron
#CMD crontab -l
#CMD crond

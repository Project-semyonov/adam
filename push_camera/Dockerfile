FROM alpine
COPY . /root/
WORKDIR /root/
ENTRYPOINT sh
RUN crontab delete-cron
RUN crond
CMD crond

FROM alpine
COPY . /root/
WORKDIR /root/
ENTRYPOINT sh
RUN crontab delete-cron
CMD crontab -l
CMD crond

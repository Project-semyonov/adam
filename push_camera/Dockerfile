FROM python:3-alpine
COPY . /root/
WORKDIR /root/
ENTRYPOINT sh
RUN chmod u+x *.sh
RUN apk add ffmpeg \
            groff \
            less
RUN pip3 install awscli
COPY /main.sh /etc/periodic/15min/
#RUN chmod +x /etc/periodic/15min/*.sh
#RUN crontab delete-cron
#CMD crontab -l
#CMD ['sh', 'crond']

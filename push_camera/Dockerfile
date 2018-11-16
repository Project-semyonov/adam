FROM alpine
COPY / /root/
WORKDIR /root/
RUN mv delete-cron /etc/cron.d/ \
    && chmod 0644/etc/cron.d/delete-cron \ 
    && touch /var/log/cron.log
CMD cron && tail -f /var/log/cron.log

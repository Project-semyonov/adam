FROM hypriot/rpi-alpine-scratch
RUN apk update && \
apk upgrade && \
apk add bash && \
apk apt-get install -y python && \
apk apt-get install -y python-pip
ADD . .
#ADD ./example.py .
#ADD ./test.py .
CMD [ "python3", "./source/example.py"]

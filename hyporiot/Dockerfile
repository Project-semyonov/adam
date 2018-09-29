FROM hypriot/rpi-alpine-scratch
RUN apk update && \
apk upgrade && \
apk add bash && \
apk add --update \
	python3 \
	python \
	python-dev \
	python3-dev \
	py-pip \
	build-base \
&& pip install virtualenv \
&& rm -rf /var/cache/apk/*
ADD . .
#ADD ./example.py .
#ADD ./test.py .
CMD [ "python3", "./source/example.py"]

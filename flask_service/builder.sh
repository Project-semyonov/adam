#!/bin/bash
docker build -t semyonov4360/flask_endpoint:rpi . 
docker login -u semyonov4360
docker push semyonov4360/flask_endpoint:rpi

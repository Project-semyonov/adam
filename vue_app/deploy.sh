#!/bin/bash
docker build -t semyonov4360/vue_app:rpi . 
docker login -u semyonov4360 --password-stdin
docker push semyonov4360/vue_app:rpi


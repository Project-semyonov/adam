#!/bin/bash
docker build -t semyonov4360/test_python:rpi . 
docker login -u semyonov4360
docker push semyonov4360/test_python:rpi

#!/bin/bash
if [-e docker container ls -a | grep "camera_app"]
then
        docker restart camera_app
else
        docker build -t semyonov4360/camera_app . 
        docker run -d --privileged --name camera_app semyonov4360/camera_app
fi

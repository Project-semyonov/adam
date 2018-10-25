#!/bin/bash
if [ "$(docker container ls -a | grep -c "camera_app")" -ge 1 ]
then
        docker restart camera_app
else
        docker build -t semyonov4360/camera_app . 
        docker run -d --privileged --name camera_app semyonov4360/camera_app
fi

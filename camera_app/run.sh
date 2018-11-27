#!/bin/bash
if [ "$(docker container ls -a | grep -c "camera_app")" -ge 1 ]
then
        docker restart camera_app
else
        docker build -t semyonov4360/camera_app:rpi .
        docker run -d -v /home/pi/Videos/:/root/Videos/ --privileged -it --name camera_app semyonov4360/camera_app:rpi
fi

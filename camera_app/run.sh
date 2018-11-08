#!/bin/bash
if [ "$(docker container ls -a | grep -c "camera_app")" -ge 1 ]
then
        docker restart camera_app
else
        docker build -t semyonov4360/camera_app:rpi . 
        docker run -d --privileged -it --name camera_app semyonov4360/camera_app:rpi
        docker run -d -v /home/pi/Documents/adam/camera_app/videos/:/root/videos/ --privileged -it --name camera_app semyonov4360/camera_app:rpi
fi

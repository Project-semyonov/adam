#!/bin/bash
if [ "$(docker container ls -a | grep -c "video_deploy")" -ge 1 ]
then
        docker restart video_deploy
else
        docker build -t semyonov4360/video_deploy:rpi .
        docker run -d -v /home/pi/Videos/:/root/Videos/ --privileged -it --name video_deploy semyonov4360/video_deploy:rpi
fi

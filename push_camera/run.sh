#!/bin/bash
if [ "$(docker container ls -a | grep -c "video_deploy")" -ge 1 ]
then
        docker restart video_deploy
        docker exec video_deploy crond
else
        docker build -t semyonov4360/video_deploy:rpi .
        docker run -d -v /home/pi/Videos/:/root/Videos/ -it --name video_deploy semyonov4360/video_deploy:rpi
        docker cp responce.sh video_deploy:root/
        docker exec video_deploy bash responce.sh
        docker exec video_deploy crond
fi

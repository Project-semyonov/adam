#!/bin/bash
if [ "$(docker container ls -a | grep -c "vue_app")" -ge 1 ]
then
    docker reastart vue_app

else
    docker build -t semyonov4360/vue_app:rpi .
    
    docker run -it -p 8080:8080 --name vue-app semyonov4360/vue_app:rpi
fi

#!/bin/bash
if [-e docker container ls -a | grep "vue_app"]
then
    docker reastart vue_app

else
    docker build -t semyonov4360/vue_app .
    
    docker run -it -p 8080:8080 --name vue-app semyonov4360/vue_app
fi

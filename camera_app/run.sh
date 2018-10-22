#!/bin/bash
if docker container ls -a | grep "camera_app"
        docker restart camera_app
else
        docker build -t semyonov/camera_app . 
        docker run --rm -d --privileged --name camera_app semyonov/camera_app
fi

#!/bin/bash

docker build -t semyonov4360/camera_app:rpi .

if [ -e ../password.txt ]
then 
    myVar=$(cat ../password.txt)
    
    docker login -u semyonov4360 -p "$myVar"
    
    docker push semyonov4360/camera_app:rpi

else
    docker login -u semyonov4360 --password-stdin
    
    docker push semyonov4360/camera_app:rpi
fi

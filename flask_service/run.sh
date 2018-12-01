#!/bin/bash
if [ "$(docker container ls -a | grep -c "flask_endpoint")" -ge 1 ]
then
    docker restart flask_endpoint

else
    docker build -t semyonov4360/flask_endpoint .
    docker run --name flask_endpoint -p 5000:5000 semyonov4360/flask_endpoint
fi

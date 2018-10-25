#!/bin/bash
if [-e docker container ls -a | grep "flask_endpoint"]
then
    docker restart flask_endpoint

else
    docker build -t semyonov4360/flask_endpoint .
    docker run --name flask_endpoint -p 5000:5000 semyonov4360/flask_endpoint
fi

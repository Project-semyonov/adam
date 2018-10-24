#!/bin/bash
docker build -t semyonov4360/vue_app .
docker run -it -p 8080:8080 --rm --name vue-app semyonov4360/vue_app

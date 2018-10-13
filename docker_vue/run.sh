#!/bin/bash
docker build -t semyonov4360/vue_cli .
docker run -it -p 8080:8080 --rm --name vue-cli semyonov4360/vue_cli

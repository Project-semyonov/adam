#!/bin/bash
docker build -t semyonove4360/vue_cli .
docker run -it -p 8080:8080 --rm --name vue-cli semyonove4360/vue_cli

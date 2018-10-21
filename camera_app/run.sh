#!/bin/bash
docker build -t semyonov/camera_app .
docker run --rm -d --privileged semyonov/camera_app

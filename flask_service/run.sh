#!/bin/bash
docker build -t semyonov/flask_endpoint .
docker run --rm -p 5000:5000 semyonov/flask_endpoint

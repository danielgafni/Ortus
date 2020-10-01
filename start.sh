#!/usr/bin/bash

docker pull danielgafni/ortus:latest
docker run -d \
 -p 80:8080 \
 -p 5000:5000 \
 --mount type=bind,source="$(pwd)/app/db.sqlite",target=/ortus/app/db.sqlite \
 --mount type=bind,source="$(pwd)/.env",target=/ortus/.env

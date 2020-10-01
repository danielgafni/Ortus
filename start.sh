#!/usr/bin/bash

docker pull danielgafni/ortus:latest
docker run -d -p 80:8080 -p 5000:5000 -v "${PWD}"/app/db.sqlite:/app/db.sqlite -v "${PWD}"/.env:/.env danielgafni/ortus:latest
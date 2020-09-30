docker pull danielgafni/ortus:latest
pipenv run flask db upgrade
docker run -d -p 80:8080 -v ${PWD/app/db.sqlite}:/app/db.sqlite danielgafni/ortus:latest
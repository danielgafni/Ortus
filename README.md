# Minimalistic password manager
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Test:

[click](http://ec2-3-132-198-109.us-east-2.compute.amazonaws.com/)

# TODO:

-   edit `app/api/__init__.py`

-   production with `nginx`

-   edit `src/services/Api.js`

# Starting the application on a remote server

```bash
git clone https://github.com/danielgafni/ortus
cd ortus
docker pull danielgafni/ortus:latest
docker run -d -p 80:8080 -p 5000:5000 -v ${PWD}/app/db.sqlite:/app/db.sqlite danielgafni/ortus:latest
```
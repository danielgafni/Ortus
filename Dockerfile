FROM node:lts-alpine

WORKDIR /app

COPY package*.json ./
COPY Pipfile* ./
COPY yarn* ./

RUN apk update
RUN apk add python3 py-pip openssl
RUN pip install pipenv
RUN pipenv install
RUN pipenv run yarn install

COPY . .

RUN cp .env.local.sample .env.local
RUN echo SECRET_KEY=$(openssl rand -hex 50) > .env.local
RUN echo SECRET_VALIDATOIN_KEY=$(openssl rand -hex 50) >> .env.local

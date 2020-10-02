FROM node:lts-alpine AS development

RUN apk update
RUN apk add python3 py-pip openssl
RUN pip install pipenv

WORKDIR /ortus

# python requirements
COPY Pipfile ./
COPY Pipfile.lock ./
RUN pipenv install

# JS requirements
COPY package.json ./
COPY yarn.lock ./
COPY src ./src
RUN pipenv run yarn upgrade
RUN pipenv run yarn install
RUN pipenv run yarn build

COPY . .

RUN touch ./.env
RUN touch ./app/db.sqlite
#RUN echo "NODE_ENV=production" >> .env.local
#RUN echo SECRET_KEY=$(openssl rand -hex 50) >> .env.local
#RUN echo SECRET_VALIDATOIN_KEY=$(openssl rand -hex 50) >> .env.local

#RUN pipenv run flask db init
#RUN pipenv run flask db migrate
#RUN pipenv run flask db upgrade

CMD ["cat", ".env"]
CMD ["pipenv", "run", "flask", "run", "--host", "0.0.0.0"]
CMD ["pipenv", "run", "yarn", "serve", "--host", "0.0.0.0"]

EXPOSE 8080
EXPOSE 5000

#CMD ["nginx", "-g", "daemon off;"]
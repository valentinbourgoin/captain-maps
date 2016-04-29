Train station finder
====================
Find the nearest train station on a map !

I used the Captain Train open data, found [here](https://github.com/captaintrain/stations).  Frontend app is built in [VueJS](https://github.com/vuejs) with NPM / browserify compilation process. The backend API is a python app, using [Django REST Framework](http://www.django-rest-framework.org/), running in [Docker](https://www.docker.com/) component. Stations objects are imported in proper PgSQL database.

----------


Installation
----------------

### Frontend
Requirements : 
- [node JS](https://docs.npmjs.com/getting-started/installing-node) and npm

	npm install
	npm run dev

Server is running on http://localhost:8080/ by default.

### Backend
Requirements : 
- [Docker-compose](https://docs.docker.com/compose/install/)

Create VM (if necessary) and build services :

	docker-machine create -d virtualbox dev;
	docker-compose build
	docker-compose up -d

Sync database and import CSV data (make sure *stations* submodule is cloned and up to date) :

	docker-compose run --rm web /usr/local/bin/python manage.py migrate
	docker-compose run --rm web /usr/local/bin/python manage.py import 

Then, get docker machine IP :

	docker-machine ip dev 

You may have to change API URL in front/scripts/config.js, according to docker machine IP.
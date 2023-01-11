![enter image description here](https://lh3.googleusercontent.com/cPYomSHND0D4kDuU1qHKcv8NsaC9E1BFEljalnVwB8DCxIYSj_Wozs39C9V55nAFHaodQX_nEzs)

## Project Edu

Production ready django based starter kit application.
 
 ## Technology:
 - ***Django*** :- We have opted for Django, as we wanted to have a strong
   framework and complete ORM solution since we are planning to go with
   Python and with SQL based database
 - ***Django Rest Framework*** :- We opted for DRF as this is the best
   solution available for REST APIs for Python.
 - ***Fully Dockerised Setup*** :- Docker has become an integral part of the
   setup these days. All the settings are yml driven and are
   configurable as per the business need. One can easily turn off/on
   configurations/services via this.
 - ***System Monitoring*** :- We have included integration of MetricBeat and
   HeartBeat, they are efficient solutions to monitor system levels and
   vitals.
 - ***Celery*** :- The most preferred delayed task runner when handling
   asynchronous tasks with django applications. Very robust & easy to
   integrate.
 - ***Rabbit MQ*** :- When working with microservices, the quintessential
   requirement is of inter service communication, this where message
   broker comes into picture. Since we need to avoid the synchronous
   dependencies of the REST communication. Hence we have provisioned
   dedicated pub/sub configurations that constantly monitor the Rabbit
   MQ and execute tasks in asynchronous way.
 - ***JWT*** :- The reason why we selected JWT is that, it is used is to prove
   that the sent data was actually created by an authentic source and
   this is the most widely used mechanism while communication is
   happening over REST APIs.
 - ***Unit Test*** :- We have included the unit tests in such a way that the
   APIs are stubbed and there is no incorporation of Databases, thus
   avoiding the overheads related with Databases. Since we aim to have
   pure unit tests hence we have provisioned stubbed methods for unit
   tests.
 - ***Swagger*** :- Though for REST APIs we can get a good document available
   via Django REST Framework, but that is limited in some ways like
   publishing. We selected swagger, so that APIs can be published and be
   tested externally.

## Running the server locally

 * Clone this repo
 * Install python3.10
 * Install virtual env:
> python3 -m venv venv
 * Activate virtual env:
> source venv/bin/activate
 * Intall dependencies:
> pip install -r requirements.txt
 * Run the server:
> python manage.py runserver
-----
Docker Setup
---
 * Install [docker compose](https://docs.docker.com/compose/install/)
 * Run docker:
> Create master_app.log file inside root directory

> docker-compose build

> docker-compose up
 * To check the server, open `http://localhost:8000/`

## License

This project is licensed under the terms of the MIT license.


[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d5272664aa1f46e08d99aa13c695e663)](https://www.codacy.com/app/maestro/report-app?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=maestro-server/report-app&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.org/maestro-server/report-app.svg?branch=master)](https://travis-ci.org/maestro-server/report-app)
[![Maintainability](https://api.codeclimate.com/v1/badges/d30df800647b4c898f42/maintainability)](https://codeclimate.com/github/maestro-server/report-app/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/d30df800647b4c898f42/test_coverage)](https://codeclimate.com/github/maestro-server/report-app/test_coverage)

# Maestro Server #

Maestro Server is an open source software platform for management and discovery servers, apps and system for Hybrid IT. Can manage small and large environments, be able to visualize the latest multi-cloud environment state.

### Demo ###
To test out the demo, [Demo Online](http://demo.maestroserver.io "Demo Online")

## Documentation ##
* [UserGuide](http://docs.maestroserver.io/en/latest/userguide/cloud_inventory/reports.html "Reports User Guide")
* [API Contract](https://maestro-server.github.io/report-app/ "API Contract")

# Maestro Server - Reports API #

* Understand complex queries and generate reports
* Manage storage and control each technical flow
* Aggregate data
* Transform in artifact pdf, csv or json

![arch](http://docs.maestroserver.io/en/latest/_images/reports.png)

**Reports API, organized by modules:**

* API Rest
* Worker - General Query
* Worker - Pivot Query
* Worker - Upload Json - Filters data
* Worker - Webhook - Copy data to reports database
* Worker - Aggr - Execute agggregation task and save in report collections
* Worker - Audit - Send aggr data to audit service
* Worker - Notification (Events)
* Worker - WS (Websocket Events)

## Setup ##

#### Installation by docker ####

```bash
version: '2'

services:
    reports:
        image: maestroserver/reports-maestro
        environment:
        - "CELERY_BROKER_URL=amqp://rabbitmq:5672"
        - "MAESTRO_REPORT_URI=http://localhost:5005"
        - "MAESTRO_MONGO_URI=mongodb"
        - "MAESTRO_MONGO_DATABASE=maestro-reports"

    reports_worker:
        image: maestroserver/reports-maestro-celery
        environment:
        - "MAESTRO_REPORT_URI=http://reports:5005"
        - "MAESTRO_DATA_URI=http://data:5010"
        - "CELERY_BROKER_URL=amqp://rabbitmq:5672"
```

#### Install run api ####

```bash
python -m flask run.py --port 5005

or

FLASK_APP=run.py FLASK_DEBUG=1 flask run --port 5005

or

npm run server

// ping 
curl http://localhost:5005
```

#### Install run rabbit workers ####

```bash
celery -A app.celery worker -E -Q report --hostname=report@%h --loglevel=info

or

npm run celery
```

## TechStack ##
* Python < 3.6
* Flask
* Pandas
* NumPy
* Celery
* RabbitMq

### Env variables ###

| Env Variables             | Example               | Description                                |
|---------------------------|-----------------------|--------------------------------------------|
| MAESTRO_PORT              | 5005                  | Reports API Port                           |
| MAESTRO_MONGO_URI         | localhost             | Mongo Url conn                             |
| MAESTRO_MONGO_DATABASE    | maestro-reports       | Db name, its differente of servers-app     |
| MAESTRO_DATA_URI          | http://localhost:5010 | Data APP - API URL                         |
| MAESTRO_REPORT_URI        | http://localhost:5005 | Report App - API URL                       |
| MAESTRO_AUDIT_URI         | http://localhost:10900| Audit App - API URL                        |
| MAESTRO_WEBSOCKET_URI     | http://localhost:8000 | Webosocket App - API URL                   |
| MAESTRO_INSERT_QTD        | 200                   | Throughput insert in reports collection    |
|                           |                       |                                            |
| MAESTRO_WEBSOCKET_SECRET  | XXXX                  | Secret Key - JWT Websocket connections     |
| MAESTRO_SECRETJWT_PRIVATE | XXX                   | Secret Key - JWT private connections       |
| MAESTRO_NOAUTH            | XXX                   | Secret Pass - validate private connections |
|                           |                       |                                            |
| CELERY_BROKER_URL         | amqp://rabbitmq:5672  | RabbitMQ connection                        |                


### Contribute ###

Are you interested in developing Maestro Server, creating new features or extending them?

We created a set of documentation, explaining how to set up your development environment, coding styles, standards, learn about the architecture and more. Welcome to the team and contribute with us.

[See our developer guide](http://docs.maestroserver.io/en/latest/contrib.html)

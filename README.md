[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d5272664aa1f46e08d99aa13c695e663)](https://www.codacy.com/app/maestro/report-app?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=maestro-server/report-app&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.org/maestro-server/report-app.svg?branch=master)](https://travis-ci.org/maestro-server/report-app)
[![Maintainability](https://api.codeclimate.com/v1/badges/d30df800647b4c898f42/maintainability)](https://codeclimate.com/github/maestro-server/report-app/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/d30df800647b4c898f42/test_coverage)](https://codeclimate.com/github/maestro-server/report-app/test_coverage)


# Maestro Server - Report API #

Core API, organized by modules:

* API Rest
* Worker - General Query
* Worker - Pivot Query
* Worker - Transform - CSV
* Worker - Transform - Inventory (Ansible)
* Worker - Transform - PDF
* Worker - Upload Json
* Worker - Notification (Events)

## Dependencies ##
* Python <3.4
* Flask
* Celery
* RabbitMq
* Redis
* Upload Config (S3 or Local)

## Setup #
Create .env file, with:

TESTING=False
SECRETJWT='secret'

CELERY_BROKER_URL="amqp://localhost:5672"
CELERY_RESULT_BACKEND="redis://localhost:6379/0"
CELERYD_TASK_TIME_LIMIT=30

MAESTRO_PORT=5005
MAESTRO_MONGO_URI='localhost'
MAESTRO_MONGO_DATABASE='maestro-reports'
MAESTRO_DISCOVERY_URL='http://localhost:5000'
MAESTRO_SCAN_QTD=200
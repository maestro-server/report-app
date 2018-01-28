
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
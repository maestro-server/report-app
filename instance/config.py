# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

import os
from app.libs.jsonEncoder import DateTimeEncoder
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Config(object):
    TESTING = os.environ.get("TESTING", False)
    RESTFUL_JSON = {'cls': DateTimeEncoder}
    WS_SECRET = os.environ.get("MAESTRO_WEBSOCKET_SECRET", "wsSecretKey")

    DATABASE_URI = os.environ.get("MAESTRO_MONGO_URI", "mongodb://localhost")
    DATABASE_NAME = os.environ.get("MAESTRO_MONGO_DATABASE", "maestro-reports")

    MAESTRO_DATA_URI = os.environ.get("MAESTRO_DATA_URI", "http://localhost:5010")
    MAESTRO_AUDIT_URI = os.environ.get("MAESTRO_AUDIT_URI", "http://localhost:10900")
    MAESTRO_REPORT_URI = os.environ.get("MAESTRO_REPORT_URI", "http://localhost:5005")
    MAESTRO_WEBSOCKET_URI = os.environ.get("MAESTRO_WEBSOCKET_URI", "http://localhost:8000")

    SECRETJWT_PRIVATE = os.environ.get("MAESTRO_SECRETJWT_PRIVATE", "defaultSecretKeyPrivate")
    NOAUTH = os.environ.get("MAESTRO_NOAUTH", "defaultSecretNoAuthToken")

    CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", 'amqp://localhost')
    CELERY_DEFAULT_QUEUE = 'reports'
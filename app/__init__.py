# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import Flask
import pymongo
from pymongo import MongoClient
from .celery import make_celery
from app.libs.logger import logger

app = Flask(__name__)
app.config.from_object('instance.config.Config')

with MongoClient(app.config['DATABASE_URI'], serverSelectionTimeoutMS=1) as client:
    db = client[app.config['DATABASE_NAME']]

    celery = make_celery(app)

    try:
        client.server_info()
        logger.info("Mongo Online")
    except pymongo.errors.ServerSelectionTimeoutError as err:
        logger.error("==================================> MongoDB is down %s", err)

from app.representation import *

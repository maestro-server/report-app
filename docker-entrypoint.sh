#!/bin/sh

chown -R app:app .
su-exec app /usr/bin/gunicorn --config /opt/application/gunicorn_config.py run:app
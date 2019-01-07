FROM maestroserver/maestro-pandas

COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

RUN apk add --no-cache --virtual .build-dependencies build-base tini su-exec curl-dev libressl-dev
RUN addgroup app && adduser -S app

ENV APP_PATH=/opt/application
ENV PYCURL_SSL_LIBRARY=openssl

RUN pip3 install --upgrade pip gunicorn

WORKDIR $APP_PATH

COPY ./app $APP_PATH/app
COPY ./instance $APP_PATH/instance
COPY requirements.txt requirements.txt
COPY package.json package.json
COPY run.py $APP_PATH/run.py
COPY gunicorn_config.py /opt/gunicorn_config.py

RUN pip3 install -r requirements.txt

RUN apk del --no-cache --purge .build-deps \
RUN rm -rf /var/cache/apk/*

ENTRYPOINT ["/sbin/tini","-g","--"]
CMD ["docker-entrypoint.sh"]
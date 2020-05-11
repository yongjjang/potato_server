FROM tiangolo/uwsgi-nginx-flask:python3.7

WORKDIR /usr/src/
EXPOSE 80
COPY ./app /app

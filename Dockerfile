from python:latest
MAINTAINER Caio Storni
COPY . /var/docker
WORKDIR /var/docker
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT python manage.py makemigrations
ENTRYPOINT python manage.py migrate
ENTRYPOINT python manage.py runserver 0.0.0.0:9090
EXPOSE 9090

FROM ubuntu

MAINTAINER ANAND MOHAN <anandmohan777@gmail.com>

RUN apt-get update && apt-get install -y python python python-dev python-pip curl vim
RUN pip install web.py
RUN python -m pip install psycopg2 Flask

ADD /app /app
EXPOSE 8080
WORKDIR /app

CMD python helloworld.py

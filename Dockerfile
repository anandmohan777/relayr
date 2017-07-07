FROM ubuntu

MAINTAINER Saurabh Taneja

RUN apt-get update
RUN apt-get install -y python python python-dev python-pip curl

RUN pip install web.py
RUN  python -m pip install psycopg2 Flask

ADD /my_application /my_application

EXPOSE 8080

WORKDIR /my_application

CMD python hello.py



#!/usr/bin/python
import logging
from logging.handlers import RotatingFileHandler

import web, psycopg2
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	conn = psycopg2.connect(database = 'relayr', user = 'relayr' , password = 'RelayrPassword' , host = 'postgres', port = 5432)
	app.logger.info("Opened database successfully")
	cur = conn.cursor()
	cur.execute('''CREATE TABLE COMPANY(ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, AGE INT NOT NULL, ADDRESS CHAR(50), SALARY REAL);''')
	app.logger.info("Table created successfully")
	cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )");
	cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
	cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
	cur.execute("SELECT COUNT(*) from COMPANY")
	result=cur.fetchone()
	number_of_rows=result[0]
	if number_of_rows > 0:
		app.logger.info("Hello World!")
		app.logger.info(number_of_rows)
                return "Hello World!"
	else:
		app.logger.info("Could not connect to database")
                return "Could not connect to database"

if __name__ == "__main__":
    handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=10)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(host='0.0.0.0', port=8080 ,debug = True)

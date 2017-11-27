import logging
from logging.handlers import RotatingFileHandler

import web, psycopg2
from flask import Flask
app = Flask(__name__)

@app.route("/")
def helloworld():
        cur = initscript()
        result=cur.fetchone()
        if result[0] > 0:
            return result[1]
        else:
            return "Cannot connect to the database"

def initscript():
	conn = psycopg2.connect(database = 'relayr', user = 'relayr' , password = 'Passw0rd' , host = 'postgres', port = 5432)
        app.logger.info("Opened database successfully")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS APP_DB(ID INT , DESCRIPTION TEXT);")
        app.logger.info("Table created successfully")
        cur.execute("INSERT INTO APP_DB (ID, DESCRIPTION) VALUES (1, 'Hello World!')")
        cur.execute("SELECT * from APP_DB")
        conn.commit()	   
        return cur

if __name__ == "__main__":
        handler = RotatingFileHandler('app.log', maxBytes=1000, backupCount=10)
        handler.setLevel(logging.INFO)
        app.logger.addHandler(handler)
        app.run(host='0.0.0.0', port=8080 ,debug = True)

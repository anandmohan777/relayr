## helloworld-python-flask-webapp

This is a Python app that connect to PostgreSQL database and returns 'Hello, world' message that is stored in the database.

## How to run
After cloning the repo run the following

```bash
cd relayr
sudo docker swarm init 
sudo docker stack deploy -c docker-compose.yml relayrapp
```

then, type the following in your browser

```bash
127.0.0.1:8080
```

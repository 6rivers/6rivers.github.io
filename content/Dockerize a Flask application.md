Title: Dockerize a Flask application
Date: 2022-10-22
Category: Python
Summary: Creating a flask application and deploy  it using Docker
opengraph_image: dockerize_flask.jpg


#### About Docker:

- Docker is an open source platform that enables developers to manage containers. A container is a lightweight virtualization solution that enables our flask web app to run in total isolation from all of its dependencies and configurations without the use of actual virtual servers. 
- By using  Python "virtualenv", you can easily swap between Python versions and dependencies, but you are restricted to the host OS. Containerization enables portability from one machine to another. Although it is not the only platform for containers, "Docker" is the most commonly used.
- You can find several docker [images](https://hub.docker.com/_/python/) with every combination of OS and Python versions.
- You can follow this [official link](https://docs.docker.com/get-docker/) to install Docker on your machine.
- Now we will create a simple web app using Flask and will dockerize it.

#### Build a sample Flask app:

- Create a new folder
```python
mkdir Docker-Flask
```

- Inside the root folder, Create and activate virtual environment(I'm using Windows OS here)
```python 
cd Docker-Flask
python -m venv venv
venv\scripts\activate
```

- Within activated virtual environment, install Flask
```python
pip install Flask
```

- Create a new "application.py" in the same folder and add below sample code
```python 
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<h3>This is a Docker Demo for Flask Application</h3>'

if __name__ == '__main__':
    app.run()
```

- Now create a '.flaskenv' file and write "FLASK_APP=application.py" which specify how to load the application.
- Since we are using '.flaskenv' file we need to install 'python-dotenv' using `pip install python-dotenv`
- Now run `pip freeze > requirements.txt` to create a file that has a list of all libraries used in this project.
- To start our development server, run `flask run` command from the root folder(Docker-Flask).

![run_flask]({static}images/docker_flask_2.png)

- To verify, go to "http://127.0.0.1:5000/" in your browser.

#### Dockerfile:

- The command that is used to build container images is `docker build` and we can give instructions to this build command using a file called "Dockerfile".
- Create this file in the root folder and copy the below commands and save it.
```Dockerfile
FROM python:3.8-slim

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"]
```

- "`FROM python:3.8-slim`" tells the Docker which base image to be used, in this case, a Python image.
- `WORKDIR /app` tells the Docker which folder to use for rest of the operations.
- `COPY . /app`, this command makes the Docker to copy all the files in our local root directory to container's '/app' folder.
- `RUN pip install -r requirements.txt` will install each requirement written in the requirements.txt file.
- `EXPOSE 5000`, the port that this container will use for web server can be configured by this command. (5000 is the standard Flask port)
- `CMD ["flask", "run", "--host", "0.0.0.0"]`, this command starts the server. Here we are using `host = 0.0.0.0` which makes Flask to listen all IP addresses in that container so that the container can be accessible from outside.

#### Build a Docker Image: 

- Now we need to build the image using `docker build` command as shown below
```Dockerfile
docker build -t flask-demo-app:latest .
```
- `-t` argument sets the name and tag for the new container image. The "`.`" represents the base directory in which the container is to be created, which has Dockerfile. The image will be created during the build phase and saved on your machine after evaluating the commands in the Dockerfile.
- `docker images` lists the images created on your machine.
#### Run the Docker image:

- With an image created, now we can run the container version of our flask application using `docker run` command
```Docker
docker run --name flask-app -d -p 5000:5000 flask-demo-app:latest
```

- `--name` parameter gives the name to the container(flask-app), `-d` to run the container in the background or detached mode and not connected to our terminal,  `-p 5000:5000` maps the host's(In this instance, my laptop) port 5000 to the container's port 5000. `flask-demo-app:latest` indicates the image name.
- By running the above command, your dockerized application will be available at localhost(http://127.0.0.1:5000/)
![check_app]({static}images/docker_flask_1.png)

- When we have locally tested docker containers, we can migrate them to cloud services that support Docker.
#### Other Info:
- `docker ps` to see the list of containers running currently
- `docker stop <docker-id>` to stop the container
- `docker restart <docker-id>` to restart the container
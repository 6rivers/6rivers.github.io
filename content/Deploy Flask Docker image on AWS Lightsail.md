Title: Deploy Flask Docker image on AWS Lightsail
Date: 2022-12-04
Category: Python
Summary: Creating a flask application, its Docker image and deploying it to AWS Lightsail
opengraph_image: AWS_Lightsail.jpg


- If you have your Flask application container built and running locally on your local dev machine. And want to get it running on the cloud to make your application available for other users over the internet, there is a simplified solution on AWS called Amazon Lightsail Container Services. 
- It removes many underlying complex AWS concepts for us and it is an ideal solution for developers who just want to focus on coding their applications.
- Also Lightsail's budgeting is easy and has predictable price structure.

#### Prerequisites:

1. **AWS account**
2. **Docker** -- to create docker image
3. **AWS Command Line Interface (CLI)** -- to manage Lightsail service. Follow this [link](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) to install CLI on your machine
4. **Lightsail Control Plugin** -- to access container images on your local machine, [link](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-install-software#install-software-lightsailctl) to install plugin.

Detailed post on dockerization of Flask app, can be find [here](https://ranganaths.com/dockerize-a-flask-application.html)

#### Build a sample Flask app:

- Create a new directory
``` cmd
mkdir Docker-Flask-Lightsail
cd Docker-Flask-Lightsail
```

- Create a new 'application.py' and copy the below code and save it
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<h3>This is a demo for deploying a flask app on AWS Lightsail using Docker</h3>'

if __name__ == '__main__':
    app.run()
```

- Now create a 'requirements.txt' file and write `Flask==2.1.2` and save the file.

#### Dockerize Flask app:

- Create a new 'Dockerfile' and write the below commands and save it.
```Dockerfile
FROM python:3.8-slim

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "application.py" ]
```

- run below command to create docker image
```dockerfile
docker build -t flask-lightsail:latest .
```
- Now to run docker container run below command
```Dockerfile
docker run --name flask-service -d -p 5000:5000 flask-lightsail:latest 
```
- To verify, go to 'http://127.0.0.1:5000/' 

#### Deploy the image to AWS Lighsail:

Now, we need to deploy this image to AWS Lightsail. For that we need to create Lightsail container service using the AWS CLI and push our local container image to the new Lightsail container service.

- To create the Lightsail container service use below command, where power and scale parameters represents the capacity of the container service. Here we are using "mirco" which provides **vCPU:** 0.25 and **RAM:** 1GB. This option is free of charge for first three months.
```cmd
aws lightsail create-container-service --service-name flask-app --power micro --scale 1
```
- Initially you might see `"state": "PENDING",` in the output while your lightsail container service is being created for you.
- To check the status of your container service, use below command
```cmd
aws lightsail get-container-services
```

- To push our application container image use
```cmd
aws lightsail push-container-image --service-name flask-app --label flask-container-image --image flask-lightsail:latest
```

- `--service-name` -- The name of the container service in the lightsail service to which our application container image will be pushed.
- `--label` -- the label to be applied for the image on the container service
- `--image` -- our application container image which will be pushed to the container service
- The above command will returns an output similar to below where ":flask-app.flask-container-image.8" is the image details
```
Refer to this image as ":flask-app.flask-container-image.8" in deployments
```

- Now we need to create two json files called "**containers.json**" and "**public-endpoint.json**" 
- "**containers.json**" -- describes the settings of the containers
```json
{
    "flask": {
        "image": ":flask-app.flask-container.7",
        "ports": {
            "5000": "HTTP"
        }
    }
}
```
- "**public-endpoint.json**" -- describes the settings of the public endpoint for the container service
```json
{
    "containerName": "flask",
    "containerPort": 5000
}
```
- Now we need to run the container on the Lightsail using below command
```cmd
aws lightsail create-container-service-deployment --service-name flask-app --containers file://containers.json --public-endpoint file://public-endpoint.json 
```

- It will return you an URL to navigate to our flask app
- To delete container service
```cmd
aws lightsail delete-container-service --service-name flask-app
```
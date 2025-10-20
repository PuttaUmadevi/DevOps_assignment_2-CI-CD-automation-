Task : Implementing a complete automated workflow that covers version control, containerization, 
continuous integration, continuous delivery, and orchestration.

Step followed :

STEP - 1 : application

Built a simple application for the ticket booking system using HTML,CSS,JavaScript and a simple backend using python-flask
![frontend web page screenshot](frontend.png)

STEP - 2 : Dockerize

1) create dockerfile
2) In powershell : Docker Login , Build docker image , contanierize it , and run the container

Commands :
> docker login
> docker build -t tag_name .
> docker run -d -p 8081:5000 image_name
Now open localhost:8081

![alt text](docker.png)
![alt text](docker2.png)


Now Pushing the image to docker hub

>docker tag <local-image-name> <your-dockerhub-username>/<image-name>:<tag>

> docker push <your-dockerhub-username>/<image-name>:<tag>

![alt text](image.png)
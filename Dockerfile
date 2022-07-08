#Given that we just have python3 as a dependency in our application, we can simply choose a python image.
FROM python:3.9-slim-buster

#We are specifying /myportfolio directory as the working directory of the container image
WORKDIR /project-daak-alanPortfolio

#Copy all project files into the container image at the working directory
COPY requirements.txt .

#Install dependencies using pip3
RUN pip3 install -r requirements.txt

COPY . .

#Specify the command that runs when a container is created from this container image
CMD ["flask", "run", "--host=0.0.0.0"]

#Specify the port that will be exposed from the container. In our case, it's port 5000 by default
EXPOSE 5000
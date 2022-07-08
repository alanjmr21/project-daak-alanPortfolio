#!bin/sh

#go to the project
cd project-daak-alanPortfolio

#pull all changes from repo
git fetch && git reset origin/main --hard

#Spin containers down to avoid memory issues
docker compose -f docker-compose.prod.yml down

#Build the images and start the container using the .prod.yml file
docker compose -f docker-compose.prod.yml up -d --build
#!bin/sh

#go to the project
cd project-daak-alanPortfolio

#pull all changes from repo
git fetch && git reset origin/main --hard

#Enter the python virtual environment and Install python dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

#Restart myportfolio service
systemctl daemon-reload
systemctl restart myportfolio
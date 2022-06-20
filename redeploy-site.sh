#!bin/sh

#kill all tmux sessions
tmux kill-session -a

#go to the project
cd project-daak-alanPortfolio

#pull all changes from repo
git fetch && git reset origin/main --hard

#create a new detached session named "alanPortfolio"
tmux new -s alanPortfolio

#activate virtual environment
tmux send-keys -t "alanPortfolio" "source python3-virtualenv/bin/activate" Enter

#install dependencies
tmux send-keys -t "alanPortfolio" "pip install -r requirements.txt" Enter

#run the site
tmux send-keys -t "alanPortfolio" "export FLASK_ENV=develoment" Enter
tmux send-keys -t "alanPortfolio" "flask run --host=0.0.0.0" Enter

#detach from the session
tmux send-keys -t "alanPortfolio" C-b d
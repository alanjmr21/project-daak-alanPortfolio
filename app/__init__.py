#from crypt import methods
from datetime import datetime
from email import contentmanager
from email.policy import default
import os
from playhouse.shortcuts import model_to_dict
from flask import Flask, render_template, request
import json
from peewee import *
from jinja2 import Environment, FileSystemLoader
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)
if os.getenv("TESTING") == "true": 
    print("Running in test mode")
    mydb=SqliteDatabase('file:memory?mode=memory&cache=shared',uri=True)
else: 
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
              user=os.getenv("MYSQL_USER"),
              password=os.getenv("MYSQL_PASSWORD"),
              host=os.getenv("MYSQL_HOST"),
              port=3306
)

class TimelinePost(Model):
    name=CharField()
    email=CharField()
    content=CharField()
    created_at=DateTimeField(default=datetime.now)
    
    class Meta:
        database=mydb

mydb.connect()
mydb.create_tables([TimelinePost])

a = open('app/data/work.json')
work_data = json.load(a)
a.close()
work_d = work_data.copy()

b = open('app/data/hobbies.json')
hobby_data = json.load(b)
b.close()
hobbies_d = hobby_data.copy()

c = open('app/data/education.json')
education_data = json.load(c)
c.close()
education_d = education_data.copy()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

@app.route('/work')
def work():
    return render_template('work.html', work = work_d)

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', hobbies = hobbies_d)

@app.route('/education')
def education():
    return render_template('education.html', education = education_d)

@app.route('/travel')
def travel():
    return render_template('travel.html')

@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title="Timeline")

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    #NAME
    name = request.form['name']
    if name == "": 
        return "Invalid name", 400

    #EMAIL 
    email = request.form['email']
    if not '@' in email:
        return "Invalid email", 400

    #CONTENT
    content = request.form['content']
    if content == "":
        return "Invalid content", 400
    
    #NO ERRORS
    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    
    return model_to_dict(timeline_post)
    
@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts':[
            model_to_dict(p)
            for p in
            TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

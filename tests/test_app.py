#tests/test_app.py

import unittest 
import os 
os.environ['TESTING'] = 'true'

from app import app 

class AppTestCase(unittest.TestCase):
    def setUp(self): 
        self.client = app.test_client()

    def test_home(self): 
        response = self.client.get("/")
        assert response.status_code == 200 
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html
        assert "<a href = {{ url_for('aboutme')}}>" in html 

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200 
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json 
        #length = 0, nothing added 
        assert len(json["timeline_posts"]) == 0

        #testing POST method 
        new_post = self.client.post('/api/timeline_post', data={"name":"Lauren", "email":"lauren@example.com", "content":"Lauren's Context"})
        assert new_post.status_code == 200
        
        #testing GET method 
        get_post = self.client.get('/api/timeline_post')
        json = get_post.get_json()
        #now, the length should be 1 
        assert len(json['timeline_posts']) == 1
        
        #checking timeline 
        timeline_post = self.client.get('/timeline')
        assert timeline_post.status_code == 200
        html = timeline_post.get_data(as_text=True)
        assert '<form id = "form" method = "POST" action = "/api/timeline_post">' in html

    def test_malformed_timeline_post(self): 
        #1st test - Checking name 
        response = self.client.post("/api/timeline_post", data = {"email":"john@example.com", "content":"Hello World, I'm John!"})
        assert response.status_code == 400 
        html = response.get_data(as_text=True)
        #response for the 1st test 
        assert "Invalid name" in html 

        #2nd test - Checking content 
        response = self.client.post("/api/timeline_post", data={"name":"John Doe", "email":"john@example.com", "content":""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        #response for 2nd test 
        assert "Invalid content" in html
        
        #3rd test - Checking Email 
        response = self.client.post("/api/timeline_post", data={"name":"John Doe","email":"not an email", "content":"Hello World, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
         

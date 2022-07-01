#test_db.py 

import unittest 
from peewee import * 

from app import TimelinePost 

MODELS = [TimelinePost]

#use an in-memory SQLite for tests. 
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase): 
    def setUp(self):
        #Bind model classes to test db. Since we have a complete list of
        #all the modules, we do not need to recursively bind dependencies. 
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        
        test_db.connect() 
        test_db.create_tables(MODELS)

    def tearDown(self): 
        #Not strictly necessary since SQLite in-memory databases only live 
        #for the duration of the connection, and in the next step we close
        #the connection...but a good practice all the same. 

        test_db.drop_tables(MODELS)

        #close connection to db. 
        test_db.close()
        
    def test_timeline_post(self): 
        #Create 2 timeline posts. 
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello world, I\'m John!')
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe', email='jame@example.com', content='Hello world, I\'m Jane!')
        assert second_post.id == 2
        #gets the timeline post with id == 1 
        first_get = TimelinePost.get(id=1)
        #checks the contents if they are the same 
        assert first_get.name == 'John Doe'
        assert first_get.email == 'john@example.com'
        assert first_get.content == 'Hello world, I\'m John!'

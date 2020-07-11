from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock
from application import app, db
from os import getenv

class TestBase(TestCase):
    def create_app(self):
        return app


    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class TestResponse(TestBase):
    def test_homeview(self):
        response = self.client.get(url_for('home'), data="")
        self.assertIn(b"DnD Character Generator test", response.data)
    
    
    def test_home(self):
        with requests_mock.mock() as x:
            x.get("http://service_two:5001/class", text="Barbarian")
            x.get("http://service_three:5002/race", text="Dwarf")
            x.post("http://service_four:5003/name", text="Bunkyl")
            x.post("http://service_four:5003/stats", text='{"strength": 14, "constitution": 14, "charisma": 14, "dexterity": 14, "intelligence": 14, "wisdom": 14}')
            response = self.client.post(url_for('home', data = ""))
            self.assertIn(b"Barbarian", response.data)
            self.assertIn(b"Dwarf", response.data)
            self.assertIn(b"Bunkyl", response.data)
            self.assertIn(b"wisdom", response.data)

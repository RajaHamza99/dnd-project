from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock
from application import app
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




class TestResponse(TestBase):
    def test_homeview(self):
        response = self.client.get(url_for('home'), data="")
        self.assertIn(b"DnD Character Generator", response.data)

    def test_home(self):
        with requests_mock.mock() as x:
            x.get("http://service_two:5001/class", text="Bard")
            x.get("http://service_three:5002/race", text="Elf")
            x.post("http://service_four:5003/name", text="Wrandithas")
            response = self.client.post(url_for('home'))
            self.assertIn(b"Bard", response.data)
            self.assertIn(b"Elf", response.data)
            self.assertIn(b"Wrandithas", response.data)

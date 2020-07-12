from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock

from application import app

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


class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    
    
    def test_generatename(self):
        elf_names = ["Wrandithas", "Baljeon", "Ianris", "Zumpetor", "Olowraek", "Advalur", "Trazeiros", "Virkian", "Qidan", "Luwraek", "Adleth", "Krisrora", "Bithyra", "Gilharice", "Grecyne", "Inatris", "Keyrel", "Caicaryn", "Greroris", "Qixisys"]
       
        with requests_mock.mock() as x:
            x.post("http://service_four:5003/generatename", text="Elf")
            response = self.client.post(url_for('generatename'))
            self.assertIn(b"Wrandithas", response.data)

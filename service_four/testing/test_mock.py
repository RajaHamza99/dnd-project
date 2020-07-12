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
        elf_names = [b"Wrandithas", b"Baljeon", b"Ianris", b"Zumpetor", b"Olowraek", b"Advalur", b"Trazeiros", b"Virkian", b"Qidan", b"Luwraek", b"Adleth", b"Krisrora", b"Bithyra", b"Gilharice", b"Grecyne", b"Inatris", b"Keyrel", b"Caicaryn", b"Greroris", b"Qixisys"]
       
        response = self.client.post(url_for('generatename'), data="Elf")
        self.assertTrue(response.data in elf_names)


    def test_generatestats(self):
        stats = {"strength": 10, "dexterity": 10, "constitution": 10, "intelligence": 10, "wisdom": 10, "charisma": 10}

        response = self.client.post(url_for('generatestats'), data="Elf")
        self.assertIn()

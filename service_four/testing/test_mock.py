from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app


class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_generatename(self):
        elf_names = ["Wrandithas", "Baljeon", "Ianris", "Zumpetor", "Olowraek", "Advalur", "Trazeiros", "Virkian", "Qidan", "Luwraek", "Adleth", "Krisrora", "Bithyra", "Gilharice", "Grecyne", "Inatris", "Keyrel", "Caicaryn", "Greroris", "Qixisys"]
        with patch('requests.post') as x:
            x.return_value.text = "Elf"
            response = self.client.post(url_for('generatename'))
            self.assertIn(b"Wrandithas", response.data)

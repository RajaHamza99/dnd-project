from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock
from os import getenv

try:
    from application import app
except ImportError:
    print(ImportError)

class TestBase(TestCase):
    def create_app(self):
        return app
                            
class TestResponse(TestBase):
    def test_generatename(self):
        elf_names = ["Wrandithas", "Baljeon", "Ianris", "Zumpetor", "Olowraek", "Advalur", "Trazeiros", "Virkian", "Qidan", "Luwraek", "Adleth", "Krisrora", "Bithyra", "Gilharice", "Grecyne", "Inatris", "Keyrel", "Caicaryn", "Greroris", "Qixisys"]
        with requests.mock_mock() as x:
            x.get('http://service_four:5003/name', text="Elf")
            response = self.client.get(url_for('generatename',))
            self.assertIn(response.text in elf_names)
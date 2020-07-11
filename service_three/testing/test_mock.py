from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_generaterace(self):
        races = [b"Elf", b"Tiefling", b"Gnome", b"Human", b"Satyr", b"Half-Elf"]
        response = self.client.get(url_for('generaterace'))
        self.assertTrue(response.data in races)

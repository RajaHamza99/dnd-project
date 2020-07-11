from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_generaterace_view(self):
        self.assertEqual(self.client.get(url_for('generaterace')).status_code, 200)

    def test_generaterace(self):
        races = [b"Dragonborn", b"Dwarf", b"Halfling", b"Human", b"Half-Orc", b"Kenku"]
        response = self.client.get(url_for('generaterace'))
        self.assertTrue(response.data in races)

from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_home_view(self):
        self.assertEqual(self.client.get(url_for('generateclass')).status_code, 200)

    def test_generaterace(self):
        classes = [b"Barbarian", b"Fighter", b"Monk", b"Rogue", b"Blood Hunter"]
        response = self.client.get(url_for('generateclass'))
        self.assertTrue(response.data in classes)

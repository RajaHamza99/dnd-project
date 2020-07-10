from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_human(self):
        with patch('requests.get') as g:
            g.return_value.text = "Barbarian"

            response = self.client.get(url_for('home'))
            self.assertIn(b'Barbarian', response.data)

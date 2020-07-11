from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_generateclass(self):
        classes = [b"Bard", b"Cleric", b"Druid", b"Paladin", b"Ranger", b"Sorcerer", b"Warlock", b"Wizard"]
        response = self.client.get(url_for('generateclass'))
        self.assertTrue(response.data in classes)

from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock
from os import getenv
import sys
from app import app


class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):
    def test_homeview(self):
        self.assertEqual(self.client.get(url_for('home')).status_code, 200)

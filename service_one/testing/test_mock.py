import pytest
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_human(self):
    elf_names = [b"Wrandithas", b"Baljeon", b"Ianris", b"Zumpetor", b"Olowraek", b"Advalur", b"Trazeiros", b"Virkian", b"Qidan", b"Luwraek", b"Adleth", b"Krisrora", b"Bithyra", b"Gilharice", b"Grecyne", b"Inatris", b"Keyrel", b"Caicaryn", b"Greroris", b"Qixisys"]
    response = self.client.post('/generatename', data='Human')
    self.assertIn(response.data in human_names)

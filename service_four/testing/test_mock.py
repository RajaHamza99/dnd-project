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
        elf_names = [b"Wrandithas", b"Baljeon", b"Ianris", b"Zumpetor", b"Olowraek", b"Advalur", b"Trazeiros", b"Virkian", b"Qidan", b"Luwraek", b"Adleth", b"Krisrora", b"Bithyra", b"Gilharice", b"Grecyne", b"Inatris", b"Keyrel", b"Caicaryn", b"Greroris", b"Qixisys"]
       
        response = self.client.post(url_for('generatename'), data="Elf")
        self.assertTrue(response.data in elf_names)

    def test_generatetieflingname(self):
        tiefling_names = [b"Rezire", b"Garadius", b"Valemon", b"Zherakas", b"Iamir", b"Guerakas", b"Kilron", b"Harmony", b"Innovation", b"Hymn", b"Rolyvia", b"Oriborys", b"Mismaia", b"Seiripunith", b"Velyola", b"Sarqine", b"Valza", b"Uncommon", b"Trickery", b"Voyage"]
        
        response = self.client.post(url_for('generatename'), data="Tiefling")
        self.assertTrue(response.data in tiefling_names)

    def test_generatehumanname(self):
        human_names = human_names = [b"Fahnin Zehro", b"Melam Nulud", b"Brukvork Deadshard", b"Barstulm Mooncreek", b"Fabral Glug", b"Bral Stivredz", b"Tulvom Orbpike", b"Um Twobough", b"Mihpion-Zad Nanskankhifk", b"Beurhuef Biprueb", b"Gandoutvoc Gevarginti", b"Drerdoc Hemuri", b"Jia Jain", b"Iam Niaoy", b"Ritemer Godreza", b"Cranin Ozogal", b"Judimah Zommid", b"Namih Pahla", b"Teelzenell Keentrap", b"Jole Forestfang", b"Choto Mag", b"Kih Mamog", b"Lovami Seawood", b"Kafre Noseorb", b"Rethani Jekrevehd", b"Totho Meldrikt", b"Sudhandra Nakanovza", b"Hihi Emura", b"Jai Waim", b"Shai Nua", b"Irb Ralurgal", b"Mitf Pisonzas"]

        response = self.client.post(url_for('generatename'), data="Human")
        self.assertTrue(response.data in human_names)

    def test_generategnomename(self):
        gnome_names = [b"Bilgrim", b"Dornan", b"Yemorn", b"Dornan", b"Jeser", b"Manlin", b"Eniver", b"Panacryn", b"Willen", b"Rasben", b"Daphiniana", b"Dorhana", b"Banfi", b"Welroe", b"Niwyse", b"Foldira", b"Wrona", b"Lilli", b"Jogani", b"Krigani"]

        response = self.client.post(url_for('generatename'), data="Gnome")
        self.assertTrue(response.data in gnome_names)


    def test_satyrnames(self):
        satyr_names = [b"Nalprath", b"Narkerta", b"Elroykos", b"Narkdon", b"Galreth", b"Tavokas", b"Quooros", b"Cruster", b"Dayethas", b"Jaurian", b"Enahanna", b"Ollyn", b"Brixis", b"Albynn", b"Jarwyse", b"Faedys", b"Illaxis", b"Zentora", b"Trilenae", b"Leskiries"]

        response = self.client.post(url_for('generatename'), data="Satyr")
        self.assertTrue(response.data in satyr_names)

    def test_halfelfnames(self):
        half_elf_names = [b"Panneiros", b"Ianelor", b"Dorlumin", b"Frilsariph", b"Zannan", b"Elelor", b"Graparin", b"Belzaren", b"Corfaelor", b"Tralumin", b"Aluhophe", b"Saelmythe", b"Yllmythe", b"Sylstine", b"Hozenya", b"Aluzenya", b"Wolxaris", b"Bynhophe", b"Yeshophe", b"Xyrenyphe"]
        response = self.client.post(url_for('generatename'), data="Half-Elf")
        self.assertTrue(response.data in half_elf_names)

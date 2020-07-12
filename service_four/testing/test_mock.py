from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app


    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
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

    def test_dragonbornnames(self):
        dragonborn_names = [b"Jinkax Ochek", b"Nesjhan Felkejaros", b"Vrakqrin Clearrhidiash", b"Saseth Nyuchoth", b"Yorfras Drankendualash", b"Dolin Cuustic", b"Lumirakas Errhunduth", b"Pawarum Curjed", b"Narfarn Myimphostudak", b"Faerfras Thapoc", b"Opora Dalmishkmuril", b"Hawophyl Vechaathic", b"Ushirann Nyelmiak", b"Loravyre Guacithus", b"Erlifyire Fenkashtondil", b"Nadalynn Cluldriash", b"Welsigil Tultus", b"Loragissa Uthtijellec", b"Koriel Shunkuth", b"Ophihymm Shuchuas"]
        

        response = self.client.post(url_for('generatename'), data="Dragonborn")
        self.assertTrue(response.data in dragonborn_names)

    def test_dwarfnames(self):
        dwarf_names = [b"Bunkyl", b"Bundrum", b"Galkahm", b"Bhargran", b"Tormar", b"Gralmir", b"Berman", b"Thermun", b"Gramdram", b"Bharnom", b"Nalgwyn", b"Jinmura", b"Braenwynn", b"Brillethiel", b"Sarvian", b"Kaittin", b"Bronria", b"Nasswaen", b"Brillera", b"Barbera"]

        response = self.client.post(url_for('generatename'), data="Dwarf")
        self.assertTrue(response.data in dwarf_names)


    def test_halflingnames(self):
        halfling_names = [b"Kaseon", b"Jokas", b"Tebul", b"Urider", b"Conkas", b"Kasrin", b"Panton", b"Barlos", b"Osbin", b"Gardal", b"Ledove", b"Lecey", b"Ariree", b"Idani", b"Paesira", b"Anara", b"Levyre", b"Pruwyse", b"Oradrey", b"Therjen"]

        response = self.client.post(url_for('generatename'), data="Halfling")
        self.assertTrue(response.data in halfling_names)

    def test_halforcnames(self):
        half_orc_names = [b"Lumurimm", b"Drigar", b"Gadash", b"Kumash", b"Harask", b"Oguotar", b"Gramabak", b"Koranars", b"Zurigak", b"Grumurth", b"Zanid", b"Zanegur", b"Rez", b"Ekuzira", b"Zonisha", b"Kerazara", b"Alogum", b"Gijunchu", b"Zunamar", b"Rahegri"]

        response = self.client.post(url_for('generatename'), data="Half-Orc")
        self.assertTrue(response.data in half_orc_names)

    def test_kenkunames(self):
        kenku_names = [b"Shaker", b"Bubbler", b"Chimer", b"Swatter", b"Crow Call", b"Horse Blow", b"Pig Snort", b"Saw Wobble", b"Mallet Smash", b"Wood Drop"]

        response = self.client.post(url_for('generatename'), data="Kenku")
        self.assertTrue(response.data in kenku_names)




    def test_generateelf(self):
        stats = {"strength": 10, "dexterity": 10, "constitution": 10, "intelligence": 10, "wisdom": 10, "charisma": 10}

        response = self.client.post(url_for('generatestats'), data="Elf")
        self.assertIn(b"wisdom", response.data)
        self.assertIn(b"strength", response.data)
        self.assertIn(b"dexterity", response.data)
        self.assertIn(b"constitution", response.data)
        self.assertIn(b"intelligence", response.data)
        self.assertIn(b"charisma", response.data)
        
        assert stats["strength"] >= 3 and stats["strength"] <=18
        assert stats["dexterity"] >= 3 and stats ["dexterity"] <= 20
        assert stats ["constitution"] >= 3 and stats ["constitution"] <= 18
        assert stats ["intelligence"] >= 3 and stats ["intelligence"] <= 18
        assert stats ["charisma"] >= 3 and stats ["charisma"] <= 18
        assert stats ["wisdom"] >= 3 and stats ["wisdom"] <= 18


    def test_generatetiefling(self):
        stats = {"strength": 10, "dexterity": 10, "constitution": 10, "intelligence": 10, "wisdom": 10, "charisma": 10}

        response = self.client.post(url_for('generatestats'), data="Tiefling")
        self.assertIn(b"wisdom", response.data)
        self.assertIn(b"strength", response.data)
        self.assertIn(b"dexterity", response.data)
        self.assertIn(b"constitution", response.data)
        self.assertIn(b"intelligence", response.data)
        self.assertIn(b"charisma", response.data)
        
        assert stats["strength"] >= 3 and stats["strength"] <=18
        assert stats["dexterity"] >= 3 and stats["dexterity"] <=18
        assert stats["constitution"] >=3 and stats ["constitution"] <=18
        assert stats["intelligence"] >=3 and stats ["intelligence"] <=19
        assert stats["charisma"] >= 3 and stats ["charisma"] <=20
        assert stats["wisdom"] >= 3 and stats ["wisdom"] <=18


    def test_generatehuman(self):
        stats = {"strength": 10, "dexterity": 10, "constitution": 10, "intelligence": 10, "wisdom": 10, "charisma": 10}

        response = self.client.post(url_for('generatestats'), data="Human")
        self.assertIn(b"wisdom", response.data)
        self.assertIn(b"strength", response.data)
        self.assertIn(b"dexterity", response.data)
        self.assertIn(b"constitution", response.data)
        self.assertIn(b"intelligence", response.data)
        self.assertIn(b"charisma", response.data)
        
        assert stats["strength"] >= 3 and stats["strength"] <=19
        assert stats["dexterity"] >= 3 and stats["dexterity"] <=19
        assert stats["constitution"] >=3 and stats ["constitution"] <=19
        assert stats["intelligence"] >=3 and stats ["intelligence"] <=19
        assert stats["charisma"] >= 3 and stats ["charisma"] <=19
        assert stats["wisdom"] >= 3 and stats ["wisdom"] <=19


    def test_generategnome(self):
        stats = {"strength": 10, "dexterity": 10, "constitution": 10, "intelligence": 10, "wisdom": 10, "charisma": 10}
        
        response = self.client.post(url_for('generatestats'), data="Gnome")
        self.assertIn(b"wisdom", response.data)
        self.assertIn(b"strength", response.data)
        self.assertIn(b"dexterity", response.data)
        self.assertIn(b"constitution", response.data)
        self.assertIn(b"intelligence", response.data)
        self.assertIn(b"charisma", response.data)
        
        assert stats["strength"] >= 3 and stats["strength"] <=18
        assert stats["dexterity"] >= 3 and stats["dexterity"] <=18
        assert stats["constitution"] >=3 and stats ["constitution"] <=18
        assert stats["intelligence"] >=3 and stats ["intelligence"] <=20
        assert stats["charisma"] >= 3 and stats ["charisma"] <=18
        assert stats["wisdom"] >= 3 and stats ["wisdom"] <=18

    def test_generatesatyr(self):
        stats = {"strength": 10, "dexterity": 10, "constitution": 10, "intelligence": 10, "wisdom": 10, "charisma": 10}

        response = self.client.post(url_for('generatestats'), data="Satyr")
        self.assertIn(b"wisdom", response.data)
        self.assertIn(b"strength", response.data)
        self.assertIn(b"dexterity", response.data)
        self.assertIn(b"constitution", response.data)
        self.assertIn(b"intelligence", response.data)
        self.assertIn(b"charisma", response.data)
        
        assert stats["strength"] >= 3 and stats["strength"] <=18
        assert stats["dexterity"] >= 3 and stats["dexterity"] <=19
        assert stats["constitution"] >=3 and stats ["constitution"] <=18
        assert stats["intelligence"] >=3 and stats ["intelligence"] <=18
        assert stats["charisma"] >= 3 and stats ["charisma"] <=20
        assert stats["wisdom"] >= 3 and stats ["wisdom"] <=18



    def test_generatehalfelf(self):
        stats = {"strength": 10, "dexterity": 10, "constitution": 10, "intelligence": 10, "wisdom": 10, "charisma": 10}


        response = self.client.post(url_for('generatestats'), data="Half-Elf")
        self.assertIn(b"wisdom", response.data)
        self.assertIn(b"strength", response.data)
        self.assertIn(b"dexterity", response.data)
        self.assertIn(b"constitution", response.data)
        self.assertIn(b"intelligence", response.data)
        self.assertIn(b"charisma", response.data)
        
        assert stats["strength"] >= 3 and stats["strength"] <=18
        assert stats["dexterity"] >= 3 and stats["dexterity"] <=18
        assert stats["constitution"] >=3 and stats ["constitution"] <=18
        assert stats["intelligence"] >=3 and stats ["intelligence"] <=19
        assert stats["charisma"] >= 3 and stats ["charisma"] <=20
        assert stats["wisdom"] >= 3 and stats ["wisdom"] <=19

    def test_generatedragonborn(self):
        stats = {"strength": 10, "dexterity": 10, "constitution": 10, "intelligence": 10, "wisdom": 10, "charisma": 10}

        response = self.client.post(url_for('generatestats'), data="Dragonborn")
        self.assertIn(b"wisdom", response.data)
        self.assertIn(b"strength", response.data)
        self.assertIn(b"dexterity", response.data)
        self.assertIn(b"constitution", response.data)
        self.assertIn(b"intelligence", response.data)
        self.assertIn(b"charisma", response.data)
        
        assert stats["strength"] >= 3 and stats["strength"] <=18
        assert stats["dexterity"] >= 3 and stats["dexterity"] <=18
        assert stats["constitution"] >=3 and stats ["constitution"] <=18
        assert stats["intelligence"] >=3 and stats ["intelligence"] <=18
        assert stats["charisma"] >= 3 and stats ["charisma"] <=19
        assert stats["wisdom"] >= 3 and stats ["wisdom"] <=19


    def test_generatedwarf(self):
        stats = {"strength": 10, "dexterity": 10, "constitution": 10, "intelligence": 10, "wisdom": 10, "charisma": 10}


        response = self.client.post(url_for('generatestats'), data="Dwarf")
        self.assertIn(b"wisdom", response.data)
        self.assertIn(b"strength", response.data)
        self.assertIn(b"dexterity", response.data)
        self.assertIn(b"constitution", response.data)
        self.assertIn(b"intelligence", response.data)
        self.assertIn(b"charisma", response.data)
        
        assert stats["strength"] >= 3 and stats["strength"] <=18
        assert stats["dexterity"] >= 3 and stats["dexterity"] <=18
        assert stats["constitution"] >=3 and stats ["constitution"] <=20
        assert stats["intelligence"] >=3 and stats ["intelligence"] <=18
        assert stats["charisma"] >= 3 and stats ["charisma"] <=18
        assert stats["wisdom"] >= 3 and stats ["wisdom"] <=18

    def test_generatehalfling(self):
        stats = {"strength": 10, "dexterity": 10, "constitution": 10, "intelligence": 10, "wisdom": 10, "charisma": 10}

        response = self.client.post(url_for('generatestats'), data="Halfling")
        self.assertIn(b"wisdom", response.data)
        self.assertIn(b"strength", response.data)
        self.assertIn(b"dexterity", response.data)
        self.assertIn(b"constitution", response.data)
        self.assertIn(b"intelligence", response.data)
        self.assertIn(b"charisma", response.data)
        
        assert stats["strength"] >= 3 and stats["strength"] <=18
        assert stats["dexterity"] >= 3 and stats["dexterity"] <=20
        assert stats["constitution"] >=3 and stats ["constitution"] <=18
        assert stats["intelligence"] >=3 and stats ["intelligence"] <=18
        assert stats["charisma"] >= 3 and stats ["charisma"] <=18
        assert stats["wisdom"] >= 3 and stats ["wisdom"] <=18


    def test_generatehalforc(self):
        stats = {"strength": 10, "dexterity": 10, "constitution": 10, "intelligence": 10, "wisdom": 10, "charisma": 10}

        response = self.client.post(url_for('generatestats'), data="Half-Orc")
        self.assertIn(b"wisdom", response.data)
        self.assertIn(b"strength", response.data)
        self.assertIn(b"dexterity", response.data)
        self.assertIn(b"constitution", response.data)
        self.assertIn(b"intelligence", response.data)
        self.assertIn(b"charisma", response.data)
        
        assert stats["strength"] >= 3 and stats["strength"] <=20
        assert stats["dexterity"] >= 3 and stats["dexterity"] <=18
        assert stats["constitution"] >=3 and stats ["constitution"] <=19
        assert stats["intelligence"] >=3 and stats ["intelligence"] <=18
        assert stats["charisma"] >= 3 and stats ["charisma"] <=18
        assert stats["wisdom"] >= 3 and stats ["wisdom"] <=18


    def test_generatekenku(self):
        stats = {"strength": 10, "dexterity": 10, "constitution": 10, "intelligence": 10, "wisdom": 10, "charisma": 10}
        
        response = self.client.post(url_for('generatestats'), data="Kenku")
        self.assertIn(b"wisdom", response.data)
        self.assertIn(b"strength", response.data)
        self.assertIn(b"dexterity", response.data)
        self.assertIn(b"constitution", response.data)
        self.assertIn(b"intelligence", response.data)
        self.assertIn(b"charisma", response.data)

        assert stats["strength"] >= 3 and stats["strength"] <=18
        assert stats["dexterity"] >= 3 and stats["dexterity"] <=20
        assert stats["constitution"] >=3 and stats ["constitution"] <=18
        assert stats["intelligence"] >=3 and stats ["intelligence"] <=18
        assert stats["charisma"] >= 3 and stats ["charisma"] <=18
        assert stats["wisdom"] >= 3 and stats ["wisdom"] <=19

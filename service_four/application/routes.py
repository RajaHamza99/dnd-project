from flask import redirect, url_for, request, Response
from application import app
import random, requests

@app.route('/', methods = ['GET', 'POST'])
@app.route('/name', methods = ['GET', 'POST'])
def generatename():
    name = request.data.decode('utf-8')
    elf_names = ["Wrandithas", "Baljeon", "Ianris", "Zumpetor", "Olowraek", "Advalur", "Trazeiros", "Virkian", "Qidan", "Luwraek", "Adleth", "Krisrora", "Bithyra", "Gilharice", "Grecyne", "Inatris", "Keyrel", "Caicaryn", "Greroris", "Qixisys"]
    tiefling_names = ["Rezire", "Garadius", "Valemon", "Zherakas", "Iamir", "Guerakas", "Kilron", "Harmony", "Innovation", "Hymn", "Rolyvia", "Oriborys", "Mismaia", "Seiripunith", "Velyola", "Sarqine", "Valza", "Uncommon", "Trickery", "Voyage"]
    human_names = ["Fahnin Zehro", "Melam Nulud", "Brukvork Deadshard", "Barstulm Mooncreek", "Fabral Glug", "Bral Stivredz", "Tulvom Orbpike", "Um Twobough", "Mihpion-Zad Nanskankhifk", "Beurhuef Biprueb", "Gandoutvoc Gevarginti", "Drerdoc Hemuri", "Jia Jain", "Iam Niaoy", "Ritemer Godreza", "Cranin Ozogal", "Judimah Zommid", "Namih Pahla", "Teelzenell Keentrap", "Jole Forestfang", "Choto Mag", "Kih Mamog", "Lovami Seawood", "Kafre Noseorb", "Rethani Jekrevehd", "Totho Meldrikt", "Sudhandra Nakanovza", "Hihi Emura", "Jai Waim", "Shai Nua", "Irb Ralurgal", "Mitf Pisonzas"]
    gnome_names = ["Bilgrim", "Dornan", "Yemorn", "Dornan", "Jeser", "Manlin", "Eniver", "Panacryn", "Willen", "Rasben", "Daphiniana", "Dorhana", "Banfi", "Welroe", "Niwyse", "Foldira", "Wrona", "Lilli", "Jogani", "Krigani"]
    satyr_names = ["Nalprath", "Narkerta", "Elroykos", "Narkdon", "Galreth", "Tavokas", "Quooros", "Cruster", "Dayethas", "Jaurian", "Enahanna", "Ollyn", "Brixis", "Albynn", "Jarwyse", "Faedys", "Illaxis", "Zentora", "Trilenae", "Leskiries"]
    half_elf_names = ["Panneiros", "Ianelor", "Dorlumin", "Frilsariph", "Zannan", "Elelor", "Graparin", "Belzaren", "Corfaelor", "Tralumin", "Aluhophe", "Saelmythe", "Yllmythe", "Sylstine", "Hozenya", "Aluzenya", "Wolxaris", "Bynhophe", "Yeshophe", "Xyrenyphe"]

    if name == 'Elf':
        choose_name = random.choice(elf_names)
    elif name == 'Tiefling':
        choose_name = random.choice(tiefling_names)
    elif name == 'Human':
        choose_name = random.choice(human_names)
    elif name == 'Gnome':
        choose_name = random.choice(gnome_names)
    elif name == 'Satyr':
        choose_name = random.choice(satyr_names)
    elif name == 'Half-Elf':
        choose_name = random.choice(half_elf_names)
    return Response(choose_name, mimetype='text/plain') 

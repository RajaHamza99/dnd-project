from flask import redirect, url_for, request, Response, jsonify
from application import app
import random, requests

@app.route('/name', methods = ['POST'])
def generatename():
    race = request.data.decode('utf-8')
    print("hello" + race) 
    elf_names = ["Wrandithas", "Baljeon", "Ianris", "Zumpetor", "Olowraek", "Advalur", "Trazeiros", "Virkian", "Qidan", "Luwraek", "Adleth", "Krisrora", "Bithyra", "Gilharice", "Grecyne", "Inatris", "Keyrel", "Caicaryn", "Greroris", "Qixisys"]
    tiefling_names = ["Rezire", "Garadius", "Valemon", "Zherakas", "Iamir", "Guerakas", "Kilron", "Harmony", "Innovation", "Hymn", "Rolyvia", "Oriborys", "Mismaia", "Seiripunith", "Velyola", "Sarqine", "Valza", "Uncommon", "Trickery", "Voyage"]
    human_names = ["Fahnin Zehro", "Melam Nulud", "Brukvork Deadshard", "Barstulm Mooncreek", "Fabral Glug", "Bral Stivredz", "Tulvom Orbpike", "Um Twobough", "Mihpion-Zad Nanskankhifk", "Beurhuef Biprueb", "Gandoutvoc Gevarginti", "Drerdoc Hemuri", "Jia Jain", "Iam Niaoy", "Ritemer Godreza", "Cranin Ozogal", "Judimah Zommid", "Namih Pahla", "Teelzenell Keentrap", "Jole Forestfang", "Choto Mag", "Kih Mamog", "Lovami Seawood", "Kafre Noseorb", "Rethani Jekrevehd", "Totho Meldrikt", "Sudhandra Nakanovza", "Hihi Emura", "Jai Waim", "Shai Nua", "Irb Ralurgal", "Mitf Pisonzas"]
    gnome_names = ["Bilgrim", "Dornan", "Yemorn", "Dornan", "Jeser", "Manlin", "Eniver", "Panacryn", "Willen", "Rasben", "Daphiniana", "Dorhana", "Banfi", "Welroe", "Niwyse", "Foldira", "Wrona", "Lilli", "Jogani", "Krigani"]
    satyr_names = ["Nalprath", "Narkerta", "Elroykos", "Narkdon", "Galreth", "Tavokas", "Quooros", "Cruster", "Dayethas", "Jaurian", "Enahanna", "Ollyn", "Brixis", "Albynn", "Jarwyse", "Faedys", "Illaxis", "Zentora", "Trilenae", "Leskiries"]
    half_elf_names = ["Panneiros", "Ianelor", "Dorlumin", "Frilsariph", "Zannan", "Elelor", "Graparin", "Belzaren", "Corfaelor", "Tralumin", "Aluhophe", "Saelmythe", "Yllmythe", "Sylstine", "Hozenya", "Aluzenya", "Wolxaris", "Bynhophe", "Yeshophe", "Xyrenyphe"]
    dragonborn_names = ["Jinkax Ochek", "Nesjhan Felkejaros", "Vrakqrin Clearrhidiash", "Saseth Nyuchoth", "Yorfras Drankendualash", "Dolin Cuustic", "Lumirakas Errhunduth", "Pawarum Curjed", "Narfarn Myimphostudak", "Faerfras Thapoc", "Opora Dalmishkmuril", "Hawophyl Vechaathic", "Ushirann Nyelmiak", "Loravyre Guacithus", "Erlifyire Fenkashtondil", "Nadalynn Cluldriash", "Welsigil Tultus", "Loragissa Uthtijellec", "Koriel Shunkuth", "Ophihymm Shuchuas"]
    dwarf_names = ["Bunkyl", "Bundrum", "Galkahm", "Bhargran", "Tormar", "Gralmir", "Berman", "Thermun", "Gramdram", "Bharnom", "Nalgwyn", "Jinmura", "Braenwynn", "Brillethiel", "Sarvian", "Kaittin", "Bronria", "Nasswaen", "Brillera", "Barbera"]
    halfling_names = ["Kaseon", "Jokas", "Tebul", "Urider", "Conkas", "Kasrin", "Panton", "Barlos", "Osbin", "Gardal", "Ledove", "Lecey", "Ariree", "Idani", "Paesira", "Anara", "Levyre", "Pruwyse", "Oradrey", "Therjen"]
    half_orc_names = ["Lumurimm", "Drigar", "Gadash", "Kumash", "Harask", "Oguotar", "Gramabak", "Koranars", "Zurigak", "Grumurth", "Zanid", "Zanegur", "Rez", "Ekuzira", "Zonisha", "Kerazara", "Alogum", "Gijunchu", "Zunamar", "Rahegri"]
    kenku_names = ["Shaker", "Bubbler", "Chimer", "Swatter", "Crow Call", "Horse Blow", "Pig Snort", "Saw Wobble", "Mallet Smash", "Wood Drop"]


    if race == 'Elf':
        choose_name = random.choice(elf_names)
    elif race == 'Tiefling':
        choose_name = random.choice(tiefling_names)
    elif race == 'Human':
        choose_name = random.choice(human_names)
    elif race == 'Gnome':
        choose_name = random.choice(gnome_names)
    elif race == 'Satyr':
        choose_name = random.choice(satyr_names)
    elif race == 'Half-Elf':
        choose_name = random.choice(half_elf_names)
    elif race == "Dragonborn":
        choose_name = random.choice(dragonborn_names)
    elif race == "Dwarf":
        choose_name = random.choice(dwarf_names)
    elif race == "Halfling":
        choose_name = random.choice(halfling_names)
    elif race == "Half-Orc":
        choose_name = random.choice(half_orc_names)
    elif race == "Kenku":
        choose_name = random.choice(kenku_names)
    
    return Response(choose_name, mimetype='text/plain')


@app.route('/stats', methods = ['GET', 'POST'])
def generatestats():
    stats = {"strength": random.randint(3,18), "dexterity": random.randint(3,18), "constitution": random.randint(3,18), "intelligence": random.randint(3, 18), "wisdom": random.randint(3, 18), "charisma": random.randint(3,18)}


    race = request.data.decode('utf-8')

    if race == "Elf":
        stats["dexterity"] += 2

    elif race == "Tiefling":
        stats["charisma"] += 2
        stats["intelligence"] += 1

    elif race == "Human":
        stats["strength"] += 1
        stats["dexterity"] += 1
        stats["constitution"] += 1
        stats["intelligence"] += 1
        stats["wisdom"] += 1
        stats["charisma"] += 1

    elif race == "Gnome":
        stats["intelligence"] += 2

    elif race == "Satyr":
        stats["charisma"] += 2
        stats["dexterity"] += 1

    elif race == "Half-Elf":
        stats["charisma"] += 2
        stats["wisdom"] += 1
        stats["intelligence"] += 1

    elif race == "Dragonborn":
        stats["strength"] += 2
        stats["charisma"] += 1

    elif race == "Dwarf":
        stats["constitution"] += 2

    elif race == "Halfling":
        stats["dexterity"] += 2

    elif race == "Half-Orc":
        stats["strength"] += 2
        stats["constitution"] += 1

    elif race == "Kenku":
        stats["dexterity"] += 2
        stats["wisdom"] += 1

    return jsonify(stats)

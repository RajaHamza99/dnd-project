from flask import redirect, url_for, request, Response
from application import app
import random, requests

@app.route('/', methods = ['GET', 'POST'])
@app.route('/race', methods = ['GET', 'POST'])
def generaterace():
    races = ["Dragonborn", "Dwarf", "Halfling", "Human", "Half-Orc", "Kenku"]
    choose_race = random.choice(races)
    return Response(choose_race, mimetype='text/plain')

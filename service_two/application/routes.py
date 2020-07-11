from flask import redirect, url_for, request, Response
from application import app
import random, requests

@app.route('/', methods = ['GET', 'POST'])
@app.route('/class', methods = ['GET', 'POST'])
def generateclass():
    classes = ["Bard", "Cleric", "Druid", "Paladin", "Ranger", "Sorcerer", "Warlock", "Wizard"]
    choose_class = random.choice(classes)
    return Response(choose_class, mimetype='text/plain')

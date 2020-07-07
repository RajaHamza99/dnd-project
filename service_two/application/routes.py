from flask import redirect, url_for, request, Response
from application import app
import random, requests

@app.route('/', methods = ['GET', 'POST'])
@app.route('/class2', methods = ['GET', 'POST'])
def generateclass():
    classes = ["Barbarian", "Fighter", "Monk", "Rogue", "Blood Hunter"]
    choose_class = random.choice(classes)
    return Response(choose_class, mimetype='text/plain')

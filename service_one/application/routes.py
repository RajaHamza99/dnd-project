from flask import render_template, request, url_for, Response, jsonify, json
from application import app, db
from application.forms import GenerateForm
from application.models import characters
import random, requests, time


@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():
    form = GenerateForm()
    if request.method == 'GET':
        return render_template('home.html', title='Class', form=form)
    if form.validate_on_submit():
        get_class = requests.get('http://service_two:5001/class2')
        character_class = get_class.text
        get_race = requests.get('http://service_three:5002/race2')
        character_race = get_race.text
        name = requests.post('http://service_four:5003/name', data=character_race)
        character_name = name.text
        stat = requests.post('http://service_four:5003/stats', data=character_race)
        stat_dict = json.loads(stat.text)
        data = characters(
                name = character_name,
                char_class = character_class,
                char_race = character_race)
        db.session.add(data)
        db.session.commit()


        all_characters = characters.query.all()
        return render_template('home.html', title='Class', form=form, classes=character_class, race=character_race, name=character_name, stats=stat_dict, all_characters=all_characters)

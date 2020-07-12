from application import app
from application.forms import GenerateForm, AddForm
from sqlalchemy import desc
import random, requests, time


@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():
    form = GenerateForm()
    if request.method == 'GET':
        return render_template('home.html', title='Class', form=form)
    if form.validate_on_submit():
        get_class = requests.get('http://service_two:5001/class')
        character_class = get_class.text
        get_race = requests.get('http://service_three:5002/race')
        character_race = get_race.text
        name = requests.post('http://service_four:5003/name', data=character_race)
        character_name = name.text
        return render_template('home.html', title='Class', form=form, classes=character_class, race=character_race, name=character_name)

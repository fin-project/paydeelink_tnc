
from flask import render_template
from project import app

@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('TnC.html')


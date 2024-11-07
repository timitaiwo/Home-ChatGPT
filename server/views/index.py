from flask import render_template, Blueprint

index : Blueprint = Blueprint('index', __name__)

@index.route('/')
def homepage():
    return render_template('index.html')

from flask import render_template

from api import app

@app.route('/')
def index():
    return 'Hello world home'


@app.route('/about')
def about():
    return 'hello world about us'

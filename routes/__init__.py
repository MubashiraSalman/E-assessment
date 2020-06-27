from flask import abort, redirect, request, render_template
from app import app
from models.register import Register
from db import db


@app.route('/', methods=['GET'])
def index_get():
    return render_template('index.html')


@app.route('/index.html', methods=['GET'])
def index_get2():
    return render_template('index.html')


@app.route('/login.html', methods=['GET'])
def login_get():
    return render_template('login.html')

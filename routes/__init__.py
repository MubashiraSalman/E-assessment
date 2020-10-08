from flask import Flask, abort, redirect, request, render_template, flash
from models.register import Register
from app import app
import webimage
import fr
import win32api
from subprocess import *


@app.route('/', methods=['GET'])
def index_get():
    return render_template('index.html')


@app.route('/index.html', methods=['GET'])
def index_get2():
    return render_template('index.html')


@app.route('/login.html', methods=['POST'])
def signup():
    email = request.form['email']
    password = request.form['password']
    file = request.files['filename']
    new_file = file.read()

    user = Register.query.filter_by(
        email=email).first()  # if this returns a user, then the email already exists in database

    if user:  # if a user is found, we want to redirect back to signup page so user can try again
        return redirect('/index.html')

    Register.insert_in_db(email, password, new_file)
    return render_template('/login.html')


@app.route('/login.html', methods=['GET'])
def login_get():
    return render_template('login.html')


@app.route('/test.html', methods=['POST'])
def login_post():
    email = request.form['email']
    password = request.form['password']

    user = Register.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password and compare it to the password in the database
    if not user or not (user.password == password):
        return redirect('/login.html')  # if the user doesn't exist or password is wrong, reload the page
    else:
        webimage.image_cap()
        data = user.photo
        with open('photo.jpg', 'wb') as file:
            file.write(data)
        result = fr.image_compare()
        if result:
            win32api.MessageBox(0, 'Identity Matched', 'Alert')
            return redirect('/start.html')
        else:
            win32api.MessageBox(0, 'Identity Not Matched', 'Alert')
            return redirect('/login.html')


@app.route('/start.html', methods=['GET'])
def start_test():
    p = Popen('python ./testt.py')
    return render_template('start.html')


@app.route('/testpage.html', methods=['GET'])
def start_test2():
    return render_template('test.html')
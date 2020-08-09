from flask import Flask, abort, redirect, request, render_template, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app import app
from models.register import Register
from db import db
import webimage
import base64
import cv2


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

    user = Register.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

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
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not (user.password == password):
        return redirect('/login.html')  # if the user doesn't exist or password is wrong, reload the page
    else:
        webimage.image_cap()
        data = user.photo
        # with open("imageToSave.png", "wb") as fh:
        #     fh.write(base64.decodebytes(img))
        # img.decode('base64')
        # cv2.imwrite(filename='imagefromdb.jpg', img=img)
        with open('photo.jpg', 'wb') as file:
            file.write(data)
        return redirect('/test.html')


@app.route('/test.html', methods=['GET'])
def start_test():
    return render_template('/test.html')



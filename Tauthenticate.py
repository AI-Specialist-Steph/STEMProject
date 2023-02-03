from flask import Blueprint, render_template,request, flash, redirect, url_for
from .databaseMod import Client
from werkzeug.security import generate_password_hash, check_password_hash
from . import blobDb
from flask_login import login_user, login_required, logout_user, login_remembered, current_user

Tauthenticate = Blueprint('Tauthenticate', __name__)

#using http request methods to retreive and make request. This enables the page to reload when user does not input data

@Tauthenticate.route('/t.login', methods=['GET', 'POST'])
def teacher_login():
    if request.method == 'POST':
        Email = request.form.get('staffEmail')
        password = request.form.get('Tpassword')

        client = Client.query.filter_by(Email=Email).first()
        if client:
            if check_password_hash(client.password, password):
                flash('Login Successful', category='exception')
                login_user(Client, remember=True)
                login_remembered()
                return redirect(url_for('home.Tdashboard'))
            else:
                flash('Incorrect details', category='error')
        else:
            flash('Email cannot be found, sign up and try again', category='error')
    return render_template("tLogin.html", client=current_user)

@Tauthenticate.route('/t.logout')
@login_required
def teacher_logout():
    logout_user()
    return redirect(url_for('Tauthenticate.teacher_login'))

@Tauthenticate.route('/t-sign-up', methods=['GET', 'POST'])
def teacher_sign_up():
    if request.method == 'POST' : #differenciating between the POST and GET request
        staffEmail = request.form.get('staffEmail')
        Name = request.form.get('Name')
        TBirthday = request.form.get('TBirthday')
        Tpassword =request.form.get('Tpassword')
        Tpassword00 = request.form.get('Tpassword00')

        client = Client.query.filter_by(Email=staffEmail).first()
        if client:
            flash('email already exists, log in', category='error')
        elif len(staffEmail) < 9:
            flash('enter valid details', category='error')
        elif Tpassword != Tpassword00:
            flash('Passwords do not match', category='error')
        elif TBirthday == '2022':
            flash('error', category='error')
        elif len(Name) < 1:
            flash('error', category='error')
        elif len(Tpassword) >15:
            flash('Password must be less than 15 characters', category='error')
        else:
            flash('ACCOUNT CREATED', category='exception')
            new_client = Client(Email=staffEmail,
                                Name=Name,
                                date=TBirthday,
                                password=generate_password_hash(Tpassword, method='sha256'))
            blobDb.session.add(new_client)
            blobDb.session.commit()
            return redirect(url_for('home.Tdashboard'))

    return render_template("tSignUp.html", client=current_user)

#Login and sign up route for teacher works
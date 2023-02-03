from flask import Blueprint, render_template,request, flash, redirect, url_for
from .databaseMod import Client
from werkzeug.security import generate_password_hash, check_password_hash
from . import blobDb
from flask_login import login_user, login_required, logout_user, login_remembered, current_user

authenticate = Blueprint('authenticate', __name__)

#using http request methods to retreive and make request. This enables the page to reload when user does not input data
@authenticate.route('/s.login', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        Email = request.form.get('studentEmail')
        password = request.form.get('Spassword')

        client = Client.query.filter_by(Email=Email).first()
        if client:
            if check_password_hash(client.password, password):
                flash('Login Successful', category='exception')
                login_user(Client, remember=True)
                login_remembered()
                return redirect(url_for('endP.dashboard'))
            else:
                flash('Incorrect details', category='error')
        else:
            flash('Email cannot be found, sign up and try again', category='error')


    return render_template("sLogin.html", client=current_user)


@authenticate.route('/s.logout')
@login_required
def student_logout():
    logout_user()
    return redirect(url_for('authenticate.student_login'))

@authenticate.route('/s-sign-up', methods=['GET', 'POST']) #student sign up
def student_sign_up():
    if request.method == 'POST' : #differenciating between the POST and GET request
        studentEmail = request.form.get('studentEmail')
        Name = request.form.get('Name')
        SBirthday = request.form.get('SBirthday')
        Spassword =request.form.get('Spassword')
        Spassword00 = request.form.get('Spassword00')

        client = Client.query.filter_by(Email=studentEmail).first()
        if client:
            flash('email already exists, log in', category='error')

        elif len(studentEmail) < 9:
            flash('enter valid details', category='error')
        elif Spassword != Spassword00:
            flash('Passwords do not match', category='error')
        elif SBirthday == '2022':
            flash('error', category='error')
        elif len(Name) < 1:
            flash('error', category='error')
        elif len(Spassword) >15:
            flash('Password must be less than 15 characters', category='error')
        else:


            new_client = Client(Email=studentEmail,
                                   Name=Name,
                                   date=SBirthday,
                                   password=generate_password_hash(Spassword, method='sha256'))
            blobDb.session.add(new_client)
            blobDb.session.commit()
            login_user(new_client, remember=True)
            flash('ACCOUNT CREATED', category='exception')
            return redirect(url_for('endP.dashboard'))


    return render_template("sSignUp.html", client=current_user)   #as per the requirement, only subscribers can access blobsmaths

#login and sign up routes for student works
#request allows web to get info that was filled out by the user
#flash, shows message on the screen
#https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/
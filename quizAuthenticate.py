from flask import Blueprint, render_template

quizAuthenticate = Blueprint('quizAuthenticate', __name__)

@quizAuthenticate.route('/sub.science')
def subject_science():
    return "<p>Science</p>"

@quizAuthenticate.route('/sub.technology')
def subject_technology():
    return "<p>Technology</p>"

@quizAuthenticate.route('/sub.engineering')
def subject_engineering():
    return "<p>Engineering</p>"

@quizAuthenticate.route('/sub.maths')
def subject_maths():
    return render_template("subMaths.html")


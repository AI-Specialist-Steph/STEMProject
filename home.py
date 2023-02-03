from flask import Blueprint
from flask import render_template
from flask_login import  login_required, login_remembered, current_user

home = Blueprint('home', __name__,template_folder='Strings')

#defining the function
@home.route('/Tdashboard')
@login_required
def Tdashboard():

    return render_template('Tdashboard.html', client=current_user)
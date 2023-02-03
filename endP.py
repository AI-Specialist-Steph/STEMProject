from flask import Blueprint
from flask import render_template
from flask_login import  login_required, current_user

endP = Blueprint('endP', __name__,template_folder='Strings')

#defining the function
@endP.route('/') #called a decorator #go to the main page of the website
@login_required
def dashboard():
    return render_template('dashboard.html', client=current_user)






#I want Blobsmath to be an image instead of a text "<h1>Blobsmath</h1>"
#student user will be redirected to this page after sign up/log in
#student user should be redirected to a start quiz page which will be available on dashboard

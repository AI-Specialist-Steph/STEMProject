from flask import Blueprint, render_template
from flask_login import  login_required, current_user

vanilla = Blueprint('vanilla', __name__,template_folder='Strings')

@vanilla.route('/redirectVanilla', methods=['GET', 'POST'])
def redirectVanilla():
    return render_template("redirectVanilla.html", client=current_user)



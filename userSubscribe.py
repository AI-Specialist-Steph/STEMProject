from flask import Blueprint, render_template, request, flash, redirect, url_for
from .databaseMod import Client
from flask_login import current_user, login_user
from . import blobDb


userSubscribe = Blueprint('userSubscribe', __name__)


@userSubscribe.route('/subscribe', methods=['GET', 'POST'])
def user_subscribe():
    if request.method == 'POST':
        userEmail = request.form.get('userEmail')
        client = Client.query.filter_by(Email=userEmail).first()
        if client:
            flash('You have already subscribed, Log In', category='error')
        else:
            flash('Thanks for subscribing, redirecting to Log in page', category='error')
            new_client = Client(Email=userEmail)
            blobDb.session.add(new_client)
            blobDb.session.commit()


            return redirect(url_for('vanilla.redirectVanilla'))

    return render_template("subscribe.html", client=current_user)

#if user is already logged in, they should be redirected to the log in page

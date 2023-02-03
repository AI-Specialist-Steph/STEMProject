from flask import Flask
#creating a database with sql alchemy but it can also be connected to an already made database
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

blobDb = SQLAlchemy()
DATABASE_Name = "blobmaths.db"






def create_web():
    web = Flask(__name__) #represents the name of the application ppackage, used by flask to identify templates, static assests instance folder
    web.config['SECRET_KEY'] = 'only accessible by high officials'
    #file to store details in
    web.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASE_Name}' #database is stored in DATABASE_Name
    blobDb.init_app(web) #init_app is a keyword, stating that this database would be used for this web

    login_manager = LoginManager()
    login_manager.login_view = 'userSubscribe.user_subscribe'                                       #where should the user be redirected to if log in is required
    login_manager.init_app(web)



    from .endP import endP
    from .home import home
    from .authenticate import authenticate
    from .Tauthenticate import Tauthenticate
    from .quizAuthenticate import quizAuthenticate
    from .userSubscribe import userSubscribe
    from .vanilla import vanilla


    web.register_blueprint(endP, url_prefix='/')
    web.register_blueprint(home, url_prefix='/')
    web.register_blueprint(vanilla, url_prefix='/')

    web.register_blueprint(authenticate, url_prefix='/')
    web.register_blueprint(Tauthenticate, url_prefix='/')
    web.register_blueprint(quizAuthenticate, url_prefix='/')
    web.register_blueprint(userSubscribe, url_prefix='/')

    # database

    from .databaseMod import Client

    @login_manager.user_loader
    def load_client(id):
        return Client.query.get(int(id)) #how we load a user




    with web.app_context():
        blobDb.create_all()

    return web


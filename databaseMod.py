#database for user info (subscribe, log in, sign up)
#database for subjects(class activities)
#database for uploaded materials by the teachers

from . import blobDb
from flask_login import UserMixin #checks if user credentials are valid. ref: stackoverflow

#when you want to store a different kind of object- define the name of the object and have it inherit from blobDb.Model

#class Subject(blobDb.Model):

class Client (blobDb.Model, UserMixin):
    id = blobDb.Column(blobDb.Integer, primary_key=True)  #creating unique identifiers for each user
    Email = blobDb.Column(blobDb.String(300), unique=True) #two users cant have the same email
    password = blobDb.Column(blobDb.String(300))
    Name = blobDb.Column(blobDb.String(300))
    date = blobDb.Column(blobDb.String(50))



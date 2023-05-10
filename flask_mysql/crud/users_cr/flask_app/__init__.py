from flask import Flask
from flask_app.controllers import users

app = Flask(__name__)
app.secret_key="rLBdVPV2Fsgxrgp7vANv"

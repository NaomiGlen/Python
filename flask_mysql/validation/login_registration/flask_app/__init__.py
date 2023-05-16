from flask import Flask
app = Flask(__name__)
app.secret_key = "6Jpb4U4Pet559A4DeV5u"

from flask_app.controllers import users
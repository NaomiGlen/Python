from flask import Flask
app = Flask(__name__)
app.secret_key="qdzDyedjPVedMgcrg8K9"

from flask_app.controllers import users
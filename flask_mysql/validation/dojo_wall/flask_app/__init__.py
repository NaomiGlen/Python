from flask import Flask
app = Flask(__name__)
app.secret_key = "yPvrvXZidcHWDuUYm08V"

from flask_app.controllers import users, posts

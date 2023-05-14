from flask import Flask
app = Flask(__name__)
app.secret_key="zZh4Jnj7x0fCPn604DxK"

from flask_app.controllers import cookies
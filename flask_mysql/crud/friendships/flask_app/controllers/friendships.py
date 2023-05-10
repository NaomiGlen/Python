from flask_app import app
from flask import render_template, redirect,request
from flask_app.models.friendship import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add/user', methods=['POST'])
def create_user():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name']
    }
    user_id=User.save(data)
    return redirect('/')

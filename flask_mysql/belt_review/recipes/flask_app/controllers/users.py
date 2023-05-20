from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/user/login')

@app.route('/user/login')
def login():
    if 'user_id' in session:
        return redirect('/dashboard')
    return render_template('index.html')

@app.route('/user/login/process', methods=['POST'])
def login_success():
    user = User.valid_login(request.form)
    if not user:
        return redirect('/user/login')
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/register/user/process', methods=['POST'])
def register_success():
    if not User.valid_registration(request.form):
        return redirect('/user/login')
    user_id = User.save(request.form)
    session['user_id'] = user_id
    return redirect('/dashboard')

@app.route('/user/logout')
def logout():
    if 'user_id' in session:
        session.pop('user_id')
        return redirect('/user/login')
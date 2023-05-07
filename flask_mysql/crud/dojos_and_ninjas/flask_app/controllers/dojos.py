from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def dojos():
    return render_template("dojos.html",all_dojos=Dojo.get_all())

@app.route('/create/dojo', methods = ['POST'])
def create_dojo():
    data = {
        "name" : request.form['name']
    }
    Dojo.save(data)
    return redirect('/')

@app.route('/show/<int:dojo_id>')
def detail_dojo(dojo_id):
    data = {
        'id' : dojo_id
    }

@app.route('/show/dojo')
def dojo_ninjas():
    return render_template("show_dojo.html",dojo_ninjas=Dojo.get_dojo_with_ninjas())

@app.route('/new/ninja')
def new_ninja():
    return render_template("new_ninja.html")

@app.route('/create/ninja', methods = ['POST'])
def create_ninja():
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age'],
    }
    Ninja.save(data)
    return redirect('/')

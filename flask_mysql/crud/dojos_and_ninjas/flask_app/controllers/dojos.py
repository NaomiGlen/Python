from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask_app.controllers import ninjas

@app.route('/')
def index():
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
    return render_template("show_dojo.html", dojo_ninjas = Dojo.get_dojo_with_ninjas(data))

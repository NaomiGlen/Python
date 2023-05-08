from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo, ninja

@app.route ('/ninjas')
def ninjas():
    return render_template('ninja.html', dojos=dojo.Dojo.get_all())

@app.route('/create/ninja', methods = ['POST'])
def create_ninja():
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age'],
    }
    ninja.Ninja.save(data)
    return redirect('/')

@app.route('/new/ninja')
def new_ninja():
    return render_template("new_ninja.html",all_dojos=dojo.Dojo.get_all())

@app.route('/ninjas/edit/<ninja_id>')
def edit_pate(ninja_id):
    return render_template('edit_ninja.html')

@app.route('/ninjas/delete/<ninja_id>/<dojo_ninjas.dojo_id>')
def delete_ninja(ninja_id):
    print("Deleting ninja with id:", ninja_id)
    return redirect(f'/dojos/{dojo_ninjas.dojo_id}')

@app.route('/ninjas/update', methods=["POST"])
def update_ninja():
    print("Update to update ninja with data:", request.form)
    return 
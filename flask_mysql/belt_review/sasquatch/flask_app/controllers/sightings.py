from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.user import User
from flask_app.models.sighting import Sighting

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/user/login')
    user = User.get_by_id({"id": session["user_id"]})
    if not user:
        return redirect('/user/logout')
    return render_template('dashboard.html', user=user, sightings=Sighting.get_all())

@app.route('/sightings/new')
def new_sighting():
    if 'user_id' not in session:
            return redirect('/user/login')
    return render_template('new_sighting.html', user=User.get_by_id({"id": session["user_id"]}))

@app.route('/sightings/new/process', methods=['POST'])
def new_sighting_process():
    if 'user_id' not in session:
                return redirect('/user/login')
    if not Sighting.validate_sighting(request.form):
        return redirect('/sighting/new')
    data = {
        'user_id': session["user_id"],
        'location': request.form['location'],
        'content': request.form['content'],
        'sight_date': request.form['sight_date'],
        'num_sasquatch': request.form['num_sasquatch'],
    }
    Sighting.save(data)
    return redirect('/dashboard')

@app.route('/sightings/<int:id>')
def view_sighting(id):
    if 'user_id' not in session:
            return redirect('/user/login')
    return render_template('view_sighting.html', sighting=Sighting.get_by_id({"id": id}), user=User.get_by_id({"id": session["user_id"]}))

@app.route('/sightings/edit/<int:id>')
def edit_sighting(id):
    if 'user_id' not in session:
        return redirect('/user/login')
    return render_template('edit_sighting.html', sighting=Sighting.get_by_id({"id": id}), user=User.get_by_id({"id": session["user_id"]}))

@app.route('/sightings/edit/process/<int:id>', methods=['POST'])
def edit_sighting_process(id):
    if 'user_id' not in session:
        return redirect('/user/login')
    if not Sighting.validate_sighting(request.form):
            return redirect('/sighting/edit/{id}')
    data = {
        'id': id,
        'location': request.form['location'],
        'content': request.form['content'],
        'sight_date': request.form['sight_date'],
        'num_sasquatch': request.form['num_sasquatch'],
    }
    Sighting.update(data)
    return redirect('/dashboard')

@app.route('/sightings/delete/<int:id>')
def delete_sighting(id):
    if 'user_id' not in session:
            return redirect('/user/login')
    Sighting.delete({"id":id})
    return redirect('/dashboard')
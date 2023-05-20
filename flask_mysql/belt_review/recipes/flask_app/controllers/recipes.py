from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/user/login')
    user = User.get_by_id({"id": session["user_id"]})
    if not user:
        return redirect('/user/logout')
    return render_template('dashboard.html', user=user, recipes=Recipe.get_all())

@app.route('/recipes/new')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/user/login')
    return render_template('new_recipe.html')

@app.route('/recipes/new/process', methods=['POST'])
def new_recipe_process():
    if 'user_id' not in session:
        return redirect('/user/login')
    if not Recipe.valid_recipe(request.form):
        return redirect('/recipes/new')
    data = {
        'user_id': session['user_id'],
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'submit_date': request.form['submit_date'],
        'under_30': request.form['under_30'],
    }
    Recipe.save(data)
    return redirect('/dashboard')

@app.route('/recipes/<int:id>')
def view_recipe(id):
    if 'user_id' not in session:
        return redirect('/user/login')
    return render_template('view_recipe.html', recipe=Recipe.get_by_id({"id": id}))

@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/user/login')
    return render_template('edit_recipe.html', recipe=Recipe.get_by_id({"id": id}))

@app.route('/recipes/edit/process/<int:id>', methods=['POST'])
def edit_recipe_process(id):
    if 'user_id' not in session:
            return redirect('/user/login')
    if not Recipe.valid_recipe(request.form):
        return redirect('/recipes/edit/{id}')
    data = {
        'id': id,
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'submit_date': request.form['submit_date'],
        'under_30': request.form['under_30'],
        }
    Recipe.update(data)
    return redirect('/dashboard')

@app.route('/recipes/delete/<int:id>')
def delete_recipe(id):
    if 'user_id' not in session:
            return redirect('/user/login')
    Recipe.delete({"id": id})
    return redirect('/dashboard')
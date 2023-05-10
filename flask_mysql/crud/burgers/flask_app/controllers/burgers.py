from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.burger import Burger
from flask_app.models.restaurant import Restaurant
from flask_app.models.topping import Topping

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create/burger',methods=['POST'])
def create_burger():
    data = {
        "name":request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "calories": request.form['calories']
    }
    if not Burger.validate_burger(request.form):
        return redirect('/')
    Burger.save(data)
    return redirect('/burgers')

@app.route('/burgers')
def burgers():
    return render_template("results.html",burgers=Burger.get_all())

@app.route('/show/<int:burger_id>')
def detail_page(burger_id):
    data = {
        'id': burger_id
    }
    return render_template("details_page.html",burger=Burger.get_one(data))

@app.route('/edit_page/<int:burger_id>')
def edit_page(burger_id):
    data = {
        'id': burger_id
    }
    return render_template("edit_page.html", burger = Burger.get_one(data))

@app.route('/update/<int:burger_id>', methods=['POST'])
def update(burger_id):
    data = {
        'id': burger_id,
        "name":request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "calories": request.form['calories']
    }
    Burger.update(data)
    return redirect(f"/show/{burger_id}")

@app.route('/delete/<int:burger_id>')
def delete(burger_id):
    data = {
        'id': burger_id,
    }
    Burger.destroy(data)
    return redirect('/burgers')
from flask_app import app
from flask import render_template,redirect,flash,request,session
from flask_app.models.cookie import Cookie

@app.route('/')
@app.route('/cookie')
def orders():
    orders = Cookie.get_all()
    print(orders)
    return render_template("index.html", orders = orders)

@app.route('/cookie/new')
def new_order():
    return render_template("new_order.html")

@app.route('/cookie', methods=['POST'])
def create_order():
    order_info = request.form
    if not Cookie.is_valid_order(order_info):
        print("FAILED")
        return redirect('/cookie/new')
    Cookie.save(order_info)
    print("SUCCESS")
    return redirect('/cookie/new')

@app.route('/cookie/edit/<int:order_id>')
def edit(order_id):
    order=Cookie.get_by_id(order_id)
    return render_template("edit_order.html", order=order)

@app.route('/cookie/edit/<int:order_id>', methods=['POST'])
def update(order_id):
    order_info = request.form
    if not Cookie.is_valid_order(order_info):
        print("FAILED")
        return redirect(f"/cookie/edit/{order_id}")
    Cookie.update(order_info)
    print("SUCCESS")
    return redirect('/')
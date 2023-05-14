from flask_app import app
from flask import render_template,redirect,flash,request,session
from flask_app.models.user import User

@app.route('/')
def users():
    friends = User.get_all()
    print(friends)
    return render_template("users.html", all_friends = friends)

@app.route('/user/new')
def new():
    return render_template("new_user.html")

@app.route('/user/create',methods=['POST'])
def create():
    user_info = request.form
    if User.is_valid_user(user_info):
        User.save(user_info)
        print("Pass")
        return redirect('/')
    print("FAIL")
    return redirect('/user/new')

@app.route('/user/show/<int:id>')
def show(id):
    data = {
        "id":id
    }
    return render_template("show_user.html",user=User.get_one(data))

@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        "id":id
    }
    return render_template("edit_user.html",user=User.get_one(data))

@app.route('/user/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/')

@app.route('/user/delete/<int:id>')
def delete(id):
    data={ 
        'id': id
    }
    User.delete(data)
    return redirect('/user')

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    return redirect('/dashboard')
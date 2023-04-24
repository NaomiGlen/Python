from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', phrase="hello",times=5)

@app.route('/success')
def success():
    return "success"

@app.route('/lists')
def render_lists():
    student_info=[
        {'name':'Michael','age':35},
        {'name':'John','age':30},
        {'name':'Mark','age':25},
        {'name':'KB','age':27}
    ]
    return render_template("lists.html",random_numbers=[3,1,5],students=student_info)

#What if we wanted to be able to say "Hello, Michael" or "Hello, Amy" or "Hello, Wes"?
#We could make three routes, but that feels pretty repetitive.
#Also, every time we want to include someone else, we would need to create a new route.
#This is a great opportunity to add variable rules to our routes.
#For the example above, we could make the name a variable, like so:
#@app.route('/hello/<name>')
#def hello(name):
#    print(name)
#i    return "Hello, "+ name

#We can add as many of these as we need, giving each variable a different name:
#@app.route('/users/<username>/<id>')
#def show_user_profile(username, id):
#    print(username)
#    print(id)
#    return "username: " + username + "id: " + id

if __name__=="__main__":
    app.run(debug=True)
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/success')
def success():
    return "success"

#What if we wanted to be able to say "Hello, Michael" or "Hello, Amy" or "Hello, Wes"?
#We could make three routes, but that feels pretty repetitive.
#Also, every time we want to include someone else, we would need to create a new route.
#This is a great opportunity to add variable rules to our routes.
#For the example above, we could make the name a variable, like so:
@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "Hello, "+ name

#We can add as many of these as we need, giving each variable a different name:
@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + "id: " + id

if __name__=="__main__":
    app.run(debug=True)
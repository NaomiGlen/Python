from flask import Flask, render_template,redirect,request,session
app = Flask(__name__)
app.secret_key="I'm b1u3 Da-ba-d3e-d@-ba-d!"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    print("Got Post")
    session['username']=request.form['name']
    session['dojolocation']=request.form['location']
    session['favoritelanguage']=request.form['language']
    session['comments']=request.form['comments']
    return redirect('/result')

@app.route('/result')
def display():
    return render_template("result.html", 
                           name_on_template=session['username'], 
                           location_on_template=session['dojolocation'],
                           language_on_template=session['favoritelanguage'],
                           comments_on_template=session['comments']
                           )

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
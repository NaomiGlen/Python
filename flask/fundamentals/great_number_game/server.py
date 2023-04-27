from flask import Flask, render_template,request, redirect, session
import random
app = Flask(__name__)
app.secret_key='d0nt dROp ThAt dUn-DuN-dUn'

@app.route('/')
def index():
    if not 'random' in session:
        session['random']=random.randint(1,100)
        session['status']='new'
        session['guesses']=0
    print('Status This Session:', session['status'])
    print('Random Number This Session:', session['random'])
    return render_template("index.html", randNum=session['random'], status=session['status'], guesses=session['guesses'])

@app.route('/guess', methods=['POST'])
def guess():
    if request.form['guess-value']:
        if int(request.form['guess-value'])>session['random']:
            session['status'] = 'high'
        elif int(request.form['guess-value']) < session['random']:
            session['status'] = 'low'
        else :
            session['status'] = 'win'
        session['guesses'] += 1
        if session['status'] != 'win' and session['guesses'] >= 5:
            session['status'] ='lose'
    return redirect('/')

@app.route('/destroy_session')
def reset():
    session.clear()
    print('Session Reset!')
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
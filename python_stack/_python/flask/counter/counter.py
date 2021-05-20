from flask import Flask,render_template, session,redirect

app = Flask(__name__)
app.secret_key = 'keep it safe'

@app.route('/')
def index():
    if 'count' not in session:
        session['count']=0
    else :
        session['count']+=1
    
    return render_template('index.html')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/add2')
def add2():
    session['count'] += 1
    return redirect('/')
    
if __name__ == '__main__':
    app.run(debug=True)




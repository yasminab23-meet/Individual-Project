from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

firebaseConfig = {
  "apiKey": "AIzaSyDpPTQPbM2RhjGqS3-1Byy_hcuHPBiTUTw",
  "authDomain": "individual-cs-project-y2.firebaseapp.com",
  "projectId": "individual-cs-project-y2",
  "storageBucket": "individual-cs-project-y2.appspot.com",
  "messagingSenderId": "133344098525",
  "appId": "1:133344098525:web:de61b0c848f34167734334",
  "measurementId": "G-8SDSJ5CDMD",
  "databaseURL" :"https://individual-cs-project-y2-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase=pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()



@app.route('/')
def home():
    return render_template('index.html') 
    

@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user']=auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('hobbies'))
        except:
            error='LOGIN FAILED'
    return render_template('login.html')


@app.route('/create_account',methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
    try:
        login_session['user']=auth.create_user_with_email_and_password(email, password)
        return redirect(url_for('hobbies'))
    except:
        error='LOGIN FAILED'
    return render_template('create_account.html')

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')

@app.route('/martial_arts')
def martial_arts():
    return render_template('martial_arts.html')

@app.route ('/climbing')
def climbing():
    return render_template('climbing.html')

@app.route('/woodwork')
def woodwork():
    return render_template('woodwork.html')









if __name__ == '__main__':
    app.run(debug=True)
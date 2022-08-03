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
    

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/create_account')
def create_account():
    return render_template('create_account.html')

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')

if __name__ == '__main__':
    app.run(debug=True)
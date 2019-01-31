import os
from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://vhltvfuekxyisp:4e8e3284506f4903c26843cbeca2e8bc2ed4693c95ddd2dd8f104550c5700e27@ec2-79-125-6-250.eu-west-1.compute.amazonaws.com:5432/d4j9oravts15j7"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
    return render_template('index.html', message="Welcome!")

@app.route("/go_register", methods=["POST"])
def go_to_register():
    return render_template('register.html')

@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")   
    email = request.form.get("email")
    password = request.form.get("password")
        
    user = User(username = username, email = email, password = password)
    db.session.add(user)
    db.session.commit()
    return render_template('success.html')

@app.route("/sign_in", methods=["POST"])
def sign_in():
    input_user = request.form.get("username")
    input_password = request.form.get("password")  
    if " " in input_user or " " in input_password:
        return render_template('error.html', message = "You're trying to hack us!")    
    user = User.query.filter_by(username = input_user, password = input_password).first()
    
    if user is None:
        return render_template("error.html", message="You are not registered")    
    return render_template('welcome.html', message = input_user)

@app.route("/sign_out", methods=["POST"])
def sign_out():
    return render_template('index.html', message="You are logged out")
    

       




if __name__ == "__main__":
    with app.app_context():
        main()     

from flask import Flask,render_template,request
import sqlite3
from pymongo import MongoClient

app = Flask(__name__ , template_folder='Templates')
@app.route('/')
def Index():
    name = "Our Home"
    return render_template('index.html', data = name)

@app.route('/contact')
def Contact():
    return render_template('contact.html')

@app.route('/about')
def About():
    return render_template('about.html')

@app.route("/newuser")
def my_new_register_page():
    return render_template("newuserregister.html")
@app.route("/login")
def my_new_login_page():
    return render_template("newuserlogin.html")

@app.route("/registeruser", methods=['POST','GET'])
def my_register_user():
    entered_email = request.form.get("email")
    entered_username=request.form.get("username")
    entered_password=request.form.get("password")
    entered_password=entered_password.lower()
    print(entered_email,entered_username,entered_password)
   # database name
    info = db.SDP
    n={"usernamer":entered_username,
       "password":entered_password,
       "email":entered_email,
   }

    tofind1 = {"email":entered_email}
    info = db.user
    c=0
    for x in tofind1:
        if (user.find_one(tofind1)):
          c=1
    if(c==1):
        return "Email Already Exists...... Try again"
    else:
       user.insert_one
       return "User Registered Successfully"

@app.route("/loginuser",methods=['POST','GET'])
def my_login():
    entered_username = request.form.get("username")
    entered_password = request.form.get("password")
    client = MongoClient('mongodb://localhost:27017/')
    db = client['SDP']  # database name
    info = db.SDP
    user = db.user
    c=0
    tofind1 = {"username":entered_username }
    for x in tofind1:
        if(user.find_one(tofind1)):
            c=1
    tofind2={"password":entered_password}
    for x in tofind2:
        if (user.find_one(tofind2)):
            c = 2
    if (c!=2):
        return "Invalid User Credentials... try again"
    else:
        return "Success"

if __name__ == "__main__":
    app.run(debug=True)
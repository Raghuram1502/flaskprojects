from flask import Flask,request,render_template

app = Flask(__name__)
d = {}
count = 1
@app.route('/',methods = ["GET"])
def event():
    return render_template("event.html")

@app.route('/nextpage', methods = ["GET"])
def nextpage():
    return render_template("register.html")

@app.route('/register',methods= ["POST"])
def register():
    global d,count
    name = request.form["name"]
    age = request.form["age"]
    gender = request.form["gender"]
    address = request.form["address"]
    phn = request.form["phn"]
    email = request.form["email"]
    license = request.form["lisence"]
    x = {"Name": name,"age":age,"gender":gender, "address":address, "phn":phn, "email":email,"lisence":license}
    d[count] = x
    count += 1
    return render_template("details.html",id= count-1)
    

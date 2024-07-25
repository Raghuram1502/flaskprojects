from flask import Flask,request,render_template

app = Flask(__name__)

d = {}
count = 1

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/add", methods= ["POST"])
def add():
    global d,count
    name = request.form["name"]
    age = request.form["age"]
    gender = request.form["gender"]
    address = request.form["address"]
    phn = request.form["phn"]
    email = request.form["email"]
    sick = request.form["sick"]
    x = {"Name": name,"age":age,"gender":gender, "address":address, "phn":phn, "email":email, "sick":sick}
    d[count] = x
    count += 1
    return render_template("details.html",d=d)

@app.route("/search",methods =["POST"])
def search():
    global d
    x = request.form["id"]
    return render_template("search.html",d=d[int(x)])


    

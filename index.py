from flask import Flask,request,render_template

app = Flask(__name__)

d = {}
count = 1

@app.route('/addTodo',methods = ["post","GET"])
def addtodo():
    global d,count
    x = request.form["todo"]
    d[count] = x
    count += 1  
    return render_template("index.html",d=d)

@app.route('/delete', methods = ["GET"])
def delete():
    global d
    d.clear()
    return render_template("index.html",d=d)
    
@app.route('/')
def hello():
    global d
    return render_template("index.html",d=d)
   


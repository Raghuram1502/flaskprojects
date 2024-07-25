from flask import Flask,request

app = Flask(__name__)
d = {}
count = 1
@app.route('/addTodo', methods = ["POST"])
def todo():
    t = request.json["todo"]
    global d,count
    d[count] = t
    count += 1
    return {"id": len(d)}

@app.route('/allTodos',methods = ["GET"])
def get():
    global d
    x = request.args.get('id')
    return d[int(x)]

@app.route('/update',methods = ["PUT"])
def update():
    global d
    x = request.json["id"]
    v = request.json["value"]
    if x in d.keys():
        d[x] = v
        return f"{x} is updated"
    else:
        return "id not found" 



@app.route('/delete',methods = ["DELETE"])
def delete():
    global d
    x = request.json["id"]
    if x in d.keys():
        del d[x]
        return f"{x} is deleted"
    else:
        return "id not found"


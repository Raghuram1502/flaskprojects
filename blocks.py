from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import Integer, String,ForeignKey

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

class Blocks(db.Model):
    id = mapped_column(Integer,autoincrement=True, primary_key=True)
    value = mapped_column(String(100),nullable=False)

with app.app_context():
    db.create_all()

@app.route('/',methods = ["GET"])
def blocks():
    return render_template("blocks.html")

@app.route('/add', methods = ["POST"])
def add():
    x = request.form.get("block")
    block = Blocks(value = x)
    db.session.add(block)
    db.session.commit()
    return render_template("blocks.html")

@app.route('/getallblocks', methods = ["GET"])
def getallblocks():
    blocks = db.session.execute(db.select(Blocks)).scalars()
    return render_template("container.html",blocks = blocks)

@app.route('/delete/<int:id>',methods = ["GET","POST"])
def delete(id):
    x = db.get_or_404(Blocks,id)
    if request.method == "POST":
        db.session.delete(x)
        db.session.commit()
    return render_template("blocks.html")

@app.route('/update/<int:id>',methods = ["GET","POST"])
def update(id):
    data = request.form.get("value")
    x = db.get_or_404(Blocks,id)
    if request.method == "POST":
        if x and data is None:
            return "error value or id not found"
        if "value" in data:
            x.value = data["value"]
    db.session.commit()
    return "updated"






from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import Integer, String,ForeignKey
from flask_migrate import Migrate

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
migrate = Migrate(app, db)
db.init_app(app)

class College(db.Model):
    __tablename__ = "colleges" 
    id = mapped_column(Integer, primary_key=True)
    location = mapped_column(String(50))
#   student = relationship("Student", back_populates = "college")

class Student(db.Model):    
    __tablename__ = "students"
    id = mapped_column(Integer,primary_key=True)
    name = mapped_column(String(50),nullable=False)
    age = mapped_column(Integer)
    address = mapped_column(String(50))
    department = mapped_column(String(50))
    college_id = mapped_column(Integer, ForeignKey("colleges.id"),nullable=False)
#    college = relationship("College", back_populates = "students")

with app.app_context():
    db.create_all()
 
    new_college1 = College(id = 1,location = "main campus")
    new_college2 = College(id = 2,location = "valley campus")
    #db.session.add(new_college1)
    #db.session.add(new_college2)
    #db.session.commit()

@app.route('/create', methods = ["POST"])
def create():
    id = request.json.get("id")
    name = request.json.get("name")
    age = request.json.get("age")
    address = request.json.get("address")
    department = request.json.get("department")
    college_id = request.json.get("college_id")
    
    student1 = Student(id = id,name = name, age = age,address = address, department = department, college_id = college_id)
    db.session.add(student1)
    db.session.commit()
    return "ok"

@app.route('/getallstudents', methods = ["GET"])
def getallstudents():
    students = db.session.execute(db.select(Student)).scalars()
    students_list = [{"id":student.id, "name" : student.name, "age" : student.age, "address" : student.address, "department" : student.department, "college_id" : student.college_id}for student in students]
    return students_list
 
@app.route('/delete/<int:id>', methods = ["DELETE"])
def delete(id):
    student = db.get_or_404(Student,id)
    if student is None:
        return "error id not found"
    db.session.delete(student)
    db.session.commit()
    return "student is removed successfully"

@app.route('/update/<int:id>', methods = ["PUT"])
def update(id):
    data = request.json
    student = db.get_or_404(Student,id)
    if student is None:
        return "error id not found"
    if "name" in data:
        student.name = data["name"]
    if "age" in data:
        student.age = data["age"]
    db.session.commit()
    return "ok"

@app.route('/department',methods = ["POST"])
def get_department():
    department = request.json.get("department")
    college_id = request.json.get("college_id")
    students = db.session.execute(db.select(Student).filter_by(department = department,college_id=college_id)).scalars()

    students_list = [{"id":student.id, "name" : student.name, "age" : student.age, "address" : student.address, "department" : student.department, "college_id" : student.college_id} for student in students]
    return students_list
    
@app.route('/college/<int:college_id>',methods = ["GET"])
def college(college_id):
    college = db.session.execute(db.select(Student).filter_by(college_id = college_id)).scalars()
    students_list = [{"id":student.id, "name" : student.name, "age" : student.age, "address" : student.address, "department" : student.department, "college_id" : student.college_id} for student in college]
    return students_list









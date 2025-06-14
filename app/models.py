# The above code defines two classes, Admin and Employee, with attributes for user information and
# login credentials using Flask and SQLAlchemy.
from . import db
from flask_login import UserMixin
import datetime

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, default="Admin")
    
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False, default="$hashed_admin_password")  # Replace with a hashed password


class Employee(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    position = db.Column(db.String(100), nullable=False, default="Employee")  # Default position
    salary = db.Column(db.Float, nullable=False, default=0.0)  # Default salary
  
from app import db
class JobAssignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    job_title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    assigned_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    due_date = db.Column(db.DateTime, nullable=True)  # Add due_date
    completed_date = db.Column(db.DateTime, nullable=True)  # Add completed_date
    status = db.Column(db.String(20), default="Not Accepted")  # Default to "Not Accepted"

    employee = db.relationship('Employee', backref=db.backref('job_assignments', lazy=True))

    def __repr__(self):
        return f'<JobAssignment {self.job_title} - {self.employee_id} - {self.status}>'

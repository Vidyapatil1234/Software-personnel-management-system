from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from .models import Employee, Admin
from . import db
import smtplib  
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart  

auth = Blueprint('auth', __name__)
@auth.route('/create_employee', methods=['GET', 'POST'])
@login_required
def create_employee():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        position = request.form.get('position')
        salary = float(request.form.get('salary'))  # Convert salary to float
        password = request.form.get('password')
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        existing_user = Employee.query.filter_by(email=email).first()
        if existing_user:
            flash('Employee email already exists!', 'error')
            return redirect(url_for('auth.create_employee'))

        new_employee = Employee(name=name, email=email, position=position, salary=salary, password=hashed_password)
        db.session.add(new_employee)
        db.session.commit()

        flash('Employee account created successfully!', 'success')
        return redirect(url_for('views.admin_dashboard'))

    return render_template('create_employee.html')

# Function to send email with credentials
def send_email(to_email, name, password):
    sender_email = "vmpatil1892003@gmail.com"  # Replace with actual email
    sender_password = "Vtqlxvzaatdoqfmok"  # Use an app password for security
    subject = "Your Employee Account Details"
    body = f"""
    Hello {name},

    Your employee account has been successfully created.

    🔑 **Login Credentials:**
    - Email: {to_email}
    - Password: {password}

    📢 **Important:**
    Please log in immediately and change your password for security reasons.

    Best Regards,
    Admin Team
    """

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email:", e)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = Employee.query.filter_by(email=email).first() or Admin.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('views.admin_dashboard' if isinstance(user, Admin) else 'views.dashboard'))
        else:
            flash('Invalid email or password', 'error')

    return render_template('login.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('auth.login'))



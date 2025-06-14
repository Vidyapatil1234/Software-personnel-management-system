from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import Employee, db, JobAssignment
import datetime

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html', user=current_user)

@views.route('/dashboard')
@login_required
def dashboard():
    job_assignments = JobAssignment.query.filter_by(employee_id=current_user.id).all()
    return render_template('dashboard.html', user=current_user, job_assignments=job_assignments)

@views.route('/accept-job/<int:job_id>', methods=['POST'])
@login_required
def accept_job(job_id):
    job = JobAssignment.query.get(job_id)

    if not job:
        flash("Job not found!", "error")
        return redirect(url_for('views.dashboard'))

    if job.employee_id != current_user.id:
        flash("Unauthorized action!", "error")
        return redirect(url_for('views.dashboard'))

    if job.status == "Accepted":
        flash("Job already accepted!", "warning")
        return redirect(url_for('views.dashboard'))

    job.status = "Accepted"
    db.session.commit()
    flash("Job accepted successfully!", "success")

    return redirect(url_for('views.dashboard'))

@views.route('/update-job-status/<int:job_id>', methods=['POST']) # Corrected line
@login_required
def update_job_status(job_id):
    job = JobAssignment.query.get(job_id)

    if not job:
        flash("Job not found!", "error")
        return redirect(url_for('views.dashboard'))

    if job.employee_id != current_user.id:
        flash("Unauthorized action!", "error")
        return redirect(url_for('views.dashboard'))

    new_status = request.form.get('status')

    if new_status == "Completed":
        job.completed_date = datetime.datetime.now(datetime.timezone.utc)

    job.status = new_status
    db.session.commit()
    flash("Job status updated successfully!", "success")

    return redirect(url_for('views.dashboard'))

@views.route('/admin-dashboard')
@login_required
def admin_dashboard():
    return render_template('admin_dashboard.html', user=current_user)

@views.route('/view-total-employees')
def view_total_employees():
    employees = Employee.query.all()
    return render_template('view_total_employees.html', employees=employees)

@views.route('/generate-reports')
def generate_reports():
    return render_template('generate_reports.html')

@views.route('/promote-employee', methods=['POST'])
@login_required
def promote_employee():
    employee_id = request.form.get('employee_id')
    new_position = request.form.get('new_position')
    salary_hike = float(request.form.get('salary_hike'))

    employee = Employee.query.get(employee_id)
    if employee:
        employee.position = new_position
        employee.salary += (employee.salary * salary_hike / 100)
        db.session.commit()
        flash(f"{employee.name} has been promoted to {new_position}!", "success")
    else:
        flash("Employee not found!", "error")

    return redirect(url_for('views.view_total_employees'))

@views.route('/delete-employee/<int:employee_id>', methods=['POST'])
@login_required
def delete_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if employee:
        db.session.delete(employee)
        db.session.commit()
        flash(f"{employee.name} has been removed!", "success")
    else:
        flash("Employee not found!", "error")

    return redirect(url_for('views.view_total_employees'))

@views.route('/view-job-assignments')
@login_required
def view_job_assignments():
    job_assignments = JobAssignment.query.all()
    employees = Employee.query.all()
    return render_template('view_job_assignments.html', job_assignments=job_assignments, employees=employees)

@views.route('/assign-job', methods=['POST'])
@login_required
def assign_job():
    employee_id = request.form.get('employee_id')
    job_title = request.form.get('job_title')
    description = request.form.get('description')
    due_date_str = request.form.get('due_date')

    employee = Employee.query.get(employee_id)
    if not employee:
        flash("Employee not found!", "error")
        return redirect(url_for('views.view_job_assignments'))

    try:
        due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d") if due_date_str else None
    except ValueError:
        flash("Invalid date format. Please use YYYY-MM-DD.", "error")
        return redirect(url_for('views.view_job_assignments'))

    new_job = JobAssignment(
        employee_id=employee_id,
        job_title=job_title,
        description=description,
        due_date=due_date,
        completed_date=None,
        status="Not Accepted"
    )

    db.session.add(new_job)
    db.session.commit()

    flash(f"Job '{job_title}' assigned to {employee.name}!", "success")
    return redirect(url_for('views.view_job_assignments'))

@views.route('/reassign-job/<int:job_id>', methods=['POST'])
@login_required
def reassign_job(job_id):
    if not current_user.is_admin:
        flash("Only admins can reassign jobs!", "error")
        return redirect(url_for('views.view_job_assignments'))

    job = JobAssignment.query.get(job_id)
    if not job:
        flash("Job not found!", "error")
        return redirect(url_for('views.view_job_assignments'))

    new_employee_id = request.form.get('employee_id')
    new_employee = Employee.query.get(new_employee_id)

    if not new_employee:
        flash("New employee not found!", "error")
        return redirect(url_for('views.view_job_assignments'))

    job.employee_id = new_employee_id
    job.status = "Not Accepted"
    job.completed_date = None
    db.session.commit()

    flash(f"Job '{job.job_title}' reassigned to {new_employee.name}!", "success")
    return redirect(url_for('views.view_job_assignments'))
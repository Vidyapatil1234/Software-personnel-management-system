
# Software-Personnel-Management-System




## Overview
The Software Personnel Management System is a web-based application designed to manage employee records, job assignments, salaries, and reports. It includes role-based access for admins and employees with dedicated dashboards and functionalities.
## Features
User Authentication: Secure  signup and login for admins and employees.

**Admin Dashboard:**

- View total employees

- Manage employee data (Add, Edit, Delete)

- View job assignments

- Update salaries

- Generate reports

- Logout functionality

**Employee Dashboard:**

- View personal profile

- View job assignments and salary details

- Logout functionality


## Deployment
1. Clone the repository:

```bash
git clone https://github.com/Vidyapatil1234/Software-personnel-management-system.git
```
2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Set up the database:
```
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```
5. Run the application:
```
flask Run
```
6. Open in your browser:
```
http://127.0.0.1:5000/
```

## Workflow
- **Admin Login** → Access dashboard → Manage - employees → Assign jobs → Update salaries

- **Employee Login** → View personal details → Check job assignments & salary → Logout
## About Me
An AI & ML specialized student with a strong passion for web development. Currently working on building scalable and user-friendly web applications. Experienced in Flask, React.js, SQLAlchemy, and modern frontend frameworks. Interested in system architecture, role-based access control, and optimizing user experiences.
## Author
- [@Vidya Patil](https://github.com/Vidyapatil1234)

## License
This project is licensed under the 
[MIT](https://choosealicense.com/licenses/mit/)
License.

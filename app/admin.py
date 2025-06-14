from app import db, create_app
from app.models import Admin  # Ensure correct import

app = create_app()  # Make sure create_app() correctly initializes Flask & DB
from werkzeug.security import generate_password_hash

with app.app_context():
    hashed_password = generate_password_hash("admin123", method='pbkdf2:sha256')  # Hash the password
    admin = Admin(name="admin", email="admin@gmail.com", password=hashed_password)
    db.session.add(admin)
    db.session.commit()
    print("Admin user added successfully with hashed password.")


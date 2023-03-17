from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def matric_no(id):
    return f"ALT/PYT/{id:04d}"


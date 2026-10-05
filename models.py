from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id=db.Column(db.Integer,primary_key=True)
    username= db.Column(db.String(100),unique=True,nullable=False)
    password=db.Column(db.Text,nullable=False)
    register_date=db.Column(db.String(20),nullable=False)
    profile_image=db.Column(db.String(255),nullable=True)
    role=db.Column(db.String(20),nullable=False)
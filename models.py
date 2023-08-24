from . import db
from flask_login import UserMixin

class Profile(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    donation_history = db.Column(db.ARRAY(db.Float), default=list)
    total_donated = db.Column(db.Float, default=0.0)

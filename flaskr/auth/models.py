from flaskr.extensions import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    # __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    active = db.Column(db.Boolean, default=True)
    created = db.Column(db.DateTime(timezone=True), default = func.now())
    # role = db.relationship('Role')

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(100), unique=True)

import sqlalchemy as sa

user_role_m2m = db.Table(
    "user_role",
    sa.Column("user_id", sa.ForeignKey(User.id), primary_key=True),
    sa.Column("role_id", sa.ForeignKey(Role.id), primary_key=True),
)
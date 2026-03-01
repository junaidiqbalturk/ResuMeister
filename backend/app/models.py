from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    account_detail = db.relationship('AccountDetail', backref='user', uselist=False, cascade="all, delete-orphan")
    resumes = db.relationship('Resume', backref='author', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class AccountDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    full_name = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    address = db.Column(db.String(200), nullable=True)
    github_profile = db.Column(db.String(100), nullable=True)
    linkedin_profile = db.Column(db.String(100), nullable=True)
    discord = db.Column(db.String(100), nullable=True)

    def to_dict(self):
        return {
            'full_name': self.full_name,
            'phone': self.phone,
            'address': self.address,
            'github_profile': self.github_profile,
            'linkedin_profile': self.linkedin_profile,
            'discord': self.discord
        }

class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False, default='Untitled Resume')
    data = db.Column(db.Text, nullable=False) # JSON string containing the full resume payload
    template_id = db.Column(db.String(20), nullable=False, default='1')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        import json
        try:
            parsed_data = json.loads(self.data)
        except:
            parsed_data = {}
            
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'template_id': self.template_id,
            'data': parsed_data,
            'created_at': self.created_at.isoformat() + 'Z' if self.created_at else None,
            'updated_at': self.updated_at.isoformat() + 'Z' if self.updated_at else None
        }

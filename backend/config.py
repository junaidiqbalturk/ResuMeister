import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:greamesmith@localhost:5432/resumeister'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

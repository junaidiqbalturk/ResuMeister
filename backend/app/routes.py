from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt

from app import db, bcrypt
from app.models import User

# Define the blueprint
main = Blueprint('main', __name__)

# Sample in-memory user storage for demo purposes (in real apps, use a database)
users = {}


@main.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    print("Password getting from data:", password)
    confirm_password = data.get('confirmPassword')
    print("Confirmed Password getting from data:", confirm_password)

    if password != confirm_password:
        return jsonify({'message': 'Passwords do not match'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email already exists'}), 400
    username = email.split('@')[0]  # making username by spiriting the email address
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, email=email, password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201


@main.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if user and bcrypt.check_password_hash(user.password, password):
        # User authenticated successfully
        return jsonify({'success': True, 'message': 'Login successful'}), 200
    else:
        # Authentication failed
        return jsonify({'success': False, 'message': 'Invalid credentials'}), 401





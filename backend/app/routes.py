import pdfkit
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
    print("Data coming from Frontend:", data) # Log incoming
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

@main.route('/generate-resume', methods=['POST'])
def generate_resume():
    data = request.get_json()

    name = data.get('name')
    contact = data.get('contact')
    experience = data.get('experience')
    template_id = data.get('templateId')  # Template ID sent from Vue

    # Define template-based customizations (for simplicity, we'll assume PDFs are generated with just a name, contact, and experience)
    template_content = f"""
    Name: {name}
    Contact: {contact}
    Experience: {experience}
    """

    # Choose a different template style based on template_id (you can expand this logic)
    if template_id == 1:
        resume_html = f"<div style='font-family: Arial, sans-serif; color: black;'>{template_content}</div>"
    else:
        resume_html = f"<div style='font-family: 'Courier New'; color: blue;'>{template_content}</div>"

    # Generate PDF from HTML using pdfkit
    pdf = pdfkit.from_string(resume_html, False)

    # Save the PDF file
    file_path = f"generated_resume_{template_id}.pdf"
    with open(file_path, 'wb') as file:
        file.write(pdf)

    return jsonify({"message": "Resume generated successfully", "file_path": file_path})



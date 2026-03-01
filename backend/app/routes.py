import pdfkit
from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt

from app import db, bcrypt
from app.models import User, AccountDetail

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
        
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, email=email, password=hashed_password, image_file='default.jpg')

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        'message': 'User registered successfully',
        'user': {
            'id': new_user.id,
            'username': new_user.username,
            'email': new_user.email
        }
    }), 201


@main.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if user and bcrypt.check_password_hash(user.password, password):
        # User authenticated successfully
        return jsonify({'success': True, 'message': 'Login successful', 'user': {'id': user.id, 'username': user.username, 'email': user.email}}), 200
    else:
        # Authentication failed
        return jsonify({'success': False, 'message': 'Invalid credentials'}), 401
        
@main.route('/account/details/<int:user_id>', methods=['GET'])
def get_account_details(user_id):
    details = AccountDetail.query.filter_by(user_id=user_id).first()
    if details:
        return jsonify({'success': True, 'data': details.to_dict()}), 200
    return jsonify({'success': False, 'message': 'Account details not found'}), 404

@main.route('/account/details/<int:user_id>', methods=['POST', 'PUT'])
def save_account_details(user_id):
    data = request.json
    details = AccountDetail.query.filter_by(user_id=user_id).first()
    
    if not details:
        details = AccountDetail(user_id=user_id)
        db.session.add(details)
        
    if 'fullName' in data: details.full_name = data.get('fullName')
    if 'phone' in data: details.phone = data.get('phone')
    if 'address' in data: details.address = data.get('address')
    if 'githubProfile' in data: details.github_profile = data.get('githubProfile')
    if 'linkedinProfile' in data: details.linkedin_profile = data.get('linkedinProfile')
    if 'discord' in data: details.discord = data.get('discord')
    
    db.session.commit()
    
    return jsonify({'success': True, 'message': 'Account details saved successfully', 'data': details.to_dict()}), 200

@main.route('/account/details/<int:user_id>', methods=['DELETE'])
def delete_account_details(user_id):
    details = AccountDetail.query.filter_by(user_id=user_id).first()
    if details:
        db.session.delete(details)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Account details deleted successfully'}), 200
    return jsonify({'success': False, 'message': 'Account details not found'}), 404

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



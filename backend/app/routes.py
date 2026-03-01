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
    from flask_login import login_user
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if user and bcrypt.check_password_hash(user.password, password):
        # User authenticated successfully - CREATE SESSION
        login_user(user, remember=True)
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

# --- RESUME CRUD ENDPOINTS ---

from app.models import Resume
from flask_login import login_required, current_user
import json

@main.route('/api/resumes', methods=['GET'])
@login_required
def get_resumes():
    """Get all resumes for the logged-in user."""
    resumes = Resume.query.filter_by(user_id=current_user.id).order_by(Resume.updated_at.desc()).all()
    return jsonify({"resumes": [r.to_dict() for r in resumes]}), 200

@main.route('/api/resumes', methods=['POST'])
@login_required
def create_resume():
    """Create a new resume."""
    req = request.get_json()
    if not req:
        return jsonify({"message": "Invalid data format"}), 400

    title = req.get('title', 'Untitled Resume')
    template_id = req.get('template_id', '1')
    data = req.get('data', {})

    new_resume = Resume(
        user_id=current_user.id,
        title=title,
        template_id=template_id,
        data=json.dumps(data)
    )
    db.session.add(new_resume)
    db.session.commit()

    return jsonify({"message": "Resume created successfully", "resume": new_resume.to_dict()}), 201

@main.route('/api/resumes/<int:resume_id>', methods=['GET'])
@login_required
def get_resume(resume_id):
    """Retrieve a specific resume."""
    resume = Resume.query.get_or_404(resume_id)
    if resume.user_id != current_user.id:
        return jsonify({"message": "Unauthorized"}), 403
    return jsonify({"resume": resume.to_dict()}), 200

@main.route('/api/resumes/<int:resume_id>', methods=['PUT', 'POST'])
@login_required
def update_resume(resume_id):
    """Update an existing resume."""
    resume = Resume.query.get_or_404(resume_id)
    if resume.user_id != current_user.id:
        return jsonify({"message": "Unauthorized"}), 403

    req = request.get_json()
    if not req:
        return jsonify({"message": "Invalid data format"}), 400

    if 'title' in req:
        resume.title = req['title']
    if 'template_id' in req:
        resume.template_id = req['template_id']
    if 'data' in req:
        resume.data = json.dumps(req['data'])

    db.session.commit()
    return jsonify({"message": "Resume updated successfully", "resume": resume.to_dict()}), 200

@main.route('/api/resumes/<int:resume_id>', methods=['DELETE'])
@login_required
def delete_resume(resume_id):
    """Delete a resume."""
    resume = Resume.query.get_or_404(resume_id)
    if resume.user_id != current_user.id:
        return jsonify({"message": "Unauthorized"}), 403

    db.session.delete(resume)
    db.session.commit()
    return jsonify({"message": "Resume deleted successfully"}), 200

# --- ATS SCANNER API ---
import os
import tempfile
from werkzeug.utils import secure_filename
from app.models import AtsScan

@main.route('/api/ats-scan', methods=['POST'])
@login_required
def ats_scan():
    try:
        from ats_algorithm import rank_candidates
        
        job_description = request.form.get('job_description', '')
        if not job_description:
            return jsonify({"message": "Job description is required"}), 400
            
        if 'cv_file' not in request.files:
            return jsonify({"message": "CV file is required"}), 400
            
        file = request.files['cv_file']
        if file.filename == '':
            return jsonify({"message": "No selected file"}), 400
            
        filename = secure_filename(file.filename)
        ext = os.path.splitext(filename)[1].lower()
        if ext not in ['.pdf', '.docx']:
            return jsonify({"message": "Only PDF and DOCX files are supported"}), 400
            
        fd, temp_path = tempfile.mkstemp(suffix=ext)
        with os.fdopen(fd, 'wb') as temp_file:
            file.save(temp_file)
            
        try:
            results = rank_candidates([temp_path], job_description)
            if not results:
                return jsonify({"message": "Could not parse document."}), 500
                
            result = results[0]
            
            user_id = current_user.id if current_user.is_authenticated else None
            
            new_scan = AtsScan(
                user_id=user_id,
                job_description=job_description,
                cv_file_name=filename,
                match_score=result['overall_score'],
                semantic_score=result['semantic_score'],
                keyword_score=result['keyword_score']
            )
            db.session.add(new_scan)
            db.session.commit()
            
            return jsonify({
                "success": True,
                "scan_id": new_scan.id,
                "result": result
            }), 200
            
        finally:
            os.remove(temp_path)
            
    except Exception as e:
        print(f"ATS Scan Error: {str(e)}")
        return jsonify({"message": f"Server error: {str(e)}"}), 500

@main.route('/api/ats-history', methods=['GET'])
@login_required
def get_ats_history():
    try:
        scans = AtsScan.query.filter_by(user_id=current_user.id).order_by(AtsScan.created_at.desc()).all()
        history = []
        for scan in scans:
            history.append({
                "id": scan.id,
                "job_description": scan.job_description[:100] + "..." if len(scan.job_description) > 100 else scan.job_description,
                "cv_filename": scan.cv_file_name,
                "overall_score": scan.match_score,
                "semantic_score": scan.semantic_score,
                "keyword_score": scan.keyword_score,
                "created_at": scan.created_at.isoformat()
            })
        return jsonify({"success": True, "history": history}), 200
    except Exception as e:
        return jsonify({"success": False, "message": "Failed to fetch ATS history."}), 500


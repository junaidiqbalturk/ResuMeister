from app import create_app, db
from app.models import User
import sys
import traceback
import uuid

app = create_app()
with app.app_context():
    try:
        from flask_bcrypt import Bcrypt
        bcrypt = Bcrypt()
        hashed_password = bcrypt.generate_password_hash("StrongPassword1!").decode('utf-8')
        unique_id = str(uuid.uuid4())[:8]
        new_user = User(username=f"DebugUser_{unique_id}", email=f"debug_{unique_id}@example.com", password=hashed_password, image_file="default.jpg")
        db.session.add(new_user)
        db.session.commit()
        print("Success! New user ID:", new_user.id)
    except Exception as e:
        print("ERROR OCCURRED:")
        traceback.print_exc()

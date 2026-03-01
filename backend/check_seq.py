from app import create_app, db
from app.models import User
from sqlalchemy import text
import sys

app = create_app()
with app.app_context():
    try:
        # Check current max ID
        max_id_res = db.session.execute(text('SELECT max(id) FROM "user";')).scalar()
        print(f"Max ID in user table is: {max_id_res}")
        
        # Check sequence value
        seq_val_res = db.session.execute(text("SELECT nextval(pg_get_serial_sequence('\"user\"', 'id'));")).scalar()
        print(f"Nextval for user id sequence is: {seq_val_res}")
        
        # If sequence is less than max id, fix it correctly
        if max_id_res and seq_val_res <= max_id_res:
            print("Sequence is lagging! Fixing it now...")
            db.session.execute(text(f"SELECT setval(pg_get_serial_sequence('\"user\"', 'id'), {max_id_res + 1});"))
            db.session.commit()
            print("Sequence bumped.")
        else:
            print("Sequence seems fine.")
    except Exception as e:
        print(f"Error checking sequences: {e}")

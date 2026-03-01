from app import create_app, db
import sys

app = create_app()
with app.app_context():
    try:
        from sqlalchemy import text
        # Fix sequence for user table
        db.session.execute(text("SELECT setval(pg_get_serial_sequence('\"user\"', 'id'), coalesce(max(id), 1), max(id) IS NOT null) FROM \"user\";"))
        
        # Also fix sequence for account_detail just in case
        db.session.execute(text("SELECT setval(pg_get_serial_sequence('account_detail', 'id'), coalesce(max(id), 1), max(id) IS NOT null) FROM account_detail;"))
        
        db.session.commit()
        print("Sequences fixed successfully.")
    except Exception as e:
        print(f"Error fixing sequences: {e}")

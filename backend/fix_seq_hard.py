from app import create_app, db
import sys
from sqlalchemy import text

app = create_app()
with app.app_context():
    try:
        # Create sequences if they don't exist
        db.session.execute(text("CREATE SEQUENCE IF NOT EXISTS user_id_seq;"))
        db.session.execute(text("ALTER TABLE \"user\" ALTER COLUMN id SET DEFAULT nextval('user_id_seq');"))
        db.session.execute(text("ALTER SEQUENCE user_id_seq OWNED BY \"user\".id;"))
        
        # Set value based on current max row
        db.session.execute(text("SELECT setval('user_id_seq', coalesce(max(id), 1), max(id) IS NOT null) FROM \"user\";"))

        # Same for account detail
        db.session.execute(text("CREATE SEQUENCE IF NOT EXISTS account_detail_id_seq;"))
        db.session.execute(text("ALTER TABLE account_detail ALTER COLUMN id SET DEFAULT nextval('account_detail_id_seq');"))
        db.session.execute(text("ALTER SEQUENCE account_detail_id_seq OWNED BY account_detail.id;"))
        db.session.execute(text("SELECT setval('account_detail_id_seq', coalesce(max(id), 1), max(id) IS NOT null) FROM account_detail;"))
        
        db.session.commit()
        print("Sequences hard-linked and fixed successfully.")
    except Exception as e:
        db.session.rollback()
        print(f"Error fixing sequences: {e}")

# create_user.py - Simplified version (no email/full_name)
from database.db import SessionLocal
from models.user import User

def create_user(username, password):
    db = SessionLocal()
    
    existing = db.query(User).filter(User.username == username).first()
    if existing:
        print(f"❌ User '{username}' already exists!")
        db.close()
        return False
    
    new_user = User(
        username=username,
        password=User.hash_password(password)
    )
    
    db.add(new_user)
    db.commit()
    db.close()
    print(f"✅ User '{username}' created successfully!")
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("Creating default users...")
    print("=" * 50)
    
    create_user("admin", "admin123")
    create_user("manager", "manager123")
    create_user("staff", "staff123")
    
    print("\n" + "=" * 50)
    print("📝 Login Credentials:")
    print("   admin / admin123")
    print("   manager / manager123")
    print("   staff / staff123")
    print("=" * 50)
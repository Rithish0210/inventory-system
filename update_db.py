# update_db.py - Add missing columns to users table without deleting data
import sqlite3

def update_database():
    conn = sqlite3.connect("stock.db")
    cursor = conn.cursor()
    
    # Check if users table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    table_exists = cursor.fetchone()
    
    if not table_exists:
        print("❌ Users table doesn't exist yet. It will be created when you run the app.")
        conn.close()
        return
    
    # Get existing columns
    cursor.execute("PRAGMA table_info(users)")
    columns = [col[1] for col in cursor.fetchall()]
    
    print(f"📋 Existing columns: {columns}")
    
    # Add missing columns one by one
    if "email" not in columns:
        print("➕ Adding email column...")
        cursor.execute("ALTER TABLE users ADD COLUMN email TEXT")
    
    if "full_name" not in columns:
        print("➕ Adding full_name column...")
        cursor.execute("ALTER TABLE users ADD COLUMN full_name TEXT")
    
    if "is_active" not in columns:
        print("➕ Adding is_active column...")
        cursor.execute("ALTER TABLE users ADD COLUMN is_active INTEGER DEFAULT 1")
    
    conn.commit()
    
    # Verify the update
    cursor.execute("PRAGMA table_info(users)")
    updated_columns = [col[1] for col in cursor.fetchall()]
    print(f"✅ Updated columns: {updated_columns}")
    
    conn.close()
    print("\n🎉 Database updated successfully! Your existing items are safe.")

if __name__ == "__main__":
    update_database()
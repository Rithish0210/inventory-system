# 📦 RJ Stocks - Inventory Management System

A full-featured inventory management system built with **FastAPI**, **SQLite**, and **Tailwind CSS**. Perfect for small businesses to track stock levels, manage items, and receive low stock alerts.

## ✨ Features

- ✅ **User Authentication** - Secure login/logout with password hashing
- ✅ **Inventory Management** - Add, view, and manage stock items
- ✅ **Stock Operations** - Increase/decrease stock by 5 units with one click
- ✅ **Low Stock Alerts** - Automatic highlighting when quantity falls below threshold
- ✅ **Real-time Updates** - Instant refresh after any stock change
- ✅ **Responsive Design** - Works on desktop, tablet, and mobile
- ✅ **REST API** - Complete backend API for integration
- ✅ **SQLite Database** - Lightweight, no separate database server needed

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Rithish0210/inventory-system.git
cd inventory-system

pip install fastapi uvicorn sqlalchemy passlib

Run the application:
             uvicorn main:app --reload

Open your browser:
              http://localhost:8000/login

Default Login Credentials
Username	Password	Role
rithish  Rithish0210	Administrator
manager	manager123	Store Manager
staff	staff123	Staff User
Note: First-time run automatically creates these users. Passwords are hashed and stored securely.

Project Structure:

inventory-system/
├── database/
│   └── db.py              # Database connection
├── models/
│   ├── item.py            # Item model
│   └── user.py            # User model with password hashing
├── schemas/
│   ├── item_schema.py     # Item validation
│   ├── stock_schema.py    # Stock validation
│   └── user_schema.py     # User validation
├── templates/
│   ├── index.html         # Dashboard
│   ├── items.html         # Items management
│   ├── low_stock.html     # Low stock alerts
│   └── login.html         # Login page
├── main.py                # FastAPI application
└── stock.db               # SQLite database (auto-created)

API Endpoints
Method	Endpoint	Description
GET	/login	Login page
POST	/api/login	User login
POST	/api/logout	User logout
GET	/api/current-user	Get current user info
GET	/	Dashboard home page
GET	/items-ui	Items management page
GET	/low-stock-ui	Low stock alerts page
GET	/items	Get all items (API)
POST	/add-item	Add new item
POST	/stock-in	Increase stock (+5)
POST	/stock-out	Decrease stock (-5)
GET	/low-stock	Get low stock items (API)

🗄️ Database Management
Use DB Browser for SQLite to view/edit the database directly:
Download DB Browser for SQLite
Open stock.db file
Browse/Edit users and items tables

Changing User Passwords
To change a user's password, generate a hash first:
 python -c "import hashlib; salt='rjstocks_salt_2024'; pw='your_new_password'; print(hashlib.sha256((pw+salt).encode()).hexdigest())"
then update the password field in the users table with the generated hash.

Adding New Users Manually
python -c "from database.db import SessionLocal; from models.user import User; db=SessionLocal(); db.add(User(username='newuser', password=User.hash_password('pass123'))); db.commit(); db.close()"

How to Use:
Adding Items
Login to the system

Fill in the "Register new item" form:
Item name - Name of the product
Unit - Measurement unit (kg, pcs, liters, etc.)
Initial quantity - Starting stock amount
Threshold alert - Minimum stock level for alerts
Click "Add Item" button

Managing Stock
Click "+5" to increase stock by 5 units
Click "-5" to decrease stock by 5 units
Low stock items (quantity ≤ threshold) will show red warning
Viewing Low Stock Items
Click "Low Stock" tab in navigation
Shows only items that need reordering

🔒 Security Features
✅ Passwords hashed with SHA256 + salt
✅ Session-based authentication
✅ Protected routes (require login)
✅ SQL injection prevention via SQLAlchemy

🛠️ Tech Stack
Backend: FastAPI (Python)
Database: SQLite with SQLAlchemy ORM
Frontend: HTML5, Tailwind CSS, JavaScript
Authentication: Session-based with SHA256 hashing
Icons: Font Awesome 6

📝 Future Enhancements
Export inventory to CSV/Excel
Email alerts for low stock
Activity logs (who changed what)
Barcode scanning support
Bulk import/export
Dashboard charts and analytics
Dark mode support

👨‍💻 Author
Rithish R
GitHub: @Rithish0210

🙏 Acknowledgments
FastAPI - Modern web framework
Tailwind CSS - Utility-first CSS framework
SQLAlchemy - SQL toolkit
Font Awesome - Icons

Access on Mobile
To access on mobile devices:
Run server on computer: uvicorn main:app --host 0.0.0.0 --port 8000
Find your computer's IP address (ipconfig on Windows, ifconfig on Mac/Linux)
On mobile browser: http://YOUR_COMPUTER_IP:8000/login
Make sure both devices are on the same WiFi network


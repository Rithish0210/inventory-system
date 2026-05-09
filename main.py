from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from database.db import SessionLocal, engine, Base
import models.item
import models.user
from schemas.item_schema import ItemCreate
from schemas.stock_schema import StockUpdate
from schemas.user_schema import UserCreate, UserLogin, PasswordChange

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# Add session middleware for login
app.add_middleware(
    SessionMiddleware,
    secret_key="your-secret-key-change-this",  # Change in production!
    session_cookie="inventory_session"
)

# ------------------ HELPER FUNCTIONS ------------------

def get_current_user(request: Request):
    """Get current user from session"""
    user_id = request.session.get("user_id")
    if not user_id:
        return None
    
    db = SessionLocal()
    user = db.query(models.user.User).filter(models.user.User.id == user_id).first()
    db.close()
    return user

# ------------------ AUTHENTICATION ROUTES ------------------

@app.get("/login")
def login_page():
    return FileResponse("templates/login.html")

    
    # Check if username exists
    existing = db.query(models.user.User).filter(
        models.user.User.username == user_data.username
    ).first()
    
    if existing:
        db.close()
        return {"success": False, "error": "Username already taken"}
    
    # Create new user with hashed password
    new_user = models.user.User(
        username=user_data.username,
        password=models.user.User.hash_password(user_data.password),
        email=user_data.email,
        full_name=user_data.full_name
    )
    
    db.add(new_user)
    db.commit()
    db.close()
    
    return {"success": True, "message": "User created successfully"}

@app.post("/api/login")
def login_user(user_data: UserLogin, request: Request):
    db = SessionLocal()
    
    user = db.query(models.user.User).filter(
        models.user.User.username == user_data.username
    ).first()
    
    if not user or not user.verify_password(user_data.password):
        db.close()
        return {"success": False, "error": "Invalid username or password"}
    
    # Store user in session
    request.session["user_id"] = user.id
    request.session["username"] = user.username
    
    db.close()
    return {"success": True, "redirect": "/"}

@app.post("/api/logout")
def logout(request: Request):
    request.session.clear()
    return {"success": True, "redirect": "/login"}

@app.get("/api/current-user")
def current_user(request: Request):
    user = get_current_user(request)
    if not user:
        return {"authenticated": False}
    
    return {
        "authenticated": True,
        "user_id": user.id,
        "username": user.username,
        "email": user.email,
        "full_name": user.full_name
    }

# ------------------ UI ROUTES (Protected) ------------------

@app.get("/")
def home(request: Request):
    if not get_current_user(request):
        return RedirectResponse(url="/login")
    return FileResponse("templates/index.html")

@app.get("/items-ui")
def items_ui(request: Request):
    if not get_current_user(request):
        return RedirectResponse(url="/login")
    return FileResponse("templates/items.html")

@app.get("/low-stock-ui")
def low_stock_ui(request: Request):
    if not get_current_user(request):
        return RedirectResponse(url="/login")
    return FileResponse("templates/low_stock.html")

# ------------------ API ROUTES (Protected) ------------------

@app.post("/add-item")
def add_item(item: ItemCreate, request: Request):
    if not get_current_user(request):
        return {"error": "Authentication required"}
    
    db = SessionLocal()
    new_item = models.item.Item(
        name=item.name,
        unit=item.unit,
        quantity=item.quantity,
        threshold=item.threshold
    )
    db.add(new_item)
    db.commit()
    db.close()
    return {"message": "Item added successfully"}

@app.get("/items")
def get_items(request: Request, name: str = None):
    if not get_current_user(request):
        return {"error": "Authentication required"}
    
    db = SessionLocal()
    if name:
        items = db.query(models.item.Item).filter(models.item.Item.name == name).all()
    else:
        items = db.query(models.item.Item).all()
    db.close()
    return items

@app.post("/stock-out")
def stock_out(data: StockUpdate, request: Request):
    if not get_current_user(request):
        return {"error": "Authentication required"}
    
    db = SessionLocal()
    item = db.query(models.item.Item).filter(models.item.Item.id == data.item_id).first()
    if item:
        if item.quantity < data.quantity:
            db.close()
            return {"error": "Not enough stock"}
        item.quantity -= data.quantity
        db.commit()
        db.close()
        return {"message": "Stock reduced"}
    db.close()
    return {"error": "Item not found"}

@app.post("/stock-in")
def stock_in(data: StockUpdate, request: Request):
    if not get_current_user(request):
        return {"error": "Authentication required"}
    
    db = SessionLocal()
    item = db.query(models.item.Item).filter(models.item.Item.id == data.item_id).first()
    if item:
        item.quantity += data.quantity
        db.commit()
        db.close()
        return {"message": "Stock increased"}
    db.close()
    return {"error": "Item not found"}

@app.get("/low-stock")
def low_stock(request: Request):
    if not get_current_user(request):
        return {"error": "Authentication required"}
    
    db = SessionLocal()
    items = db.query(models.item.Item).filter(
        models.item.Item.quantity < models.item.Item.threshold
    ).all()
    db.close()
    return items
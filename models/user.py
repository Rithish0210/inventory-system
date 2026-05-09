from sqlalchemy import Column, Integer, String
from database.db import Base
import hashlib

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String, nullable=True)
    full_name = Column(String, nullable=True)
    is_active = Column(Integer, default=1)
    
    @staticmethod
    def hash_password(plain_password: str) -> str:
        """Hash a password using SHA256"""
        salt = "rjstocks_salt_2024"
        combined = plain_password + salt
        return hashlib.sha256(combined.encode()).hexdigest()
    
    def verify_password(self, plain_password: str) -> bool:
        """Verify a plain text password against the stored hash"""
        # self.password is the stored hash from database
        return self.password == self.hash_password(plain_password)
from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    unit: str
    quantity: float
    threshold: float
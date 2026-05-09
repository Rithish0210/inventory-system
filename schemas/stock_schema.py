from pydantic import BaseModel

class StockUpdate(BaseModel):
    item_id: int
    quantity: float
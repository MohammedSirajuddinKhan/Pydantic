from pydantic import BaseModel, Field
from typing import Optional, Literal


class Category(BaseModel):  # Pydantic Model that validates the data
    name: Literal['starter', 'main course', 'dessert', 'beverage']


class Model(BaseModel):
    # Field: Value Type
    id: int
    name: str = Field(..., min_length=3, max_length=50,
                      description="Item Name")  # Required Field
    price: float = Field(..., gt=0, description="Item Price")  # Required Field
    category: Category = Field(..., description="Item Category")
    # It is okay if nothing comes in this
    is_available: bool = Field(default=True)
    description: Optional[str] = "Optional"  # Optional Field


item = Model(id=1,
             name="Starter",
             price=20.98,
             category=Category(name='starter'), is_available=True)
print(item)

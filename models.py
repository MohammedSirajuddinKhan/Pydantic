from pydantic import BaseModel, Field, field_validator, model_validator, computed_field
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
    description: Optional[str] = "Optional"

    # Optional Field
    # Types of custom validators

    #   Field Validator -> Only for one field
    @field_validator('name')
    @classmethod
    def title_name(cls, value):
        return value.title()

    #   Model Validator -> Multiple fields
    @model_validator(mode='after')
    def check_available(self):
        if self.is_available and self.price <= 0:
            raise ('Available item must have price greater than 0')
        return self

    #   Computed Field ->
    @computed_field
    @property
    def price_tax(self) -> float:
        return round(self.price * 1.05, 2)


item = Model(id=1, name="PaNeER tiKka", price=12,category=Category(name='main course'))

print(item) # needs to be converted to dictionary to be able to send to other inside project functions...

# model_dump() -> converts object into dictionary but works only in inside python project files
print('\nDictionary Model Dump')
print(item.model_dump())

#model_dump_json() -> to send object over the internet or the websites, out of PYTHON
print('\nJson Model Dump')
print(item.model_dump_json())
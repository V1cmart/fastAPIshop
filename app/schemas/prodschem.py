from pydantic import BaseModel, Field
from decimal import Decimal

# id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(255), nullable=False, index=True)
#     description = Column(String(1000))
#     price = Column(Numeric(10, 2), nullable=False)
#     category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

#     category = relationship("Category", back_populates="products")


class ProductBase(BaseModel):
    name: str = Field(..., max_length=255)
    description: str = Field(..., max_length=1000)
    price: Decimal
    category_id: int

    class Config:
        from_attributes = True

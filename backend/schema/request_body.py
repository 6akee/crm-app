from enum import Enum
from pydantic import BaseModel, Field


class ProductType(str, Enum):
    anime = "anime"
    movie = "movie"


class RequestBody(BaseModel):
    product_type: str = Field(description="Тип продукта для описания фактов")
    product_name: str = Field(description="Название самого продукта")
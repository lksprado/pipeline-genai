from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, validate_call
from typing import Tuple 
from datetime import datetime 
from enum import Enum 

class ProductEnum(str, Enum):
    product1 = "Luminae - Gemini"
    product2 = "Luminae - chatGPT"
    product3 =  "Luminae - Llama3"

class Sales(BaseModel):
    """
    Data contract for sales
    
    
    Args: \n
        email(EmailStr): email do comprador \n
        date_hour(datetime): order date \n
        price(PositiveFloat): order price \n
        quantity(PositiveInt): order quantity \n
        product(ProductEnum): order product category
    """
    email: EmailStr 
    date_hour: datetime
    price: PositiveFloat 
    quantity: PositiveInt  
    product: ProductEnum 
    
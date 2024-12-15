from pydantic import BaseModel
from typing import Optional

class Deal(BaseModel):
    price: float
    terms: str
    client_id: int
    provider_id: int
    context_field1: Optional[str]
    context_field2: Optional[str]

from pydantic import BaseModel

class Provider(BaseModel):
    name: str
    inn: str
    email: str
    phone_number: str

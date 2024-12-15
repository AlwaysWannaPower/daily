from pydantic import BaseModel

class Client(BaseModel):
    name: str
    inn: str
    email: str
    phone_number: str
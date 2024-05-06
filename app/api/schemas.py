from pydantic import BaseModel


class PhoneBookRecord(BaseModel):
    adres: str


class PhoneBookRecordCreate(BaseModel):
    phone_number: str
    address: str

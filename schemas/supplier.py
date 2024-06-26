from pydantic import BaseModel
from typing import List

class SupplierBase(BaseModel):
    name: str
    contact_person: str
    phone_number: int
    email: str
    address: str

class SupplierCreate(SupplierBase):
    pass

class SupplierUpdate(SupplierBase):
    id: int

class Supplier(SupplierBase):
    id: int

    class ConfigDict:
        from_attributes = True

class SupplierID(Supplier):
    id: int

    class ConfigDict:
        from_attributes = True

class Suppliers(BaseModel):
    suppliers: List[Supplier]
    total_count: int
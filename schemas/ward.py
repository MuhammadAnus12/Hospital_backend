from pydantic import BaseModel
from typing import List


class WardBase(BaseModel):
    name: str
    type: str
    capacity: int


class WardCreate(WardBase):
    pass


class Ward(WardBase):
    id: int

    class ConfigDict:
        from_attributes = True

class WardUpdate(WardBase):
    id: int

class WardID(Ward):
    id: int

    class ConfigDict:
        from_attributes = True

class Wards(BaseModel):
    wards: List[Ward]
    total_count: int


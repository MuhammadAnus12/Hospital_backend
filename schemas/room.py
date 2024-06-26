from pydantic import BaseModel
from typing import List


class RoomBase(BaseModel):
    number: int
    type: str
    availability_status: str
    department_id: int


class RoomCreate(RoomBase):
    pass


class Room(RoomBase):
    id: int

    class ConfigDict:
        from_attributes = True


class RoomUpdate(RoomBase):
    id: int


class RoomID(Room):
    id: int

    class ConfigDict:
        from_attributes = True


class Rooms(BaseModel):
    rooms: List[Room]
    total_count: int

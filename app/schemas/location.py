from typing import Optional

from sqlmodel import SQLModel


class LocationCreate(SQLModel):
    name : str
    type : Optional[str]
    dimension : Optional[str]

class LocationResponse(LocationCreate):
    id : int

class LocationUpdate(SQLModel):
    name : Optional[str]
    type : Optional[str]
    dimension : Optional[str]
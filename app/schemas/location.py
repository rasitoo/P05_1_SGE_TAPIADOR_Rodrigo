from typing import Optional

from sqlmodel import SQLModel

from app.models.character import Character


class LocationCreate(SQLModel):
    name : str
    type : Optional[str]
    dimension : Optional[str]

class LocationResponse(LocationCreate):
    id : int
    characters : Optional[list[Character]]
    citizens : Optional[list[Character]]

class LocationUpdate(SQLModel):
    name : Optional[str]
    type : Optional[str]
    dimension : Optional[str]
from typing import Optional

from sqlmodel import  SQLModel

from app.models.location import Location


class CharacterCreate(SQLModel):
    name : str
    type : Optional[str]
    status : Optional[str]
    species : Optional[str]
    gender : Optional[str]
    imageUri : Optional[str]
    location_id : Optional[int]
    origin_id : Optional[int]

class CharacterResponse(CharacterCreate):
    id: int
    location : Optional[Location]
    origin : Optional[Location]

class CharacterUpdate(SQLModel):
    name : Optional[str]
    type : Optional[str]
    status : Optional[str]
    species : Optional[str]
    gender : Optional[str]
    imageUri : Optional[str]
    location_id : Optional[int]
    origin_id : Optional[int]
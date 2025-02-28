from typing import Optional

from sqlmodel import  SQLModel


class CharacterCreate(SQLModel):
    name : str
    type : Optional[str]
    status : Optional[str]
    species : Optional[str]
    gender : Optional[str]
    imageUri : Optional[str]
    locationid : int
    originid : Optional[int]

class CharacterResponse(CharacterCreate):
    id: int

class CharacterUpdate(SQLModel):
    name : Optional[str]
    type : Optional[str]
    status : Optional[str]
    species : Optional[str]
    gender : Optional[str]
    imageUri : Optional[str]
    locationid : Optional[int]
    originid : Optional[int]
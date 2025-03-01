from sqlalchemy.orm import foreign
from sqlmodel import SQLModel, Relationship, Field,ForeignKey
from typing_extensions import Optional

from app.models.character import Character

# error multiple foreignkey solucionado gracias a https://techoverflow.net/2024/09/28/sqlmodel-how-to-fix-noforeignkeyserror-could-not-determine-join-condition-between-parent-child-tables-on-relationship/#:~:text=When%20you%20encounter%20this%20error%2C%20the%20solution%20is,to%20both%20sides%20of%20the%20Relationship%20field%20definition.
# https://stackoverflow.com/questions/55278773/sqlalchemy-ambiguousforeignkeyserror
class Location(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    name : Optional[str]
    type : Optional[str]
    dimension : Optional[str]
    characters : Optional[list[Character]] = Relationship(
        back_populates="location",
        sa_relationship_kwargs={
            "primaryjoin": "Location.id==foreign(Character.location_id)"
        }
    )
    citizens : Optional[list[Character]] = Relationship(
        back_populates="origin",
        sa_relationship_kwargs={
            "primaryjoin": "Location.id==foreign(Character.origin_id)"
        }
    )
from sqlmodel import SQLModel, Relationship, Field
from typing_extensions import Optional
#https://stackoverflow.com/questions/7548033/how-to-define-two-relationships-to-the-same-table-in-sqlalchemy
#https://stackoverflow.com/questions/71464757/what-does-sa-relationship-kwargs-lazy-selectin-means-on-sqlmodel-with-f
#https://docs.sqlalchemy.org/en/20/orm/join_conditions.html
class Character(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    name : Optional[str]
    type : Optional[str]
    status : Optional[str]
    species : Optional[str]
    gender : Optional[str]
    imageUri : Optional[str]
    location_id : Optional[int] = Field(foreign_key="location.id")
    location : Optional["Location"] = Relationship(
        back_populates="characters",
        sa_relationship_kwargs={
            #"primaryjoin": "characters.location_id==foreign(Location.id)"
            "foreign_keys":"[Character.location_id]"
        }
    )
    origin_id : Optional[int] = Field(default=None, foreign_key="location.id")
    origin : Optional["Location"] = Relationship(
        back_populates="citizens",
        sa_relationship_kwargs={
            #"primaryjoin": "citizens.origin_id==foreign(Location.id)"
            "foreign_keys":"[Character.origin_id]"

        }
    )
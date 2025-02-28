from sqlmodel import SQLModel, Relationship, Field,ForeignKey
from typing_extensions import Optional

#https://docs.sqlalchemy.org/en/20/orm/self_referential.html#self-referential
#https://stackoverflow.com/questions/71464757/what-does-sa-relationship-kwargs-lazy-selectin-means-on-sqlmodel-with-f
class Character(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    name : Optional[str]
    type : Optional[str]
    status : Optional[str]
    species : Optional[str]
    gender : Optional[str]
    imageUri : Optional[str]
    location_id : int = Field(foreign_key="location.id")
    location : Optional["Location"] = Relationship(
        back_populates="characters"
        #sa_relationship_kwargs={
        #    "primaryjoin": "Character.location_id==foreign(Location.id)",
        #    "remote_side": "[Location.id]"
        #}
    )
#    origin_id : Optional[int] = Field(default=None, foreign_key="location.id")
#    origin : Optional["Location"] = Relationship(
#        back_populates="citizens",
#        sa_relationship_kwargs={
#            "primaryjoin": "Character.origin_id==foreign(Location.id)",
#            "remote_side": "[Location.id]"
#        }
#    )
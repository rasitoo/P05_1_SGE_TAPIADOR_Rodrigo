from http.client import HTTPException

from fastapi import APIRouter, Depends
from sqlmodel import select, Session

from app.schemas.character import CharacterResponse, CharacterCreate, CharacterUpdate
from app.models.character import Character
from app.db.session import get_session

router = APIRouter(prefix="/characters", tags=["Characters"])

@router.post("/", response_model=CharacterResponse)
async def create_character(character_schema: CharacterCreate,session: Session = Depends(get_session)):
    character = Character(**character_schema.model_dump()) #model_dump convierte los datos del schema en un diccionario y el constructor de Character crea un objeto con ese diccionario
    if character.location_id is None:
        raise HTTPException(status_code=400, detail="location_id is required")
    session.add(character)
    session.commit()
    session.refresh(character)
    return CharacterResponse(**character.model_dump())

@router.get("/", response_model=list[CharacterResponse])
async def read_characters(session: Session = Depends(get_session)):
    return session.exec(select(Character)).all()

@router.get("/{id}", response_model=CharacterResponse)
async def read_character(id: int,session: Session = Depends(get_session)):
    return session.get(Character,id)

@router.patch("/{id}", response_model=CharacterResponse)
async def update_character(id: int, character_data: CharacterUpdate,session: Session = Depends(get_session)):
    character = session.get(Character,id)

    if not character:
        raise HTTPException(status_code=404, detail="Character not found")

    character_dict = character_data.model_dump(exclude_unset=True)
    for key, value in character_dict.items():
        setattr(character,key,value)

    session.add(character)
    session.commit()
    session.refresh(character)
    return character
@router.delete("/{id}", response_model=dict)
async def delete_character(id: int,session: Session = Depends(get_session)):
    character = session.get(Character,id)

    if not character:
        raise HTTPException(status_code=404, detail="Character not found")

    session.delete(character)
    session.commit()
    return {"message": "Character deleted succesfully"}
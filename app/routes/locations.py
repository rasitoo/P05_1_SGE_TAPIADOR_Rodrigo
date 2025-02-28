from http.client import HTTPException

from fastapi import APIRouter, Depends
from sqlmodel import select, Session

from app.db.session import get_session
from app.models.location import Location
from app.schemas.location import LocationResponse, LocationCreate, LocationUpdate

router = APIRouter(prefix="/locations", tags=["Locations"])

@router.post("/", response_model=LocationResponse)
async def create_location(location_schema: LocationCreate,session: Session = Depends(get_session)): #Hay qu eponer get_session sin parentesis ya que no estamos llamando a la función sino referenciándola para que FastAPI la llame (he tardado 3 horas en darme cuenta)
    location = Location(**location_schema.model_dump()) #model_dump convierte los datos del schema en un diccionario y el constructor de Character crea un objeto con ese diccionario
    session.add(location)
    session.commit()
    session.refresh(location)
    return LocationResponse(**location.model_dump())

@router.get("/", response_model=LocationResponse)
async def read_locations(session: Session = Depends(get_session)):
    return session.exec(select(Location)).all()

@router.get("/{id}", response_model=LocationResponse)
async def read_location(id: int,session: Session = Depends(get_session)):
    return session.get(Location,id)

@router.patch("/{id}", response_model=LocationResponse)
async def update_location(id: int, location_data: LocationUpdate,session: Session = Depends(get_session)):
    location = session.get(Location,id)

    if not location:
        raise HTTPException(status_code=404, detail="location not found")

    location_dict = location_data.model_dump(exclude_unset=True)
    for key, value in location_dict.items():
        setattr(location,key,value)

    session.add(location)
    session.commit()
    session.refresh(location)
    return location
@router.patch("/{id}", response_model=dict)
async def delete_location(id: int,session: Session = Depends(get_session)):
    location = session.get(Location,id)

    if not location:
        raise HTTPException(status_code=404, detail="location not found")

    session.delete(location)
    session.commit()
    return {"message": "location deleted succesfully"}
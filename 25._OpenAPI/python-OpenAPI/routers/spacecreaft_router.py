from fastapi import APIRouter
from pydantic import BaseModel

class Spacecraft(BaseModel):
    id: int
    name: str

spacecrafts = [
    Spacecraft(id=1, name="Apollo 13"),
    Spacecraft(id=2, name="Hubble"),
    Spacecraft(id=3, name="ISS"),
]

router = APIRouter()

@router.get("/api/spacecrafts/{spacecraft_id}", tags=["spacecrafts"], response_model=list[Spacecraft])
async def read_spacecraft(spacecraft_id: int):
    for spacecraft in spacecrafts:
        if spacecraft.id == spacecraft_id:
            return spacecraft
    return None


@router.post("/api/spacecrafts", tags=["spacecrafts"], response_model=list[Spacecraft])
async def _(spacecraft: Spacecraft):
    spacecrafts.append(spacecraft)
    return None
from pydantic import BaseModel, Field, root_validator, validator
from typing import List, Optional

class TargetBase(BaseModel):
    name: str
    country: str
    notes: Optional[str] = None
    complete: bool = False

class TargetCreate(TargetBase):
    pass

class TargetUpdateNotes(BaseModel):
    notes: str

class TargetUpdateComplete(BaseModel):
    complete: bool

class TargetOut(TargetBase):
    id: int

    model_config = dict(from_attributes=True)

class MissionBase(BaseModel):
    cat_id: Optional[int] = None
    complete: bool = False

class MissionCreate(MissionBase):
    targets: List[TargetCreate]

class MissionUpdate(MissionBase):
    pass

class MissionOut(MissionBase):
    id: int
    targets: List[TargetOut]

    model_config = dict(from_attributes=True)
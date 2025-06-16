import logging
from typing import List
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from fastapi import APIRouter, Depends, HTTPException, status
from app.crud.mission_crud import (
    create_mission_with_targets, get_mission, get_all_missions, delete_mission,
    assign_cat_to_mission, update_target_notes, update_target_complete
)
from app.schemas.mission_schema import (
    MissionCreate, MissionOut, TargetUpdateNotes, TargetUpdateComplete
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
logger = logging.getLogger("spy_cats_api")
logging.basicConfig(level=logging.INFO)

@router.post("/", response_model=MissionOut, status_code=status.HTTP_201_CREATED)
def api_create_mission(mission_in: MissionCreate, db: Session = Depends(get_db)):
    try:
        logger.info(f"Received mission creation request: {mission_in}")
        mission = create_mission_with_targets(db, mission_in)
        logger.info(f"Mission created successfully with id: {mission.id}")
        return mission
    except Exception as e:
        logger.error("Error creating mission", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected error occurred while creating mission: {str(e)}",
        )

@router.get("/", response_model=List[MissionOut])
def api_list_missions(db: Session = Depends(get_db)):
    return get_all_missions(db)

@router.get("/{mission_id}", response_model=MissionOut)
def api_get_mission(mission_id: int, db: Session = Depends(get_db)):
    mission = get_mission(db, mission_id)
    if not mission:
        raise HTTPException(status_code=404, detail="Mission not found")
    return mission

@router.delete("/{mission_id}", status_code=status.HTTP_204_NO_CONTENT)
def api_delete_mission(mission_id: int, db: Session = Depends(get_db)):
    success = delete_mission(db, mission_id)
    if not success:
        raise HTTPException(status_code=400, detail="Mission cannot be deleted (assigned or not found)")
    return

@router.put("/{mission_id}/assign-cat/{cat_id}", response_model=MissionOut)
def api_assign_cat(mission_id: int, cat_id: int, db: Session = Depends(get_db)):
    mission = assign_cat_to_mission(db, mission_id, cat_id)
    if not mission:
        raise HTTPException(status_code=404, detail="Mission not found")
    return mission

@router.patch("/targets/{target_id}/notes", response_model=TargetUpdateNotes)
def api_update_target_notes(target_id: int, notes_in: TargetUpdateNotes, db: Session = Depends(get_db)):
    target = update_target_notes(db, target_id, notes_in.notes)
    if not target:
        raise HTTPException(status_code=400, detail="Cannot update notes (target or mission complete, or not found)")
    return target

@router.patch("/targets/{target_id}/complete", response_model=TargetUpdateComplete)
def api_update_target_complete(target_id: int, complete_in: TargetUpdateComplete, db: Session = Depends(get_db)):
    target = update_target_complete(db, target_id, complete_in.complete)
    if not target:
        raise HTTPException(status_code=404, detail="Target not found")
    return target
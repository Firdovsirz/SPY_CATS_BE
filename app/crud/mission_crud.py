from sqlalchemy.orm import Session
from app.models.mission_model import Mission, Target
from app.schemas.mission_schema import MissionCreate, TargetUpdateNotes, TargetUpdateComplete

def create_mission_with_targets(db: Session, mission_in: MissionCreate) -> Mission:
    mission = Mission(cat_id=mission_in.cat_id, complete=mission_in.complete)
    for target_in in mission_in.targets:
        target = Target(
            name=target_in.name,
            country=target_in.country,
            notes=target_in.notes,
            complete=target_in.complete,
        )
        mission.targets.append(target)
    db.add(mission)
    db.commit()
    db.refresh(mission)
    return mission

def get_mission(db: Session, mission_id: int) -> Mission | None:
    return db.query(Mission).filter(Mission.id == mission_id).first()

def get_all_missions(db: Session) -> list[Mission]:
    return db.query(Mission).all()

def delete_mission(db: Session, mission_id: int) -> bool:
    mission = get_mission(db, mission_id)
    if not mission:
        return False
    if mission.cat_id is not None:
        return False
    db.delete(mission)
    db.commit()
    return True

def assign_cat_to_mission(db: Session, mission_id: int, cat_id: int) -> Mission | None:
    mission = get_mission(db, mission_id)
    if not mission:
        return None
    mission.cat_id = cat_id
    db.commit()
    db.refresh(mission)
    return mission

def update_target_notes(db: Session, target_id: int, notes: str) -> Target | None:
    target = db.query(Target).filter(Target.id == target_id).first()
    if not target:
        return None
    if target.complete or target.mission.complete:
        return None
    target.notes = notes
    db.commit()
    db.refresh(target)
    return target

def update_target_complete(db: Session, target_id: int, complete: bool) -> Target | None:
    target = db.query(Target).filter(Target.id == target_id).first()
    if not target:
        return None
    target.complete = complete
    db.commit()
    db.refresh(target)
    return target
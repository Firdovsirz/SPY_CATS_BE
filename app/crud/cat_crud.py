import requests
from sqlalchemy.orm import Session
from app.models.cat_model import Cat
from app.schemas.cat_schema import CatCreate, CatUpdateSalary

def fetch_allowed_breeds():
    try:
        response = requests.get("https://api.thecatapi.com/v1/breeds", timeout=5)
        response.raise_for_status()
        return [breed["name"] for breed in response.json()]
    except Exception as e:
        raise ValueError(f"Could not fetch breeds from TheCatAPI: {e}")

def create_cat(db: Session, cat: CatCreate) -> Cat:
    allowed_breeds = fetch_allowed_breeds()
    if cat.breed not in allowed_breeds:
        raise ValueError(f"Breed '{cat.breed}' is not allowed. Allowed breeds: {', '.join(allowed_breeds)}")
    db_cat = Cat(
        name=cat.name,
        years_experience=cat.years_experience,
        breed=cat.breed,
        salary=cat.salary
    )
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat

def delete_cat(db: Session, cat_id: int) -> bool:
    cat = db.query(Cat).filter(Cat.id == cat_id).first()
    if cat:
        db.delete(cat)
        db.commit()
        return True
    return False

def update_cat_salary(db: Session, cat_id: int, salary_data: CatUpdateSalary) -> Cat:
    cat = db.query(Cat).filter(Cat.id == cat_id).first()
    if cat:
        cat.salary = salary_data.salary
        db.commit()
        db.refresh(cat)
    return cat

def get_cat(db: Session, cat_id: int) -> Cat:
    return db.query(Cat).filter(Cat.id == cat_id).first()

def get_all_cats(db: Session) -> list[Cat]:
    return db.query(Cat).all()
import requests
from pydantic import BaseModel, validator

def fetch_allowed_breeds():
    try:
        response = requests.get("https://api.thecatapi.com/v1/breeds", timeout=5)
        response.raise_for_status()
        breeds = [breed["name"] for breed in response.json()]
        print({"status": "success", "code": 200, "message": "Fetched allowed breeds successfully."})
        return breeds, "Fetched allowed breeds successfully."
    except Exception as e:
        error_msg = f"Could not fetch breeds from TheCatAPI: {e}"
        print({"status": "error", "code": 500, "message": error_msg})
        return [], error_msg

ALLOWED_BREEDS, _ = fetch_allowed_breeds()

class CatBase(BaseModel):
    name: str
    years_experience: int
    breed: str
    salary: float

    @validator("breed")
    def validate_breed(cls, v):
        if v not in ALLOWED_BREEDS:
            raise ValueError({
                "status": "error",
                "code": 400,
                "message": f"'{v}' is not a valid breed. Allowed: {', '.join(ALLOWED_BREEDS)}"
            })
        return v

class CatCreate(CatBase):
    pass

class CatUpdateSalary(BaseModel):
    salary: float

class CatOut(BaseModel):
    id: int
    name: str
    years_experience: int
    breed: str
    salary: float

    model_config = dict(from_attributes=True)
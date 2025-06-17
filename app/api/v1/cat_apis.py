from typing import List, Optional, Any
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from fastapi import APIRouter, Depends, status, Request
from fastapi.responses import JSONResponse
from app.schemas.cat_schema import CatCreate, CatOut, CatUpdateSalary
from app.crud.cat_crud import create_cat, delete_cat, update_cat_salary, get_cat, get_all_cats

import logging

logger = logging.getLogger("spy_cats_api")
logging.basicConfig(level=logging.INFO)

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def success_response(
    message: str,
    data: Optional[Any] = None,
    status_code: int = status.HTTP_200_OK,
):
    return JSONResponse(
        status_code=status_code,
        content={
            "status_code": status_code,
            "message": message,
            "data": data,
        },
    )

def error_response(
    message: str,
    status_code: int = status.HTTP_400_BAD_REQUEST,
    details: Optional[Any] = None,
):
    return JSONResponse(
        status_code=status_code,
        content={
            "status_code": status_code,
            "message": message,
            "details": details,
        },
    )

@router.post("/", status_code=status.HTTP_201_CREATED)
def api_create_cat(cat: CatCreate, db: Session = Depends(get_db)):
    try:
        created_cat = create_cat(db, cat)
        cat_out = CatOut.from_orm(created_cat)
        return success_response(
            message="Spy cat created successfully",
            data=cat_out.dict(),
            status_code=status.HTTP_201_CREATED,
        )
    except ValueError as e:
        return error_response(
            message="Failed to create spy cat.",
            status_code=status.HTTP_400_BAD_REQUEST,
            details=str(e),
        )
    except Exception as e:
        return error_response(
            message="Unexpected error occurred while creating spy cat.",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            details=str(e),
        )
@router.get("/")
def api_list_cats(db: Session = Depends(get_db)):
    try:
        cats = get_all_cats(db)
        cats_out = [CatOut.from_orm(cat).dict() for cat in cats]
        logger.info(f"Retrieved {len(cats_out)} spy cats successfully.")
        return success_response(
            message="Spy cats retrieved successfully.",
            data=cats_out,
            status_code=status.HTTP_200_OK,
        )
    except Exception as e:
        logger.error(f"Unexpected error occurred while retrieving spy cats: {e}", exc_info=True)
        return error_response(
            message="Unexpected error occurred while retrieving spy cats.",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            details=str(e),
        )
    
@router.get("/{cat_id}")
def api_get_cat(cat_id: int, db: Session = Depends(get_db)):
    try:
        cat = get_cat(db, cat_id)
        if not cat:
            logger.warning(f"Cat with id {cat_id} not found.")
            return error_response(
                message="Cat not found.",
                status_code=status.HTTP_404_NOT_FOUND,
                details=f"No cat with id {cat_id}",
            )
        cat_out = CatOut.from_orm(cat)
        return success_response(
            message="Spy cat retrieved successfully.",
            data=cat_out.dict(),
            status_code=status.HTTP_200_OK,
        )
    except Exception as e:
        logger.error(f"Error retrieving cat with id {cat_id}: {e}", exc_info=True)
        return error_response(
            message="Unexpected error occurred while retrieving spy cat.",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            details=str(e),
        )
    
    except Exception as e:
        logger.error(f"Error retrieving cat with id {cat_id}: {e}", exc_info=True)
        return error_response(
            message="Unexpected error occurred while retrieving spy cat.",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            details=str(e),
        )

@router.delete("/{cat_id}")
def api_delete_cat(cat_id: int, db: Session = Depends(get_db)):
    try:
        success = delete_cat(db, cat_id)
        if not success:
            return error_response(
                message="Cat not found.",
                status_code=status.HTTP_404_NOT_FOUND,
                details=f"No cat with id {cat_id}",
            )
        return success_response(
            message="Spy cat deleted successfully.",
            data=None,
            status_code=status.HTTP_200_OK,
        )
    except Exception as e:
        return error_response(
            message="Unexpected error occurred while deleting spy cat.",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            details=str(e),
        )

@router.patch("/{cat_id}/salary")
def api_update_cat_salary(cat_id: int, salary_data: CatUpdateSalary, db: Session = Depends(get_db)):
    try:
        cat = update_cat_salary(db, cat_id, salary_data)
        if not cat:
            logger.warning(f"Cat with id {cat_id} not found for salary update.")
            return error_response(
                message="Cat not found.",
                status_code=status.HTTP_404_NOT_FOUND,
                details=f"No cat with id {cat_id}",
            )
        cat_out = CatOut.from_orm(cat)
        return success_response(
            message="Spy cat salary updated successfully.",
            data=cat_out.dict(),
            status_code=status.HTTP_200_OK,
        )
    except Exception as e:
        logger.error(f"Error updating salary for cat id {cat_id}: {e}", exc_info=True)
        return error_response(
            message="Unexpected error occurred while updating spy cat salary.",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            details=str(e),
        )

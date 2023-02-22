import datetime as dt
from os import error, rename, path
from urllib.parse import urlencode
from typing import List
import requests
from fastapi import APIRouter, Depends  # Body,
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app import config, models, utils, schemas


router = APIRouter()


@router.get("/organisations", response_model=List[models.Organisation])
def get_organisations(*, db: Session = Depends(utils.get_db)):
    organisations = db.query(schemas.Organisation).all()
    return organisations
    


@router.get("/organisation", response_model=models.Organisation)
def get_organisation(*, db: Session = Depends(utils.get_db), id: int):
    organisation = db.query(schemas.Organisations).filter(schemas.Organisation.id == id).first()
    return organisation


@router.post("/organisation", response_model=models.Organisation)
def create_organisation(
    *,
    db: Session = Depends(utils.get_db),
    organisation: models.Organisation
):
    organisation_data = organisation.dict(exclude_unset=True)
    db_organisation = schemas.Organisation(**organisation_data)
    db.add(db_organisation)
    db.commit()
    
    return db_organisation


@router.delete("/organisation")
def delete_organisation(
    *, db: Session = Depends(utils.get_db), id: int
):
    db.query(schemas.Organisation).filter(schemas.Organisation.id == id).delete()
    db.commit()

@router.put("/organisation")
def update_organisation(
    *, db: Session = Depends(utils.get_db),
    organisation: models.Organisation,
    id: int
):
    organisation_data = organisation.dict(exclude_unset=True)
    db.query(schemas.Organisation).filter(schemas.Organisation.id == id).update(organisation_data)
    db.commit()
    return organisation
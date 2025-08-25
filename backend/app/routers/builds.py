
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Build
from app.schemas import BuildCreate, Build as BuildSchema
from app.email_utils import send_failure_email
import os

router = APIRouter(prefix="/builds", tags=["builds"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=BuildSchema)

def create_build(build: BuildCreate, db: Session = Depends(get_db)):
    db_build = Build(**build.dict())
    db.add(db_build)
    db.commit()
    db.refresh(db_build)
    # Send email if build failed
    if not db_build.success:
        send_failure_email(
            pipeline=db_build.pipeline,
            status=db_build.status,
            timestamp=db_build.timestamp
        )
    return db_build

@router.get("/", response_model=list[BuildSchema])
def list_builds(db: Session = Depends(get_db)):
    return db.query(Build).all()

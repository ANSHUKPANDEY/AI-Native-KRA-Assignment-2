from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Build
from app.schemas import BuildCreate, Build as BuildSchema

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
    return db_build

@router.get("/", response_model=list[BuildSchema])
def list_builds(db: Session = Depends(get_db)):
    return db.query(Build).all()

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Build

router = APIRouter(prefix="/metrics", tags=["metrics"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/summary")
def get_summary(db: Session = Depends(get_db)):
    builds = db.query(Build).all()
    total = len(builds)
    success = sum(1 for b in builds if b.success)
    failure = total - success
    avg_time = sum(b.build_time for b in builds) / total if total else 0
    last_status = builds[-1].status if builds else None
    return {
        "total": total,
        "success": success,
        "failure": failure,
        "avg_time": avg_time,
        "last_status": last_status
    }

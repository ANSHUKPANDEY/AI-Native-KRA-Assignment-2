from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BuildBase(BaseModel):
    pipeline: str
    status: str
    build_time: float
    timestamp: datetime
    logs: Optional[str] = None
    success: bool

class BuildCreate(BuildBase):
    pass

class Build(BuildBase):
    id: int
    class Config:
        orm_mode = True

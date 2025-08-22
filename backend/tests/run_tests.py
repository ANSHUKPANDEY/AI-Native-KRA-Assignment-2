import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../app'))
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Build
from app.schemas import BuildCreate
from datetime import datetime

DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def test_create_build():
    db = TestingSessionLocal()
    build_data = BuildCreate(
        pipeline="TestPipeline",
        status="success",
        build_time=10.5,
        timestamp=datetime.now(),
        logs="Build completed successfully.",
        success=True
    )
    db_build = Build(**build_data.dict())
    db.add(db_build)
    db.commit()
    db.refresh(db_build)
    assert db_build.pipeline == "TestPipeline"
    assert db_build.success is True
    db.close()

if __name__ == "__main__":
    pytest.main([__file__])

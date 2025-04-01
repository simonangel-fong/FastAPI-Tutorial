from typing import Annotated, List
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import database
from app.models import TestTable, Base
from app.schemas import TestTableResponse

app = FastAPI(title="Oracle DB Connection", version="1.0.0")


@app.on_event("startup")
async def startup_event():
    try:
        Base.metadata.create_all(bind=database.engine)
    except Exception as e:
        return HTTPException(
            status_code=500, detail=f"Database error: {str(e)}")


@app.get('/', response_model=List[TestTableResponse], description="Returns all test table records")
async def get_testtb(db: Annotated[Session, Depends(database.get_db)]) -> List[TestTableResponse]:
    try:
        result = db.query(TestTable).all()
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Database error: {str(e)}")

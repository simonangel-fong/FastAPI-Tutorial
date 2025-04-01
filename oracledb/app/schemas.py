from pydantic import BaseModel


class TestTableResponse(BaseModel):
    id: int
    test_column: str

    class Config:
        from_attributes = True  # Allows conversion from SQLAlchemy objects

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.settings import get_settings

settings = get_settings()

db_host = settings.ORACLE_DB_HOST
db_service = settings.ORACLE_DB_SERVICE
db_user = settings.ORACLE_DB_USER
db_password = settings.ORACLE_DB_PWD
db_port = settings.ORACLE_DB_PORT

engine = create_engine(
    f"oracle+oracledb://{db_user}:{db_password}@{db_host}:{db_port}/?service_name={db_service}"
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

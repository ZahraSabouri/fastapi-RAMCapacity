import database as _db, models as _models, schemas as _schemas
import sqlalchemy.orm as _orm


def create_database():
    return _db.Base.metadata.create_all(bind=_db.engine)


def get_db():
    db = _db.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_record(db: _orm.Session, record: _schemas.RAMCapCreate):
    db_record = _models.RAMCapacity(date=record.date, total=record.total, free=record.free, used=record.used)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record


def get_record(db: _orm.Session, skip: int = 0, limit: int = 1000, id: int = 0):
    if id == 0:
        return db.query(_models.RAMCapacity).offset(skip).limit(limit).all()
    return db.query(_models.RAMCapacity).get({"id": id})
    

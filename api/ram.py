from re import U
import fastapi as _fastapi
from sqlalchemy import orm as _orm
import typing as _typing
import app.schemas as _schemas
import app.services as _services

router = _fastapi.APIRouter()

@router.post("/ram_capacity/", response_model=_schemas.RAMCap)
def create_record(record: _schemas.RAMCapCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return _services.create_record(db=db, record=record)


@router.get("/ram_capacity/", response_model=_typing.List[_schemas.RAMCap])
async def read_records(skip: int = 0, limit: int = 10, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    logs = _services.get_record(db=db, skip=skip, limit=limit)
    return logs

@router.get("/ram_capacity/{id}", response_model=_schemas.RAMCap)
def read_record(id: int = _fastapi.Path(..., description="The ID of the Record you want to retrieve.", gt = 0), \
    db: _orm.Session = _fastapi.Depends(_services.get_db)):
    logs = _services.get_record(db=db, id=id)
    return logs

# @router.get("/ram_capacity/all")
# async def read_records_allroute(blah: str = _fastapi.Depends(verify_token), \
#     db: _orm.Session = _fastapi.Depends(_services.get_db)):
#     logs = _services.get_record(db=db)
#     return logs
# https://www.youtube.com/watch?v=ECjGFDVifhk
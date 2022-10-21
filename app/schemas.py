import datetime as _dt
import pydantic as _pydantic


class _RAMCapBase(_pydantic.BaseModel):
    date: _dt.datetime
    total: str
    free: str
    used: str


class RAMCapCreate(_RAMCapBase):
    pass


class RAMCap(_RAMCapBase):
    id: int

    # to prevent lazy-loading
    class Config:
        orm_mode = True

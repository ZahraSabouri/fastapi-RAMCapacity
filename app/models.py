import datetime as _dt
import sqlalchemy as _sql
import database as _db


class RAMCapacity(_db.Base):
    __tablename__ = "ram_capacity"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    date = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    total = _sql.Column(_sql.String)
    free = _sql.Column(_sql.String)
    used = _sql.Column(_sql.String)
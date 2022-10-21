from http.client import HTTPException
from re import U
import fastapi as _fastapi
import services as _services
import api.ram as _ram


app = _fastapi.FastAPI()
app.include_router(_ram.router)

_services.create_database()

async def verify_token(x_token: str = _fastapi.Header(...)):
    if x_token != "ram_cap":
        raise HTTPException(status_code=400, detail="X-Token header invalid.")
    return "right access token entered"
    
@app.get("/")
async def root():
    return {"message": "ram space"}

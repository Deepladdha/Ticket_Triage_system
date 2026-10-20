import dotenv
dotenv.load_dotenv()

from app.api.routes import router
from fastapi import FastAPI

app = FastAPI()

app.include_router(router)

@app.get("/") 
async def root():
    return {"status": "ok", "service": "Ticket Triage API"}
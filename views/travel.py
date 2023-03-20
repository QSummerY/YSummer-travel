from fastapi import APIRouter
from config import DB_URI

travel = APIRouter()


@travel.get("/travel")
def hello():
    return f"hello travel, {DB_URI}"
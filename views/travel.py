from fastapi import APIRouter
from config import DB_URI
from models.travel import Journey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(DB_URI)
Session = sessionmaker(engine)

travel_route = APIRouter()

@travel_route.get("/travel")
def hello():
    return f"hello travel, {DB_URI}"


@travel_route.get("/read_one")
def read_one():
    with Session() as session:
        one_query = session.query(Journey).first().to_json()

    return f"hello travel, {one_query}"
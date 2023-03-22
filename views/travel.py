from fastapi import APIRouter
from config import DB_URI
from models.travel import Journey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schemas import JourneyBase
engine = create_engine(DB_URI)
Session = sessionmaker(engine)

travel = APIRouter()



@travel.get("/travel")
def hello():
    return f"hello travel, {DB_URI}"

@travel.post("/create")
async def create(journey: JourneyBase):
    with Session() as session:
        j1 = Journey(username = journey.username,
                    way = journey.way,
                    src_city = journey.src_city,
                    src_station = journey.src_station,
                    dest_city = journey.dest_city,
                    dest_station = journey.dest_station,
                    price = journey.price,
                    departure_time = journey.departure_time,
                    arrival_time = journey.arrival_time,
                    desc = journey.desc,
                    )
        session.add(j1)
        session.commit()
        session.close()
    return f"hello travel, {journey}"

@travel.get("/read_one")
def read_one():
    with Session() as session:
        one_query = session.query(Journey).first().to_json()

    return f"hello travel, {one_query}"
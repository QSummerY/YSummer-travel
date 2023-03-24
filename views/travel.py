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
        j1 = Journey(username=journey.username,
             way=journey.way,
             src_city=journey.src_city,
             src_station=journey.src_station,
             dest_city=journey.dest_city,
             dest_station=journey.dest_station,
             price=journey.price,
             departure_time=journey.departure_time,
             arrival_time=journey.arrival_time,
             desc=journey.desc,
             )
        session.add(j1)
        session.commit()
        session.close()
    return {"code": 200, "data": "", "msg": "Insert Success"}


@travel.post("/update")
async def update(journey: JourneyBase):
    if type(journey.id) != int or journey.id == None:
        return {"code": 400, "data": "", "msg": "field: 'id' must be Integer and not be null"}
    with Session() as session:
        j1 = session.query(Journey).filter(Journey.id == journey.id).first()
        j1.username = journey.username
        j1.way = journey.way
        j1.src_city = journey.src_city
        j1.src_station = journey.src_station
        j1.dest_city = journey.dest_city
        j1.dest_station = journey.dest_station
        j1.price = journey.price
        j1.departure_time = journey.departure_time
        j1.arrival_time = journey.arrival_time
        j1.desc = journey.desc

        session.commit()
        session.close()
    return {"code": 200, "data": "", "msg": "Update Success"}


@travel.get("/read_all")
def read_all():
    with Session() as session:
        all_query = session.query(Journey).order_by(Journey.id.desc()).all()
        data = []
        for item in all_query:
            data.append(item.to_json())

    return {"code": 200, "data": data, "msg": "Query success"}


@travel.get("/read_one")
def read_one(id: int = 0, username: str = ""):
    #id和username 参数 2选1
    if (id == 0 and username == "") or (id > 0 and username != ""):
        return {"code": 400, "data": "", "msg": "param: id/username must use one arg"}

    with Session() as session:
        if id == 0: #如果没传id，则使用username查询，否则查询id
            data = session.query(Journey).filter(Journey.username == username).first()
        else:
            data = session.query(Journey).filter(Journey.id == id).first()

    return {"code": 200, "data": data, "msg": "Query success"}

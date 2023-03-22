from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class JourneyBase(BaseModel):
    username: str
    way: int
    price: int
    src_city: str
    src_station: str
    dest_city: str
    dest_station: str
    departure_time: datetime
    arrival_time: datetime
    desc: Optional[str] = ""

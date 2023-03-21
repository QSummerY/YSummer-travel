from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
import os, sys
real_dir=os.getcwd()
sys.path.append(real_dir)
from app import engine



Base = declarative_base()



class Journey(Base):
    __tablename__ = 'journey'
    id = Column(Integer, primary_key=True)
    username = Column(String(32))
    way = Column(Integer) #出行方式 1: 火车高铁  2：飞机  3：大巴  4：轮船
    price = Column(Integer)  # 票价
    src_city = Column(String(32))  #出发城市
    src_station = Column(String(32))  #出发地车站/机场
    dest_city = Column(String(32))  #目的地城市
    dest_station = Column(String(32))  #目的地车站/机场
    departure_time = Column(DateTime) #出行时间
    arrival_time = Column(DateTime) #到达到时间
    desc = Column(String(128))  #出行描述，原因

Base.metadata.create_all(engine)

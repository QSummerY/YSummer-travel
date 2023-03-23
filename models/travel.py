from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
import os, sys, json
real_dir=os.getcwd()
sys.path.append(real_dir)
from config import DB_URI
from sqlalchemy import create_engine
engine = create_engine(DB_URI)




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

    def to_json(self):
        dict = {}
        dict.update(self.__dict__)
        if "_sa_instance_state" in dict:
            del dict['_sa_instance_state']
        if 'departure_time' in dict:  dict['departure_time'] = dict['departure_time'].strftime("%Y-%m-%d %H:%M:%S")
        if 'arrival_time' in dict:  dict['arrival_time'] = dict['arrival_time'].strftime("%Y-%m-%d %H:%M:%S")
        return dict

Base.metadata.create_all(engine)
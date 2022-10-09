from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DateTime
import datetime

Base = declarative_base()

class Task(Base):
    __tablename__="task"
    id=Column(Integer,primary_key=True,autoincrement=True)
    task_no=Column(Integer)
    description=Column(String(100))
    status=Column(String(50))
    created_on=Column(DateTime,default=datetime.datetime.utcnow)
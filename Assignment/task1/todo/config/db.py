from sqlalchemy import create_engine
from models.task import Base
from sqlalchemy.orm import sessionmaker


url = 'mysql://root:root@localhost:3306/leadzen_task'

eng = create_engine(url)

Base.metadata.create_all(eng)

Session = sessionmaker(bind=eng)
sess=Session()
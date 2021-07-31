import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Candels

engine = create_engine(os.environ.get('DATABASE_URL'))
Session = sessionmaker(bind=engine)
session = Session()

item = Candels()
item.value = 5

session.add(item)

session.commit()
session.close()
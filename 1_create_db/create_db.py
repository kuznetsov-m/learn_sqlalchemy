import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

from sqlalchemy import create_engine
import models

engine = create_engine(os.getenv('DATABASE_URL'))

models.Base.metadata.create_all(engine)
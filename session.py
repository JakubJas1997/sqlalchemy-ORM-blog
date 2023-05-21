from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "postgresql://postgres:qwerty@localhost:5432/blog")
    #"mysql+pymysql://postgres:qwerty@localhost:3306/blog"
Session = sessionmaker(bind=engine)
session = Session()
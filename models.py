import datetime

from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from session import engine

Base = declarative_base(bind=engine)


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    user_name = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    registration_date = Column(
        DateTime, default=datetime.datetime.now, nullable=False
    )
    articles = relationship("Article")

    def __repr__(self):
        return f"Author nickname: {self.user_name}"


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False, unique=True)
    content = Column(Text, nullable=False)
    publication_date = Column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now
    )
    author_id = Column(
        Integer,
        ForeignKey("authors.id"),
        nullable=False
    )

    def __repr__(self):
        return f"Article title: {self.title}"


Base.metadata.create_all()

"""Provides a application wide SQLAlchemy session."""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from maproulette.settings import DB_URI
from sqlalchemy.ext.declarative import declarative_base

Session = sessionmaker(bind=create_engine(DB_URI))
session = scoped_session(Session)

Base = declarative_base()

#!/usr/bin/env python3
import sqlalchemy
from sqlalchemy import Sequence
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

# Set your DB_URL
URL = 'sqlite:///:memory:'

# Create a default engine fro connecting to your DB
engine = create_engine(URL, echo=True)

# Create your declarative base
Base = declarative_base()

# Create a user based on the declarative
class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, Sequence('seq_id_user'), primary_key=True)
	name = Column(String(20))
	age = Column(Integer)
	address = Column(String(50))

	def __repr__(self):
		return ("<Name = {}, Age = {} and Address = {}>".
				format(self.name, self.age, self.address))
User.__table__

#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import models
import os

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = ""
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(length=128), nullable=False)
        cities = relationship("City", backref='state',
                          cascade='all, delete')
    def __init__(self, *args, **kwargs):
        """init """
        super().__init__(*args, **kwagrs)

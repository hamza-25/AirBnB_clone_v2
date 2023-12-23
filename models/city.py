#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship
import os



class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    # state_id = ""
    # name = ""
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        # __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities", cascade="all, delete")
    else:
        state_id = ""
        name = ""
    
    # def __init__(self, *args, **kwargs):
    #     """ init """
    #     super().__init__(*args, **kwargs)

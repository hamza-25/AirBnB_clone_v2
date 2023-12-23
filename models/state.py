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
    
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        # __tablename__ = "states"
        name = Column(String(length=128), nullable=False)
        cities = relationship("City", backref='state',
                          cascade='all, delete')
    else:
        name = ""

    # def __init__(self, *args, **kwargs):
    #     """init """
    #     super().__init__(*args, **kwargs)
        

    # if models.is_type != 'db':
    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            cities_list = []
            all_cities = models.storage.all(City).values()
            for city in all_cities:
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list

#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import os
from sqlalchemy import String, Integer, Column, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column (String(128), ForeignKey("cities.id"))
        user_id = Column (String(128), ForeignKey("users.id"))
        #users = relationship('User', backref='places')
        #cities = relationship('City', backref='places')


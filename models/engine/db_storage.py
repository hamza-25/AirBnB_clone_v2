#!/usr/bin/python3
""" """
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, text, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session, relationship


class DBStorage:
    """DBStorage Class"""
    __engine = None
    __session = None
    #user = getenv('HBNB_MYSQL_USER')
    #pwd = getenv('HBNB_MYSQL_PWD')
    #host = getenv('HBNB_MYSQL_HOST')
    #db = getenv('HBNB_MYSQL_DB')
    #environment = getenv('HBNB_ENV')

    #reviews = relationship('Place', backref='reviews', cascade='all, delete')
    def __init__(self):
        """ """
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        environment = getenv('HBNB_ENV')
        url_engine = f"mysql+mysqldb://{user}:{pwd}@{host}/{db}"
        self.__engine = create_engine(url_engine, pool_pre_ping=True)
        metadata = MetaData()
        if environment == 'test':
            metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ """
        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            instances = self.__session.query(cls).all()
            new_dict = {}
            for item in instances:
                create_key = "{}.{}".format(cls.__name__, item.__dict__.id)
                # if '_sa_instance_state' in item.__dict__.keys():
                    # del item.__dict__['_sa_instance_state']
                new_dict[create_key] = cls(**item)
        else:
            models = [User, State, City, Amenity, Place, Review]
            new_dict = {}
            for model in models:
                instances = self.__session.query(model).all()
                for item in instances:
                    create_key = "{}.{}".format(model.__name__, item.id)
                    # if '_sa_instance_state' in item.__dict__.keys():
                        # del item.__dict__['_sa_instance_state']
                    new_dict[create_key] = model(**item)
        # self.__session.close()
        print (new_dict)
        exit(0)
        return new_dict

    def new(self, obj):
        """ """
        self.__session.add(obj)

    def save(self):
        """ """
        self.__session.commit()

    def delete(self, obj=None):
        """ """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

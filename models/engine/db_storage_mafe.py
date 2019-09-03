#!/usr/bin/python3
"""This is the db storage class for AirBnB"""
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import (create_engine)
from sqlalchemy import MetaData, Table
from sqlalchemy.orm import sessionmaker

HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD =  getenv('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
HBNB_ENV = getenv('HBNB_ENV')


class DBStorage:
    """Define new engine DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """create the engine, the engine must be linked to
        the MySQL database and user  """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB), pool_pre_ping=True)
        if HBNB_ENV == 'test':
            metadata = MetaData()
            metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """method must return a dictionary like file storage"""
       
        dict_query = {}
        if cls:
            query = self.__session.query(cls).all()
            key = cls__name__ + '.'
            for iter in query:
                dict_query[key + iter.id] = iter
            return (dict_query)
        
        else:
            for allclass_iter in [BaseModel, User, State, City, Amenity, Place, Review]:
                query = self.__session.query(allclass_iter).all()
                key = cls__name__ + '.' 
                for iter in query:
                    dict_query[key + iter.id] = iter
            return (dict_query)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            delete_obj = session.query(type(obj)).filter(type(obj.id).like(obj.id))
            session.delete(delete_obj)
            self.save()

    def reload(self):
        """create all tables in the database (feature of SQLAlchemy) and
        create the current database session"""

        Session.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()

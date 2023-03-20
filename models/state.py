#!/usr/bin/python3
"""Class for State model"""
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base 
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all delete', backref='states')
    else:
        name = ''
        
    def __init__(self, *args, **kwargs):
        """Initializes state"""
        super().__init__(*args, **kwargs)
        
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """fs getter attribute that returns City instances"""
            values_city = models.storage.all('City').values()
            list_city = []
            for city in values_city:
                if city.state_id == self.id:
                    list_city.append(city)
            return list_city
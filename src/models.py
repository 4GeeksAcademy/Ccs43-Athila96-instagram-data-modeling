import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    nick_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=True)
    number_phone = Column(String(10), nullable=False)
    password = Column(String(20), nullable=False)
    post = relationship("Post", back_populates="user")
    reels = relationship("Reels", back_populates="user")
    storis = relationship("Storis", back_populates="user")
    notifocations = relationship("Notifications", back_populates="user")
    follower = relationship("Follower", back_populates="user")

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    image = Column(String(250), nullable=False)
    video = Column(String(250), nullable=False)
    like = Column(String(250), nullable=False)
    comments = Column(String(500), nullable=False)
    user_id = Column(ForeignKey("user.id"))
    user = relationship("User", back_populates="post")

class Reels(Base):
    __tablename__ = 'reels'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    image = Column(String(250), nullable=False)
    video = Column(String(250), nullable=False)
    like = Column(String(250), nullable=False)
    reproductions = Column(Integer, nullable=False)
    comments = Column(String(500), nullable=False)
    user_id = Column(ForeignKey("user.id"))
    user = relationship("User", back_populates="reels")

class Storis(Base):
    __tablename__ = 'storis'

    id = Column(Integer, primary_key=True)
    image = Column(String(250), nullable=False)
    video = Column(String(250), nullable=False)
    reactions = Column(String(250), nullable=False)
    visualizations = Column(Integer, nullable=False)
    user_id = Column(ForeignKey("user.id"))
    user = relationship("User", back_populates="storis")

class Notifications(Base):
    __tablename__ = 'notifications'

    id = Column(Integer, primary_key=True)
    notification = Column(Integer, nullable=True)
    user_id = Column(ForeignKey("user.id"))
    user = relationship("User", back_populates="notifications")
    follower_id = Column(ForeignKey("follower.id"))
    follower = relationship("Follower", back_populates="notifications")


class Follower(Base):
    __tablename__ = 'follower'

    id = Column(Integer, primary_key=True)
    id_follower = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("user.id"))
    user = relationship("User", back_populates="follower")
    notifocations = relationship("Notifications", back_populates="follower")


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

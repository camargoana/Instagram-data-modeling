import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    username = Column(String(16), nullable = False)
    email = Column(String(64), nullable = False)
    phonemobile=Column(String(16), nullable = False)
    email = Column(String(64), nullable = False)
    password= Column(String(80),nullable=False)
    status= Column(String(128),nullable=False)
    message = relationship('message', backref='user')
    mediaformat = relationship('mediaformat', backref='user')
    fileresource = relationship('fileresource', backref='user')
    post = relationship('Post', backref='user')
    reel = relationship('Reel', backref='user')
    livestream = relationship('livestream', backref='user')
    history = relationship('History', backref='user')
    post_like = relationship('PostLike', backref='user')
    reel_like = relationship('ReelLike', backref='user')
    livestream_like = relationship('livestreamLike', backref='user')
    post_comment = relationship('PostComment', backref='user')
    reel_comment = relationship('ReelComment', backref='user')
    livestream_comment = relationship('livestreamComment', backref='user')
    history_comment = relationship('HistoryComment', backref='user')
    history_reaction = relationship('HistoryReaction', backref='user')

class message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    textmessage = Column(String(128), nullable = True)
    status= Column(String(128),nullable=False)
    post = relationship("Post")
    reel = relationship("Reel")
    history = relationship("History")
    livestream = relationship("livestream")

class mediaformat(Base):
    __tablename__ = 'mediaformat'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    username = Column(String(16), nullable = False)
    typeof = Column(String(128), nullable = False)
    description = Column(String(256), nullable = True)
    status= Column(String(128),nullable=False)
    post = relationship("Post")
    reel = relationship("Reel")
    history = relationship("History")
    livestream = relationship("livestream")

class fileresource(Base):
    __tablename__ = 'fileresource'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    filetype = Column(String(16), nullable = False)
    fileformat = Column(String(16), nullable = False)
    filesize = Column(String(16), nullable = False)
    status= Column(String(128),nullable=False)
    post = relationship("Post")
    reel = relationship("Reel")
    history = relationship("History")
    livestream = relationship("livestream")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    photo = Column(String(128), nullable = True)
    video = Column(String(128), nullable = True)
    location = Column(String(128), nullable = True)
    caption = Column(String(256), nullable = True)
    mediaformat = relationship('mediaformat')
    fileresource = relationship('fileresource')

class PostLike(Base):
    __tablename__ = 'post_like'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship("Post")
    message = relationship('message')
   

class Reel(Base):
    __tablename__ = 'reel'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    video = Column(String(128), nullable = False)
    effect = Column(String(16), nullable = True)
    song = Column(String(64), nullable = True)
    mediaformat = relationship('mediaformat')
    fileresource = relationship('fileresource')

class ReelLike(Base):
    __tablename__ = 'reel_like'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    reel_id = Column(Integer, ForeignKey('reel.id'))
    reel = relationship("Reel")
    message = relationship('message')
   
class ReelComment(Base):
    __tablename__ = 'reel_comment'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    reel_id = Column(Integer, ForeignKey('reel.id'))
    reel = relationship("Reel")
    message = relationship('message')

class History(Base):
    __tablename__ = 'history'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    photo = Column(String(128), nullable = True)
    video = Column(String(128), nullable = True)
    effect = Column(String(128), nullable = True)
    text = Column(String(128), nullable = True)
    song = Column(String(64), nullable = True)
    mediaformat = relationship('mediaformat')
    fileresource = relationship('fileresource')

class HistoryComment(Base):
    __tablename__ = 'history_comment'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    history_id = Column(Integer, ForeignKey('history.id'))
    history = relationship("History")
    message = relationship('message')


class HistoryReaction(Base):
    __tablename__ = 'history_reaction'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    history_id = Column(Integer, ForeignKey('history.id'))
    history = relationship("History")

class Livestream(Base):
    __tablename__ = 'livestream'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    video = Column(String(128), nullable = False)
    location = Column(String(128), nullable = True)
    caption = Column(String(256), nullable = True)
    mediaformat = relationship('mediaformat')
    fileresource = relationship('fileresource')

class LivestreamLike(Base):
    __tablename__ = 'Livestream_like'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    livestream_id = Column(Integer, ForeignKey('livestream.id'))
    livestream = relationship("livestream")

class PostComment(Base):
    __tablename__ = 'post_comment'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship("Post")    

class LivestreamComment(Base):
    __tablename__ = 'livestream_comment'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    livestream_id = Column(Integer, ForeignKey('livestream.id'))
    livestream = relationship("livestream")
    message = relationship('message')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
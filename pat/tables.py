from eve.io.sql.decorators import registerSchema
from eve.io.sql.common import CommonColumns
from eve.io.sql import db


@registerSchema('users')
class Users(CommonColumns):
    __tablename__ = 'users'
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(120))
    fullname = db.Column(db.String(120))
    birthday = db.Column(db.String(10))
    mobile = db.Column(db.String(13))
    password = db.Column(db.String(64))
    email = db.Column(db.String(64), unique=True)
    

@registerSchema('membercode')
class Membercode(CommonColumns):
    __tablename__ = 'membercode'
    code = db.Column(db.String(4), unique=True)


@registerSchema('preregistration')
class Preregi(CommonColumns):
    __tablename__ = 'preregistration'
    email = db.Column(db.String(64))
    verification_code = db.Column(db.String(64), unique=True)
    mem_code = db.Column(db.String(32))


@registerSchema('questions')
class Questions(CommonColumns):
    __tablename__ = 'questions'
    question = db.Column(db.String(64))
    dateasked = db.Column(db.DateTime)
    askedby = db.Column(db.String(120), db.ForeignKey('users._id'))
    

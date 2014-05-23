from eve.io.sql.decorators import registerSchema
from eve.io.sql.common import CommonColumns
from eve.io.sql import db

@registerSchema('users')
class Users(CommonColumns):
    __tablename__ = 'users'
    firstname = db.Column(db.String(32), unique=True, index=True) 
    lastname  = db.Column(db.String(64)) 
    email = db.Column(db.String(64)) 
    birthday = db.Column(db.String(64))
    mobile = db.Column(db.String(64))  
    password = db.Column(db.String(64)) 

@registerSchema('stores')
class Stores(CommonColumns):
    __tablename__ = 'stores'
    storename = db.Column(db.String(100), unique=True, index=True) 
    address = db.Column(db.String(100)) 
    contact = db.Column(db.String(50))

@registerSchema('mystores')
class MyStores(CommonColumns):
    __tablename__ = 'mystores'
    storename = db.Column('stores_name', db.String(100), db.ForeignKey('stores._id')) 
    username = db.Column('users_id', db.String(100), db.ForeignKey('users._id')) 
    
@registerSchema('healthadvisors')
class HealthAdvisors(CommonColumns):
    __tablename__ = 'healthadvisors'
    name = db.Column(db.String(100), unique=True, index=True)
    specialty = db.Column(db.String(100))
    store = db.Column(db.String(100), db.ForeignKey('stores._id'))
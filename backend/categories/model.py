from backend.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Category(db.Model):
    __tablename__ = "categories"
    name:str
    image:str
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255),unique=True)
    image = db.Column(db.String(255),nullable=True)
    created_by  = db.Column(db.Integer,db.ForeignKey('users.id'))
    created_at = db.Column(db.String(255),nullable=True, default=datetime.now())
    updated_at = db.Column(db.String(255),nullable=True, onupdate=datetime.now())
    fooditems = db.relationship("FoodItem", backref='category', remote_side=[id], lazy='dynamic')
   

    def __init__(self, image, name,created_by):
     self.image = image
     self.name = name
     self.created_by = created_by
    #  self.created_at = created_at
    #  self.updated_at = updated_at
    

    def __repr__(self):
        return f"<Category {self.name} >"

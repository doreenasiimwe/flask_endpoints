from backend.db import db

class Address(db.Model):
    __tablename__ = "addresses"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255),nullable=False)
    district_id = db.Column(db.Integer,db.ForeignKey('districts.id'))
    user_id  = db.Column(db.Integer,db.ForeignKey('users.id'))
    created_at = db.Column(db.String(255),nullable=True)
    updated_at = db.Column(db.String(255),nullable=True)
   

    def __init__(self, district_id, name,user_id,created_at,updated_at):
     self.district_id = district_id
     self.name = name
     self.user_id = user_id
     self.created_at = created_at
     self.updated_at = updated_at
    

    def __repr__(self):
        return f"<Address {self.name} >"

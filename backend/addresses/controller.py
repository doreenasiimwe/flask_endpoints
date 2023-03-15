from flask import  jsonify, request, Blueprint
from backend.addresses.model import Address
from backend.db import db
import datetime
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

addresses = Blueprint('addresses', __name__, url_prefix='/addresses')

#get all addresses
@addresses.route("/")
def all_addresses():
    addresses= Address.query.all()
    return jsonify({
            "success":True,
            "data":addresses,
            "total":len(addresses)
        }),200



#creating addresses
@jwt_required()
@addresses.route('/create', methods= ['POST'])
def create_new_address():

    data = request.get_json()
    name = data['name']
    district_id = data['district_id']
    user_id =get_jwt_identity()
    
      
  
    #validations
    if not name:
         return jsonify({'error':"Address name is required"})
   
    if not district_id:
         return jsonify({'error':"District  name is required"})
    

    #check for an address with same district
    if Address.query.filter_by(district_id=district_id).first() is not None and Address.query.filter_by(user_id=user_id).first() :
        return jsonify({'error': "Address with this district name exists"}), 409 

    new_address =Address(name=name,district_id=district_id,user_id=user_id, created_at=datetime.now()) 
      
    #inserting values
    db.session.add( new_address)
    db.session.commit()
    return jsonify({'message':'New address created sucessfully','data': new_address}),201
          
   
  
    

#get,edit and delete address by id
@jwt_required()
@addresses.route('/address/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_address(id):
    address = Address.query.get_or_404(id)

    if request.method == 'GET':
        response = {
            "id":address.id,
            "name": address.name,
            "user": address.user.name,
            "created_at": address.created_at
          
        }
        return {"success": True, "address": response,"message":"Address details retrieved"}

    elif request.method == 'PUT':
        data = request.get_json()

        if not data['name']:
            return jsonify({"message":"address name is required"})
        
        if not data['district_id']:
            return jsonify({"message":"address region name is required"})
        
        
        address.name = data['name']
        address.district_id = data['district_id']
        address.user_id = get_jwt_identity()
        address.updated_at = datetime.utcnow()
        db.session.add(address)
        db.session.commit()
        return {"message": f"{address.name}  address updated successfully"}

    elif request.method == 'DELETE':
        db.session.delete(address)
        db.session.commit()
        return {"message": f"{address.name} address successfully deleted."}   
  
        
  
   




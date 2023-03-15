from flask import Blueprint,request,jsonify
from backend.db import db
from backend.food_items.model import FoodItem
import datetime
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

food_items = Blueprint('food_items',__name__,url_prefix='/food_items')



#get all food_items
@food_items.route("/")
def all_food_items():
    food_items = FoodItem.query.all()
    
    response = [{
                "id":item.id,
                "name": item.name,
                "created_by":item.created_by,
                "created_at": item.created_at,
            }for item in food_items]
        
    return jsonify({"success":True,"data":response,"total":len(food_items)}),200

#creating FoodItems
# @jwt_required()
@food_items.route('/create', methods= ['POST'])
def new_food_item():

    data = request.get_json()
    name = data['name']
    price = data['price']
    price_unit = data['price_unit']
    image = data['image']
    stock = data['stock']
    category_id = data['category_id']
    created_by = data['created_by']
    
    # created_by =  get_jwt_identity()
      
  
    #validations
    if not name:
         return jsonify({'error':"FoodItem name is required"})
    

    if FoodItem.query.filter_by(name=name).first() is not None:
        return jsonify({'error': "FoodItem name exists"}), 409 

    new_food_item = FoodItem(name=name,
                             price=price,
                             price_unit=price_unit,
                             image=image,
                             stock=stock,
                             category_id=category_id,
                             created_by=created_by
                             ) 
      
    #inserting values
    db.session.add(new_food_item)
    db.session.commit()
    return jsonify({'message':'New food FoodItem created sucessfully','data': [new_food_item.name,new_food_item.price]}),201
          

#get,edit and delete food item by id
@food_items.route('/food_item/<int:id>', methods=['POST','GET', 'PUT', 'DELETE'])
def handle_food_item(id):
    food_item = FoodItem.query.get_or_404(id)

    if request.method == 'GET':
        response = {
            "id":food_item.id,
            "name": food_item.name,
            "created_by":food_item.created_by,
            "created_at": food_item.created_at
          
        }
        return {"success": True, "item": response,"message":"Food item details retrieved"}

    elif request.method == 'PUT':
        data = request.get_json()

        if not data['name']:
            return jsonify({"message":"Food item name is required"})
    
        
        FoodItem.name = data['name']
        FoodItem.updated_at = datetime.utcnow()
        db.session.add(food_item)
        db.session.commit()
        return {"message": f"{food_item.name}  Food item updated successfully"}

    elif request.method == 'DELETE':
        db.session.delete(food_item)
        db.session.commit()
        return {"message": f"{food_item.name} Food item successfully deleted."}   
  
        
  
   



        
  



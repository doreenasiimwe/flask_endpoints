from flask import jsonify,request,Blueprint
from backend.orders.model import Order
from backend.db import db


# creating a blueprint for orders
orders = Blueprint('orders',__name__,url_prefix='/orders')

# endpoint to create an order
@orders.route('/create', methods=['POST'])
def create_new_order():
    quantity=request.json['quantity']
    location = request.json['location']
    user_id = request.json['user_id']
    status = request.json['status']
    food_item_id= request.json['food_item_id']


# validating the created order
    if not quantity:
        return jsonify({'error':"quantity of item required"}),400

    if not location:
        return jsonify({'error':"location required"}),400
    
    if not food_item_id:
        return jsonify({'error':'enter food item'}),400
    
    if not user_id:
        return jsonify({'error':'user id required'}),400
    

# storing an order
    new_order= Order(quantity=quantity,location=location,user_id=user_id,food_item_id=food_item_id,status=status)
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'success':'You have successfully placed your order'})

        



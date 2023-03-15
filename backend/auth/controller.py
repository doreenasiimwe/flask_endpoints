# from flask import Blueprint,request,jsonify
# from flask_jwt_extended import create_access_token
# from backend.users.model import User
# from backend.db import db
# from werkzeug.security import check_password_hash,generate_password_hash

# auth = Blueprint('auth',__name__,url_prefix='/auth')


# #user registration
# @auth.route('/register',methods=['GET','POST'])
# def create_user():
#     data = request.get_json()
    
#     if request.method == "POST":
          
#       name = data['name']
#       email = data['email']
#       contact = data['contact']
#       user_type = data['user_type']
#       password = data['password']


  
#       #validations
#       if not contact:
#               return jsonify({'error':"Please enter all fields"})
      
#       if not name:
#               return jsonify({'error':"First name is required"})
      

#       if len(password) < 6:
#             return jsonify({'error': "Password is too short"}), 400



#       if User.query.filter_by(email=email).first() is not None:
#         return jsonify({'error': "Email is already in use"}), 409 

    
#       if User.query.filter_by(contact=contact).first() is not None:
#         return jsonify({'error': "Phone number is already in use"}),409
       

#       #creating a hashed password in the database
#       hashed_password = generate_password_hash(password,method="sha256")
#       new_user = User(name=name,email=email,contact=contact,user_type=user_type,password=hashed_password,created_at=datetime.now()) 
      
#       #inserting values
#       db.session.add(new_user)
#       db.session.commit()
#       return jsonify({'message':'New user created sucessfully','data':new_user}),200
          
   
#     elif request.method == "GET":
#         users= User.query.all()
#         return jsonify({
#             "success":True,
#             "data":users,
#             "total":len(users)
#         })
        



# #user login
# @auth.route("/login", methods=["POST"])
# def login():
#     email = request.json.get("email", None)
#     password = request.json.get("password", None)
#     if email!= "test" or password != "test":
#         return jsonify({"msg": "Bad email or password"}), 401

#     access_token = create_access_token(identity=email)
#     return jsonify(access_token=access_token)
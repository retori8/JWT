"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200 

@api.route('/register', methods=['POST'])#REGISTRO
def register_user():
    data = request.get_json()

    user = User()
    user.email = data["email"]
    user.password = generate_password_hash(data["password"])

    if not user.email:
        return jsonify({ "msg": "Necesitamos tu email"}), 422

    if not user.password:
        return jsonify({ "msg": "Necesitamos que ingreses una contraseña"}), 422

    user_filter = User.query.filter_by(email=user.email).first()

    if user_filter:
        return jsonify({ "msg": "El usuario ya existe"}), 400

    user.new_user()

    return jsonify({"msg":"register created", "user": user.serialize()}), 201


@api.route("/login", methods=["POST"])#INICIO DE SECION
def login_user():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    
    user = User.filter.query(email=email, password=password).first()
    if user is None:
        return jsonify({"msg": "Email/Contraseña son incorrectos"}), 401
    
    access_token = create_access_token(identity=user.id)
    return jsonify({ "token": access_token, "user_id": user.id }), 200    


@app.route("/protected", methods=["GET"])#VALIDACION
@jwt_required()
def protected():
    # Accede a la identidad del usuario actual con get_jwt_identity
    current_user_id = get_jwt_identity()
    user = User.filter.get(current_user_id)
    
    return jsonify({"id": user.id, "username": user.username }), 200    

#LOGOUT    
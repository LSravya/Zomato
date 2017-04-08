from flask import Blueprint, request, session, jsonify
from app import db, requires_auth
from .model1 import Restaurant

mod_restaurant = Blueprint('restaurant', __name__, url_prefix = '/api')

@mod_restaurant.route('/restaurant', methods = ['POST'])
@requires_auth
def create_restaurant():
    name = request.form['name']
    city = request.form['city']
    category = request.form['category']
    user_id = session['user_id']
    restaurant = Restaurant(name, city, category, user_id)
    db.session.add(restaurant)
    db.session.commit()
    return jsonify(success = True, restaurant = restaurant.to_dict())

@mod_restaurant.route('/restaurant', methods = ['GET'])
@requires_auth
def get_all_restaurants():
    user_id = session['user_id']
    restaurants = Restaurant.query.filter(Restaurant.user_id == user_id).all()
    return jsonify(success = True, restaurants = [restaurant.to_dict() for restaurant in restaurants])

@mod_restaurant.route('/restaurant/<city>', methods = ['GET'])
@requires_auth
def get_city_restaurants(city):
    user_id = session['user_id']
    restaurants = Restaurant.query.filter(Restaurant.city == city).all()
    return jsonify(success = True, restaurants = [restaurant.to_dict() for restaurant in restaurants])

@mod_restaurant.route('/restaurant/<id>', methods = ['GET'])
@requires_auth
def get_restaurant(id):
    user_id = session['user_id']
    restaurant = Restaurant.query.filter(Restaurant.id == id, Restaurant.user_id == user_id).first()
    if restaurant is None:
        return jsonify(success = False), 404
    else:
        return jsonify(success = True, restaurant = restaurant.to_dict())

@mod_restaurant.route('/restaurant/<id>', methods = ['POST'])
@requires_auth
def edit_restaurant(id):
    user_id = session['user_id']
    restaurant = Restaurant.query.filter(Restaurant.id == id, Restaurant.user_id == user_id).first()
    if restaurant is None:
        return jsonify(success = False), 404
    else:
        restaurant.name = request.form['name']
        restaurant.city = request.form['city']
        restaurant.category = request.form['category']
        db.session.commit()
        return jsonify(success = True)

@mod_restaurant.route('/restaurant/<id>/delete', methods = ['POST'])
@requires_auth
def delete_restaurant(id):
    user_id = session['user_id']
    restaurant = Restaurant.query.filter(Restaurant.id == id, Restaurant.user_id == user_id).first()
    if restaurant is None:
        return jsonify(success = False), 404
    else:
        db.session.delete(restaurant)
        db.session.commit()
        return jsonify(success = True)

from server import server, db
from flask import jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import json


from server.models import *
from server.helpers.create_helper import *

import time

from validate_email import validate_email

from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

@server.route('/rest/')
@server.route('/rest/index')
def index():
    return "Flask server is running!"

@server.route('/rest/tryouts')
def tryouts():
    u = User(username='Carlos', email='carlos@example.com')
    print u
    return 'Ok'

@server.route('/rest/token_refresh', methods=['GET'])
@jwt_refresh_token_required
def token_refresh():
    user = get_jwt_identity()
    access_token = create_access_token(identity=user)
    return jsonify({'access_token': access_token})

@server.route('/rest/secret', methods=['GET'])
@jwt_required
def secret():
    return jsonify({'message': 'SHHHHH is a secret'})

@server.route('/rest/user_registration', methods=['POST'])
def user_registration():
    if not request.json:
        abort(400)
    data = json.loads(request.data)
    # Validate input from user
    if 'username' not in data: 
        return jsonify({'message': 'username is required'})
    if 'email' not in data:
        return jsonify({'message': 'email is required'})   
    if not validate_email(str(data['email'])):
        return jsonify({'message': 'wrong email format'})
    # Check if exists
    if User.find_by_username(data['username']):
        return jsonify({'message': 'User {} already exists'.format(data['username'])})   
    # Create the user
    new_user = User(
        username=data['username'],
        email=data['email']
    )
    new_user.set_password(data['password'])
    try:
        new_user.save_to_db()
        access_token = create_access_token(identity=data['username'])
        refresh_token = create_refresh_token(identity=data['username'])
        return jsonify({'message': 'User {} was created'.format(data['username']), 'access_token': access_token, 'refresh_token': refresh_token})
    except:
        return jsonify({'message': 'Something went wrong'}, 500)
    
@server.route('/rest/shopping_list/api/user_login', methods=['POST'])
def user_login():
    print request.data
    if not request.data:
        abort(400)
    data = json.loads(request.data)
    if not 'username' in data: 
        return jsonify({'message': 'username is required'})
    if not 'password' in data:
        return jsonify({'message': 'password is required'})
    current_user = User.find_by_username(data['username'])
    if not current_user:
        return jsonify({'message': 'User {} doesn\'t exists'.format(data['username'])})
    if current_user.check_password(data['password']):
        access_token = create_access_token(identity=data['username'])
        refresh_token = create_refresh_token(identity=data['username'])
        return jsonify({'message': 'Correct login for User {}'.format(data['username']), 'access_token': access_token, 'refresh_token': refresh_token})
    else:
        return jsonify({'message': 'Wrong password'})


@server.route('/rest/shopping_list/api/items', methods=['POST'])
def create_items():
    data = json.loads(request.json)
    if not request.json:
        abort(400)
    # Check Company
    db_company = Company.query.filter_by(name=data['company']).first()
    if not db_company:
        db_company = create_company(data['company'])
    else:
        db_company = db_company.id
    # Check Area
    db_area = Area.query.filter_by(name=data['area']).first()
    if not db_area:
        db_area = create_area(data['area'])
    else:
        db_area = db_area.id
    # Check Supermarket
    db_supermarket = Supermarket.query.filter_by(name=data['supermarket']).first()
    if not db_supermarket:
        db_supermarket = create_supermarket(data['supermarket'], db_company, db_area, data['lat'], data['lon'])
    else:
        db_supermarket = db_supermarket.id
    for item in data.get('articles'):
        item_category = Category.query.filter_by(name=item['category']).first()
        if not item_category:
            # create category
            db_category = create_category(item['category'])
        else:
            db_category = item_category.id
        item_sub_category = SubCategory.query.filter_by(name=item['specific_category']).first()
        if not item_sub_category:
            # create SubCategory
            db_sub_category = create_sub_category(item['specific_category'], db_category)
        else:
            db_sub_category = item_sub_category.id
        price = string_to_currency(item['price'])
        stored_article = Article.query.filter_by(name=item['name'], format=item['format']).first()
        if stored_article:
            print "need to check the price"
        else:
            article = Article(name=item['name'], price=price, format=item['format'], url=item['url'], supermarket_id=db_supermarket, category_id=db_category, sub_category_id=db_sub_category, image=item['image'])
            db.session.add(article)
            db.session.commit()
    return 'Ok'

@server.route('/rest/shopping_list/api/articles', methods=['GET'])
def get_articles():
    db_articles = Article.query.all()
    articles = []
    for article in db_articles:
        articles.append({
            'id': article.id,
            'name': article.name,
            'price': article.price,
            'format': article.format,
            'category_id': article.category_id,
            'sub_category_id': article.sub_category_id,
            'supermarket_id': article.supermarket_id,
            'image': article.image,
            'url': article.url,
        })
    return jsonify(sorted(articles, key=lambda k: k['id']))

@server.route('/rest/shopping_list/api/categories', methods=['GET'])
def get_categories():
    db_categories = Category.query.all()
    categories = []
    for category in db_categories:
        categories.append({
            'id': category.id,
            'name': category.name,
        })
    return jsonify(sorted(categories, key=lambda k: k['name']))

@server.route('/rest/shopping_list/api/subcategories', methods=['POST'])
def get_subcategories():
    if not request.json:
        abort(400)
    db_subcategories = SubCategory.query.filter_by(category_id=request.json['search']).all()
    sub_categories = []
    for sub_category in db_subcategories:
        sub_categories.append({
            'id': sub_category.id,
            'name': sub_category.name,         
        })
    return jsonify(sorted(sub_categories, key=lambda k: k['name']))
    

@server.route('/rest/shopping_list/api/filtered_articles', methods=['POST'])
def get_filtered_articles():
    if not request.json:
        abort(400)
    search = {}
    for element in request.json['search']:
        search[element] = request.json['search'].get(element)
    db_articles = Article.query.filter_by(**search).all()
    articles = []
    for article in db_articles:
        articles.append({
            'id': article.id,
            'name': article.name,
            'price': article.price,
            'format': article.format,
            'category_id': article.category_id,
            'sub_category_id': article.sub_category_id,
            'supermarket_id': article.supermarket_id,
            'image': article.image,
            'url': article.url,            
        })
    return jsonify(sorted(articles, key=lambda k: k['id']))


@server.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found!'}), 404)


@server.errorhandler(400)
def bad_request(error):
	return make_response(jsonify({'error': 'There is no name in the request'}), 400)

from server import server, db
from flask import jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import json


from server.models import *
from server.helpers.create_helper import *



@server.route('/')
@server.route('/index')
def index():
    return "Hello, World!"


@server.route('/shopping_list/api/items', methods=['POST'])
def create_items():
    dict_request = json.loads(request.json)
    if not request.json:
        abort(400)
    # Check Company
    db_company = Company.query.filter_by(name=dict_request['company']).first()
    if not db_company:
        db_company = create_company(dict_request['company'])
    else:
        db_company = db_company.id
    # Check Area
    db_area = Area.query.filter_by(name=dict_request['area']).first()
    if not db_area:
        db_area = create_area(dict_request['area'])
    else:
        db_area = db_area.id
    # Check Supermarket
    db_supermarket = Supermarket.query.filter_by(name=dict_request['supermarket']).first()
    if not db_supermarket:
        db_supermarket = create_supermarket(dict_request['supermarket'], db_company, db_area, dict_request['lat'], dict_request['lon'])
    else:
        db_supermarket = db_supermarket.id
    for item in dict_request.get('articles'):
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
        # Check wheter the article is already stored to update it
        stored_article = Article.query.filter_by(name=item['name'], format=item['format'], supermarket_id=db_supermarket, category_id=db_category, sub_category_id=db_sub_category).first()
        if stored_article:
            print "need to check the price"
        else:
            article = Article(name=item['name'], price=price, format=item['format'], supermarket_id=db_supermarket, category_id=db_category, sub_category_id=db_sub_category)
            db.session.add(article)
            db.session.commit()
    return 'Ok'

@server.route('/shopping_list/api/articles', methods=['GET'])
def get_articles():
    # db_articles = Article.query.all()
    db_articles = Article.query.paginate(1, server.config['ARTICLES_PER_PAGE'], False).items
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
        })
    return jsonify(sorted(articles, key=lambda k: k['id']))

@server.route('/shopping_list/api/categories', methods=['GET'])
def get_categories():
    db_categories = Category.query.all()
    categories = []
    for category in db_categories:
        categories.append({
            'id': category.id,
            'name': category.name,
        })
    return jsonify(sorted(categories, key=lambda k: k['name']))

@server.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)


@server.errorhandler(400)
def bad_request(error):
	return make_response(jsonify({'error': 'There is no name in the request'}), 400)

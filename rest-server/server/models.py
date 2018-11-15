from server import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash



class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    supermarkets = db.relationship('Supermarket', backref='company', lazy=True)

    def __repr__(self):
        return '<Company {}>'.format(self.name)

class Area(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    supermarkets = db.relationship('Supermarket', backref='area', lazy=True)

    def __repr__(self):
        return '<Area {}>'.format(self.name)

class Supermarket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    company_id = db.Column(db.Integer, ForeignKey("company.id"), nullable=False)
    area_id = db.Column(db.Integer, ForeignKey("area.id"), nullable=False)
    lat_location = db.Column(db.Float)
    lon_location = db.Column(db.Float)
    articles = db.relationship('Article', backref='supermarket', lazy=True)

    def __repr__(self):
        return '<Supermarket {}>'.format(self.name)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    subcategories = db.relationship('SubCategory', backref='category', lazy=True)
    articles = db.relationship('Article', backref='category', lazy=True)

    def __repr__(self):
        return '<Category {}>'.format(self.name)

class SubCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    category_id = db.Column(db.Integer, ForeignKey("category.id"), nullable=False)
    articles = db.relationship('Article', backref='subcategory', lazy=True)

    def __repr__(self):
        return '<SubCategory {}>'.format(self.name)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    price = db.Column(db.Float)
    format = db.Column(db.String(64))
    image = db.Column(db.String(128))
    url = db.Column(db.String(128))
    supermarket_id = db.Column(db.Integer, ForeignKey("supermarket.id"), nullable=False)
    category_id = db.Column(db.Integer, ForeignKey("category.id"), nullable=False)
    sub_category_id = db.Column(db.Integer, ForeignKey("sub_category.id"), nullable=False)

    def __repr__(self):
        return '<Article {}>'.format(self.name)

class User(db.Model):
    # __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    def __repr__(self):
        return '<User {}>'.format(self.username) 
    
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class ShoppingListHeader(db.Model):
    __tablename__ = 'shopping_list_header'
    id = db.Column(db.Integer, primary_key=True)       
    user_id = db.Column(db.Integer, ForeignKey("user.id"), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now())
    name = db.Column(db.String(128))

    def __repr__(self):
        return '<List {}, {}>'.format(self.user_id, self.date) 

class ShoppingListLine(db.Model):
    __tablename__ = 'shopping_list_line'
    __table_args_ = (
        db.PrimaryKeyConstraint('shopping_list_header.id', 'article.id'),
    )
    header_id = db.Column(db.Integer, ForeignKey('shopping_list_header.id'), primary_key=True) 
    article_id = db.Column(db.Integer, ForeignKey('article.id'), primary_key=True) 
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<List {}, {}, {}, {}>'.format(self.header_id, self.article_id, self.quantity, self.price) 


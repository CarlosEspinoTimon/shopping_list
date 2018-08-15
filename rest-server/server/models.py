from server import db
from sqlalchemy import ForeignKey


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
    name = db.Column(db.String(128), index=True, unique=True)
    price = db.Column(db.Float)
    format = db.Column(db.String(64))
    supermarket_id = db.Column(db.Integer, ForeignKey("supermarket.id"), nullable=False)
    category_id = db.Column(db.Integer, ForeignKey("category.id"), nullable=False)
    sub_category_id = db.Column(db.Integer, ForeignKey("sub_category.id"), nullable=False)

    def __repr__(self):
        return '<Article {}>'.format(self.name)

from server.models import *


# HELPER
def create_company(company):
    company = Company(name=company)
    db.session.add(company)
    db.session.commit()
    return company.id

def create_area(area):
    area = Area(name=area)
    db.session.add(area)
    db.session.commit()
    return area.id

def create_supermarket(name, company, area, lat, lon):
    supermarket = Supermarket(name=name, company_id=company, area_id=area, lat_location=lat, lon_location=lon)
    db.session.add(supermarket)
    db.session.commit()
    return supermarket.id

def create_category(category):
    category = Category(name=category)
    db.session.add(category)
    db.session.commit()
    return category.id

def create_sub_category(sub_category, category):
    sub_category = SubCategory(name=sub_category, category_id=category)
    db.session.add(sub_category)
    db.session.commit()
    return sub_category.id

def string_to_currency(price):
    try:
        result = float(price.replace(',','.'))
    except Exception as e:
        print "Error while converting price --> ", price
        result = 0.0
    return result

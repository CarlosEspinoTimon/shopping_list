#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

import re
import json
import requests

import csv

url = 'https://carrefour.es'

req = requests.get(url + '/supermercado/')

html_soup = BeautifulSoup(req.text, 'html.parser')



# Obtaining all the sections links
sections_links = []
sections = html_soup.find('div', {'id': 'our-sections'})
for section in sections.find_all('div', {'class': 'item'}):
    section_name = section.find('h3', {'class': 'title-05'}).text
    section_url = section.find('a', href=True)['href']
    sections_links.append({'name': section_name, 'url': section_url})

# Obtaining all the categories links
categories_links = []
for section in sections_links:
    section_request = requests.get(url + section['url'])
    section_soup = BeautifulSoup(section_request.text, 'html.parser')
    for category in section_soup.find_all('div', {'id': 'categories'}):
        category_name = category.find('a', href=True).text
        category_url = category.find('a', href=True)['href']
        categories_links.append({'section': section['name'], 'name': category_name, 'url': category_url})

# These categories has more categories:
specific_categories_links = []
for category in categories_links:
    category_request = requests.get(url + category['url'])
    category_soup = BeautifulSoup(category_request.text, 'html.parser')
    for category2 in category_soup.find_all('div', {'id': 'categories'}):
        for element in category2.find_all('li'):
            specific_category_name = element.find('a', href=True).text
            specific_category_link = element.find('a', href=True)['href']
            specific_categories_links.append({'section': category['section'], 'category': category['name'], 'name': specific_category_name, 'url': specific_category_link})

# Getting the links of all the items
items_links = []
for specific_category in specific_categories_links:
    specific_category_request = requests.get(url + specific_category['url'])
    specific_category_soup = BeautifulSoup(specific_category_request.text, 'html.parser')
    for item in specific_category_soup.find_all('h2', {'class': 'name-product'}):
        item_name = item.find('a', {'class': 'js-gap-product-click'}).text
        item_link = item.find('a', href=True)['href']
        items_links.append({'section': specific_category['section'], 'category': specific_category['category'], 'specific_category': specific_category['name'], 'name': item_name, 'url': item_link})



# Getting the info from each article
articles = []
errors = []
for article in items_links:
    try:
        article_request = requests.get(url + article['url'])
        article_soup = BeautifulSoup(article_request.text, 'html.parser')
    
        articles.append({
            'section': article['section'].encode('utf-8'),
            'category': article['category'].encode('utf-8'),
            'specific_category': article['specific_category'].encode('utf-8'),
            'item': article['name'].encode('utf-8'),
            'name': article_soup.find('h1', {'id': 'product-01'}).text.encode('utf-8'),
            'format': article_soup.find('p', {'class': 'name-formato'}).text.encode('utf-8'),
            'price': article_soup.find('span', {'class': 'js-price'}).text.encode('utf-8'),
            'image': article_soup.find('div', {'class': 'col-image'}).find('a', recursive=True)['href'],
            'url': article_request,
        })
    except Exception as e:
        errors.append({
            'error': e,
            'article': article_request
        })

print articles

# Prepare the data to be send to the server
# In this case I am forcing this data with all the extra info.
data = {
    'company': 'Carrefour',
    'area': 'Canarias',
    'supermarket': 'Carrefour Añaza',
    'lat': '256456',
    'lon': '256456',
    'articles': articles,
    'errors': errors,
}
headers = {'Content-type': 'application/json'}

# Send the data
r = requests.post('http://localhost:5000/rest/shopping_list/api/items', json=json.dumps(data, ensure_ascii=False), headers=headers)


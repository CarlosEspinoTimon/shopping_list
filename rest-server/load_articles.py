import requests
import json

data = {
    'company': 'Carrefour',
    'area': 'Canarias',
    'supermarket': 'Carrefour Anaza',
    'lat': '256456',
    'lon': '256456',
    'articles': [
      # {
      #   'category': 'Frutas',
      #   'name': 'Cerezas bio',
      #   'format': ' Bandeja de 500 g',
      #   'specific_category': 'Fruta de hueso',
      #   'section': 'El Mercado',
      #   'item': '\nCerezas bio',
      #   'price': '3,49'
      # },
      # {
      #   'category': 'Frutas',
      #   'name': 'Cerezas',
      #   'format': ' Tarrina de 1 kg. ',
      #   'specific_category': 'Fruta de hueso',
      #   'section': 'El Mercado',
      #   'item': '\nCerezas',
      #   'price': '4,50'
      # },
      # {
      #   'category': 'Frutas',
      #   'name': 'Paraguayo',
      #   'format': ' Bolsa de 1000.0 g. aprox',
      #   'specific_category': 'Fruta de hueso',
      #   'section': 'El Mercado',
      #   'item': '\nParaguayo',
      #   'price': '1,35'
      # },
      # {
      #   "category": "Frutas",
      #   "name": "Manzana golden",
      #   "format": " Bandeja de  1500.0 g. aprox",
      #   "specific_category": "Manzanas y Peras",
      #   "section": "El Mercado",
      #   "item": "\nManzana golden",
      #   "price": "2,23"
      # },
      # {
      #   "category": "Frutas",
      #   "name": "Naranja para zumo",
      #   "format": " Malla de 4 kg.",
      #   "specific_category": "Naranjas y otros c\u00edtricos",
      #   "section": "El Mercado",
      #   "item": "\nNaranja para zumo",
      #   "price": "3,96"
      # },
      # {
      #   "category": "Frutas",
      #   "name": "Pi\u00f1a ",
      #   "format": " Pieza de  1500.0 g. aprox",
      #   "specific_category": "Pi\u00f1as y Tropicales",
      #   "section": "El Mercado",
      #   "item": "\nPi\u00f1a ",
      #   "price": "1,48"
      # },
      # {
      #   "category": "Frutas",
      #   "name": "Mel\u00f3n Galia ",
      #   "format": " Pieza de 1000.0 g. aprox",
      #   "specific_category": "Sand\u00edas y Melones ",
      #   "section": "El Mercado",
      #   "item": "\nMel\u00f3n Galia ",
      #   "price": "2,35"
      # },
      # {
      #   "category": "Alimentaci\u00f3n",
      #   "name": "Tomate frito",
      #   "format": " 3x350 g.",
      #   "specific_category": "Salsas y Tomate Frito",
      #   "section": "La Despensa",
      #   "item": "\nTomate frito",
      #   "price": "1,91"
      # },
      # {
      #   "category": "Alimentaci\u00f3n",
      #   "name": "Quinoa",
      #   "format": " 400 g.",
      #   "specific_category": "Semillas",
      #   "section": "La Despensa",
      #   "item": "\nQuinoa",
      #   "price": "2,23"
      # },
      # {
      #   "category": "Alcoholes",
      #   "name": "Brandy solera Reserva",
      #   "format": " 1 l.",
      #   "specific_category": "Brandy y Co\u00f1ac",
      #   "section": "Bebidas",
      #   "item": "\nBrandy solera Reserva",
      #   "price": "8,00"
      # },
      # {
      #   "category": "Alcoholes",
      #   "name": "Bebida espirituosa",
      #   "format": " 1 l.",
      #   "specific_category": "Brandy y Co\u00f1ac",
      #   "section": "Bebidas",
      #   "item": "\nBebida espirituosa",
      #   "price": "8,10"
      # },
      # {
      #   "category": "Alcoholes",
      #   "name": "Brandy de Jerez solera Reserva",
      #   "format": " 70 cl.",
      #   "specific_category": "Brandy y Co\u00f1ac",
      #   "section": "Bebidas",
      #   "item": "\nBrandy de Jerez solera Reserva",
      #   "price": "10,65"
      # },
      # {
      #   "category": "Alimentaci\u00f3n",
      #   "name": "Papilla instant\u00e1nea multicereales",
      #   "format": " 1200 g.",
      #   "specific_category": "Papillas y Galletas",
      #   "section": "Beb\u00e9",
      #   "item": "\nPapilla instant\u00e1nea multicereales",
      #   "price": "5,80"
      # },
      # {
      #   "category": "Alimentaci\u00f3n",
      #   "name": "Couscous mediano",
      #   "format": " 500 g.",
      #   "specific_category": "Arroz y Cous Cous",
      #   "section": "La Despensa",
      #   "item": "\nCouscous mediano",
      #   "price": "1,34"
      # },
      # {
      #   "category": "Alimentaci\u00f3n",
      #   "name": "Arroz vaporizado",
      #   "format": " 1 kg.",
      #   "specific_category": "Arroz y Cous Cous",
      #   "section": "La Despensa",
      #   "item": "\nArroz vaporizado",
      #   "price": "1,59"
      # },
      # {
      #   "category": "Alimentaci\u00f3n",
      #   "name": "Galletitas 6 cereales",
      #   "format": " 125 g.",
      #   "specific_category": "Papillas y Galletas",
      #   "section": "Beb\u00e9",
      #   "item": "\nGalletitas 6 cereales",
      #   "price": "1,64"
      # },
      # {
      #   "category": "Alimentaci\u00f3n",
      #   "name": "Bolsita de pera, pl\u00e1tano y naranja 100% Eco",
      #   "format": " 100 g.",
      #   "specific_category": "Postres, Zumos, Petit y Yogures Infantiles",
      #   "section": "Beb\u00e9",
      #   "item": "\nBolsita de pera, pl\u00e1tano y naranja 100% Eco",
      #   "price": "1,00"
      # },
      # {
      #   "category": "Ba\u00f1o e Higiene Corporal",
      #   "name": "Jab\u00f3n de manos perfume manzana",
      #   "format": " 500 ml.",
      #   "specific_category": "Jab\u00f3n de Manos",
      #   "section": "Perfumer\u00eda e Higiene",
      #   "item": "\nJab\u00f3n de manos perfume manzana",
      #   "price": "1,25"
      # },
      # {
      #   "category": "Ba\u00f1o e Higiene Corporal",
      #   "name": "Bastoncillos de algod\u00f3n",
      #   "format": " 200 ud.",
      #   "specific_category": "Ojos y Oreja",
      #   "section": "Perfumer\u00eda e Higiene",
      #   "item": "\nBastoncillos de algod\u00f3n",
      #   "price": "0,50"
      # },
      # {
      #   "category": "Ba\u00f1o e Higiene Corporal",
      #   "name": "Bastoncillos",
      #   "format": " 160 ud.",
      #   "specific_category": "Ojos y Oreja",
      #   "section": "Perfumer\u00eda e Higiene",
      #   "item": "\nBastoncillos",
      #   "price": "0,44"
      # },
      # {
      #   "category": "Ba\u00f1o e Higiene Corporal",
      #   "name": "Sal de ba\u00f1o ultra hidratante arg\u00e1n",
      #   "format": " 700 g.",
      #   "specific_category": "Sales de Ba\u00f1o",
      #   "section": "Perfumer\u00eda e Higiene",
      #   "item": "\nSal de ba\u00f1o ultra hidratante arg\u00e1n",
      #   "price": "3,29"
      # },
      # {
      #   "category": "Ba\u00f1o e Higiene Corporal",
      #   "name": "Bombas de sal Rosas",
      #   "format": " 250 ml.",
      #   "specific_category": "Sales de Ba\u00f1o",
      #   "section": "Perfumer\u00eda e Higiene",
      #   "item": "\nBombas de sal Rosas",
      #   "price": "2,10"
      # },
      # {
      #   "category": "Cuidado corporal",
      #   "name": "Gel de ba\u00f1o de aceite de arg\u00e1n Essentials Hipoalerg\u00e9nico",
      #   "format": " 750 ml.",
      #   "specific_category": "Jabones y Geles",
      #   "section": "Parafarmacia",
      #   "item": "\nGel de ba\u00f1o de aceite de arg\u00e1n Essentials Hipoalerg\u00e9nico",
      #   "price": "2,95"
      # },
      # {
      #   "category": "Cuidado corporal",
      #   "name": "Gel de ba\u00f1o de aloe vera Essentials Hipoalerg\u00e9nico",
      #   "format": " 750 ml.",
      #   "specific_category": "Jabones y Geles",
      #   "section": "Parafarmacia",
      #   "item": "\nGel de ba\u00f1o de aloe vera Essentials Hipoalerg\u00e9nico",
      #   "price": "3,25"
      # },
      # {
      #   "category": "Perros",
      #   "name": "Correa de cadena met\u00e1lica estampada 1,00m/3mm T M/L",
      #   "format": " 1 Ud.",
      #   "specific_category": "Collares y Correas",
      #   "section": "Mascotas",
      #   "item": "\nCorrea de cadena met\u00e1lica estampada 1,00m/3mm T M/L",
      #   "price": "8,79"
      # },
      # {
      #   "category": "Perros",
      #   "name": "Correa bandera talla XL",
      #   "format": " 1 Ud.",
      #   "specific_category": "Collares y Correas",
      #   "section": "Mascotas",
      #   "item": "\nCorrea bandera talla XL",
      #   "price": "12,50"
      # },
      # {
      #   "category": "Alimentaci\u00f3n",
      #   "name": "Infusi\u00f3n instant\u00e1nea para aliviar gases Digest",
      #   "format": " 200 g.",
      #   "specific_category": "Complementos Alimenticios",
      #   "section": "Beb\u00e9",
      #   "item": "\nInfusi\u00f3n instant\u00e1nea para aliviar gases Digest",
      #   "price": "6,75"
      # },
      # {
      #   "category": "Alimentaci\u00f3n",
      #   "name": "Infusi\u00f3n de manzanilla e hinojo",
      #   "format": " 150 g.",
      #   "specific_category": "Complementos Alimenticios",
      #   "section": "Beb\u00e9",
      #   "item": "\nInfusi\u00f3n de manzanilla e hinojo",
      #   "price": "8,50"
      # }
      {'category': 'Frutas', 'item': '\nParaguayo', 'name': 'Paraguayo', 'image': u'https://static.carrefour.es/hd_1600x_/supermercado/bcc_static/catalogImages/product/198068/198068.png', 'format': ' Bolsa de 1000.0 g. aprox', 'section': 'El Mercado', 'price': '1,19', 'specific_category': 'Fruta de temporada', 'url': 'www.carrefour.es'}, 
      {'category': 'Frutas', 'item': '\nNectarina amarilla', 'name': 'Nectarina amarilla', 'image': u'https://static.carrefour.es/hd_1600x_/supermercado/bcc_static/catalogImages/product/196148/196148.png', 'format': ' Granel 1000.0 g. aprox', 'section': 'El Mercado', 'price': '1,19', 'specific_category': 'Fruta de temporada', 'url': 'www.carrefour.es'}, 
      {'category': 'Frutas', 'item': '\nMelocoton rojo', 'name': 'Melocoton rojo', 'image': u'https://static.carrefour.es/hd_1600x_/supermercado/bcc_static/catalogImages/product/196069/196069.png', 'format': ' Granel 1000.0 g. aprox', 'section': 'El Mercado', 'price': '1,59', 'specific_category': 'Fruta de temporada', 'url': 'www.carrefour.es'}, 
      {'category': 'Frutas', 'item': '\nMelocot\xc3\xb3n amarillo', 'name': 'Melocot\xc3\xb3n amarillo', 'image': u'https://static.carrefour.es/hd_1600x_/supermercado/bcc_static/catalogImages/product/332643/332643.jpg', 'format': ' Tarrina de 1 kg.', 'section': 'El Mercado', 'price': '1,39', 'specific_category': 'Fruta de temporada', 'url': 'www.carrefour.es'}, 
      {'category': 'Frutas', 'item': '\nAlbaricoque Granel', 'name': 'Albaricoque Granel', 'image': u'https://static.carrefour.es/hd_1600x_/supermercado/bcc_static/catalogImages/product/035980/035980.png', 'format': ' Bolsa de 1000.0 g. aprox', 'section': 'El Mercado', 'price': '1,89', 'specific_category': 'Fruta de temporada', 'url': 'www.carrefour.es'}, 
      ]
}
headers = {'Content-type': 'application/json'}
r = requests.post('http://localhost:5000/shopping_list/api/items', json=json.dumps(data), headers=headers)

print (r.status_code, r.reason)

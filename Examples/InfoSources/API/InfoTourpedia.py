"""
.. module:: AgentTourpedia

AgentTourpedia
*************

:Description: AgentTourpedia

    Tourpedia, puntos de interes en diferentes ciudades

    Acceso mediante API REST, documentacion en http://tour-pedia.org/api/index.html

    Entries de la API interesantes: getPlaces, getPlaceDetails, getPlacesByArea,

    Acceso mediante SPARQL (cuando funciona), punto de acceso http://tour-pedia.org/sparql,
    ontologias usadas http://tour-pedia.org/about/lod.html

:Authors: bejar
    

:Version: 

:Created on: 27/01/2017 9:34 

"""

import requests

__author__ = 'bejar'

TOURPEDIA_END_POINT = 'http://tour-pedia.org/api/'

# Obtenemos un atracciones en Bercelona que tengan Museu en el nombre
r = requests.get(TOURPEDIA_END_POINT+ 'getPlaces',
                 params={'location': 'Barcelona', 'category': 'attraction', 'name': 'Museu'})


dic = r.json()
print(len(dic))

# Cada lugar tiene una serie de atributos, entre ellos la llamada a la API que da los detalles del lugar, que
# a su vez tiene otro conjunto de atributos
for d in dic:
    if 'subCategory' in d:
        print(d['subCategory'])

        r = requests.get(d['details']) # usamos la llamada a la API ya codificada en el atributo
        dic2 = r.json()
        if 'description' in dic2:
            print(dic2['description'])
        if 'name' in dic2:
            print(dic2['name'])
        if 'address' in dic2:
            print(dic2['address'])
        if 'lat' in dic2:
            print(dic2['lat'], dic2['lng'])




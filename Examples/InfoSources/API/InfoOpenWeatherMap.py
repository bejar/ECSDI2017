# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 15:58:13 2013

Demo de consulta del servicio del tiempo de openweathermap.org

Para hacer consultas hay que registrarse y obtener una clave de desarrollador

@author: javier
"""

__author__ = 'javier'

import requests
from AgentUtil.APIKeys import WEATHERAPPID

# Endpoint que da previsiones del tiempo a 5 dias
WEATHER_END_POINT = 'http://api.openweathermap.org/data/2.5/forecast'

# Hacemos el GET al servicio REST
# Prevision del tiempo en Barcelona para los proximos 5 dias en sistema metrico
r = requests.get(WEATHER_END_POINT,
                 params={'q': 'Barcelona,es', 'units': 'metric',
                         'mode': 'json', 'cnt': '10', 'APPID': WEATHERAPPID
                         })

# Transformamos la respuesta de JSON a un diccionario python
dic = r.json()
print(dic)
# Imprimimos los elementos de la respuesta
for d in dic['list']:
    print(d)
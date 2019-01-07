"""
.. module:: AgentAmadeus

AgentAmadeus
*************

:Description: AgentAmadeus

    API de Amadeus self-service test environment

    Hace falta darse de alta en el portal de desarrolladores (https://developers.amadeus.com) para conseguir
    una KEY para acceder a la API

    El numero de queries en el entorno de test esta limitado mensualmente (pero os deberia sobrar)

    https://developers.amadeus.com/pricing


    Se puede conectar directamente mediante la libreria request llamando a la API REST o usando la libreria
    Python desarrollada por Amadeus

    https://github.com/amadeus4dev/amadeus-python

:Authors: bejar
    

:Version: 

:Created on: 23/01/2017 16:24 

"""

from AgentUtil.APIKeys import AMADEUS_KEY, AMADEUS_SECRET
from amadeus import Client, ResponseError

amadeus = Client(
    client_id=AMADEUS_KEY,
    client_secret=AMADEUS_SECRET
)

try:
    response = amadeus.shopping.flight_destinations.get(origin='MAD')
    print(response.data)
    print('-----------------------------------------------------------')
    response = amadeus.shopping.flight_offers.get(origin='MAD', destination='NYC', departureDate='2019-08-01')
    print(response.data)
    print('-----------------------------------------------------------')
    response = amadeus.shopping.hotel_offers.get(cityCode ='NYC')
    print(response.data)
except ResponseError as error:
    print(error)




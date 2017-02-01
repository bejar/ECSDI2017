"""
.. module:: AgentAmadeus

AgentAmadeus
*************

:Description: AgentAmadeus

    Uso de la API de Amadeus, hoteles, vuelos, tren

    http://sandbox.amadeus.com

    Documentacion de la API REST (usando requests)

    https://sandbox.amadeus.com/api-catalog

    Tambien se puede usar el modulo python amadeus

    http://amadeus.readthedocs.io/en/latest/index.html

:Authors: bejar
    

:Version: 

:Created on: 23/01/2017 16:24 

"""

from AgentUtil.APIKeys import AMADEUS_KEY
from amadeus import Flights


__author__ = 'bejar'


flights = Flights(AMADEUS_KEY)
# resp = flights.inspiration_search(
#     origin='BCN', destination='GVA',
#     departure_date="2017-01-25--2017-02-28")
#

resp = flights.extensive_search(
    origin='MAD',
    destination='BCN',
    departure_date='2017-02-05--2017-02-28',
    duration='4--10')

print resp


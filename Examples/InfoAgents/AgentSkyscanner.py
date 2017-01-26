"""
.. module:: AgentSkyscanner

AgentSkyscanner
*************

:Description: AgentSkyscanner

 Uso de la API de Skyscanner, solo permite acceder a la cache de vuelos (500 resultados por minuto)

 https://skyscanner.readthedocs.io/en/latest/index.html

:Authors: bejar
    

:Version: 

:Created on: 23/01/2017 16:38 

"""

__author__ = 'bejar'


from AgentUtil.APIKeys import SKYSCANNER_KEY


from skyscanner.skyscanner import  FlightsCache


flights_cache_service = FlightsCache(SKYSCANNER_KEY)
result = flights_cache_service.get_cheapest_quotes(
    market='UK',
    currency='EUR',
    locale='es-ES',
    originplace='BCN',
    destinationplace='GVA',
    outbounddate='2017-01',
    inbounddate='2017-02').parsed

print(result)



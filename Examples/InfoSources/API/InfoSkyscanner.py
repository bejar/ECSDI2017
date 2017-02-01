"""
.. module:: AgentSkyscanner

AgentSkyscanner
*************

:Description: AgentSkyscanner

 Uso de la API de Skyscanner, solo permite acceder a la cache de vuelos (500 resultados por minuto)

 Documentacion de la API REST (usando requests)

 https://skyscanner.github.io/slate/?_ga=1.104705984.172843296.1446781555#api-documentation

 Tambien se puede usar el modulo python skyscanner

 https://github.com/Skyscanner/skyscanner-python-sdk
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
    outbounddate='2017-02-02',
    inbounddate='2017-02-07').parsed

print(result)



__author__ = 'javier'
"""
lgdo:Amenity
  lgdo:Bar
  lgdo:Restaurant
  lgdo:Attraction
  lgdo:TourismThing
  lgdo:Cafe
  lgdo:FastFood
  lgdo:Pub
  lgdo:Attraction
  lgdo:PointOfInterest
  lgdo:Hotel

"""

from SPARQLWrapper import SPARQLWrapper, JSON
from AgentUtil.SPARQLPoints import GEODATA


sparql = SPARQLWrapper(GEODATA)

# Restaurantes que estan alrededor de 400m de long 2.16, lat 41.4
sparql.setQuery("""
Prefix lgdr:<http://linkedgeodata.org/triplify/>
Prefix lgdo:<http://linkedgeodata.org/ontology/>
prefix dbpr:<http://dbpedia.org/resource/>

Select * {
     ?s a lgdo:City .
     ?s rdfs:label "Barcelona".
     ?s owl:sameAs <http://dbpedia.org/resource/Barcelona>.

  } Limit 1000
  """)
sparql.setReturnFormat(JSON)
results = sparql.query()
print results.print_results()


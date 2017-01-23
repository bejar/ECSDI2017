"""
.. module:: AgentFlightsStarDog

AgentFlightsStarDog
*************

:Description: AgentFlightsStarDog

    

:Authors: bejar
    

:Version: 

:Created on: 18/02/2015 12:52 

"""

__author__ = 'bejar'

import gzip

from rdflib import Graph

from AgentUtil.OntoNamespaces import TIO
from AgentUtil.SPARQLPoints import FUSEKI
from SPARQLWrapper import SPARQLWrapper, JSON, XML, RDF, N3

sparql = SPARQLWrapper("http://localhost:3030/ds/query")

# Consulta al grafo los aeropuertos dentro de la caja definida por las coordenadas
sparql.setQuery(
    """
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix tio:<http://purl.org/tio/ns#>
    prefix geo:<http://www.w3.org/2003/01/geo/wgs84_pos#>
    prefix dbp:<http://dbpedia.org/ontology/>
    prefix xsd:<http://www.w3.org/2001/XMLSchema#>

    Select ?f
    where {
        ?f rdf:type dbp:Airport .
        ?f geo:lat ?lat .
        ?f geo:long ?lon .
        Filter ( ?lat < "41.7"^^xsd:float &&
                 ?lat > "41.0"^^xsd:float &&
                 ?lon < "2.3"^^xsd:float &&
                 ?lon > "2.0"^^xsd:float)
        }
    LIMIT 30
    """)

# Los SELECT no siempre retornan un grafo RDF valido, por lo que es mas seguro obtener
# la informacion como JSON
sparql.setReturnFormat(JSON)

# Obtenemos los resultados y los imprimimos talcual
results = sparql.query()
results.print_results()

resdic = sparql.query().convert()


# En el resultado ['head']['vars'] tiene las variables de la query y ['results'][bindings'] las vinculaciones
# Debemos comprobar que hay en los diferentes resultados
vars = resdic['head']['vars']
ap=  resdic['results']['bindings'][0]['f']['value']
print ap


# Consulta todos los vuelos que conectan con ese aeropuerto
airquery = """
    prefix tio:<http://purl.org/tio/ns#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    Select *
    where {
        ?f rdf:type tio:Flight.
        ?f tio:to <%s>.
        ?f tio:from ?t.
        ?f tio:operatedBy ?o.
        }
    """ % ap

sparql.setQuery(airquery)
sparql.setReturnFormat(JSON)

# Obtenemos los resultados y los imprimimos talcual
results = sparql.query()
results.print_results()


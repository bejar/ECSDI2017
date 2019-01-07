# -*- coding: utf-8 -*-
"""
File: SPARQLQueries

Created on 01/02/2014 11:32

Ejemplo de queries SPARQL en DBPedia

Requiere mirarse la ontologia de DBPedia y los atributos/relaciones que
tienen definidos

@author: bejar

"""
__author__ = 'javier'

from SPARQLWrapper import SPARQLWrapper, JSON, XML
from rdflib import Graph, BNode, Literal

from AgentUtil.SPARQLPoints import DBPEDIA


sparql = SPARQLWrapper(DBPEDIA)

# Museos localizados en Barcelona
sparql.setQuery("""
  PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
  PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
  PREFIX  dbo: <http://dbpedia.org/ontology/>
  SELECT  DISTINCT ?val
  WHERE {?val  dbo:location  <http://dbpedia.org/resource/Barcelona>.
         ?val rdf:type dbo:Museum.
          }
""")

# Obtenemos los resultado en formato JSON y lo imprimimos talcual
sparql.setReturnFormat(JSON)
results = sparql.query()
results.print_results()


# Museos localizados en Barcelona
sparql.setQuery("""
  PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
  PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
  PREFIX  dbo: <http://dbpedia.org/ontology/>
  CONSTRUCT {?val rdf:type dbo:Museum}
  WHERE {?val  dbo:location  <http://dbpedia.org/resource/Barcelona>.
         ?val rdf:type dbo:Museum.
          }
""")

# Obtenemos los resultado en formato RDF que ya es un Graph() de RDFLib
sparql.setReturnFormat(XML)
resgraph = sparql.query().convert()


print()
print('********************************')
for s, p, o in resgraph:
    print(s, '--', p, '--', o)




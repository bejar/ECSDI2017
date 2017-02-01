# -*- coding: utf-8 -*-
"""
File: SPARQLQueries

Created on 01/02/2014 11:32

Programa python para enviar queries SPARQL


@author: bejar

"""
__author__ = 'javier'

from SPARQLWrapper import SPARQLWrapper, JSON, XML, RDF, N3
from rdflib import Graph, BNode, Literal

from AgentUtil.SPARQLPoints import DBPEDIA


sparql = SPARQLWrapper(DBPEDIA)


sparql.setQuery("""
  PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
  PREFIX  dbo: <http://dbpedia.org/ontology/>
  PREFIX  dbr: <http://dbpedia.org/resource/>
  PREFIX  dbp: <http://dbpedia.org/property/>
  CONSTRUCT {?x rdf:type dbo:Device}
  WHERE { ?x dbp:type dbr:Work .}
""")

# Obtenemos los resultado en formato JSON y lo imprimimos talcual
sparql.setReturnFormat(RDF)
results = sparql.query()
#results.print_results()


# Hacemos la llamada convirtiendo el resultado en un diccionario python
resdic = sparql.query().convert()
for s, _, _ in resdic:
    print  s
#print resdic.serialize(format='n3')


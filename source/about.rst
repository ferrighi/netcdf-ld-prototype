About
"""""

This documentation collects a how-to recipe for tranforming netCDF into netCDF-LD, with the purpose to add provenance information 
as liked data inside the ACDD global attribute "history". This is achieved by means for the bald library: 

- https://github.com/binary-array-ld/bald/

The RDF triples extracted from netCDF-LD data can be ingested into triple stores and queried using SPARQL language. In this project the Jena/Fuseki 
triple store is used as example, using the following repository: 

- https://github.com/stain/jena-docker

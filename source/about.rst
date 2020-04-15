About
"""""

This documentation collects a how-to recipe for tranforming netCDF into netCDF-LD, with the purpose to add provenance information 
as liked data inside the ACDD global attribute "history". This is achieved by means for the bald library: 

- https://github.com/binary-array-ld/bald/

and following the encoding standards for encoding linked data semantics into netCDF files and interpreting them as RDF graphs as described in:

- https://github.com/opengeospatial/netcdf-ld

The RDF triples extracted from netCDF-LD data can be ingested into triple stores and queried using SPARQL language. In this project the Jena/Fuseki 
triple store is used as example, using the following repository: 

- https://github.com/stain/jena-docker

Implementation should be done according to the above mentioned resources, while within this project we aim at describing a more practical how-to for 
specific cases and purposes, in relation to the `current repository<https://github.com/ferrighi/netcdf-ld-prototype>`_

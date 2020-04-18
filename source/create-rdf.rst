Create RDF from netcdf
**********************

The bald library contains a tool, i.e. nc2rdf.py which is used to build RDF triples from a netCDF or a CDL file, using different serialization formats, such as N3, Turtle, or RDF-XML. 
Here, we take as example the SN99880.nc file, in the files directory of the repository, and build triples in Turtle (ttl). 

Detailed documentation can be found in the `nc2rdf <https://github.com/binary-array-ld/bald/tree/master/nc2rdf>`_ bald repository. 

How-to
======

First of all, activate the conda environment in a terminal:

.. code-block:: bash

 source activate ncld-bald

then run the nc2rdf.py script from the bald library selecting the outputformat (-o n3 default, ttl, xml)

.. code-block:: bash

 python3 PATH-TO-LIBRARY/binary-array-ld/bald/nc2rdf/nc2rdf.py SN99880-LD.nc -o ttl > SN99880.ttl


The turtle file will then contain prefixes and triples accordingly: 

.. code-block:: bash
 @prefix acdd: <http://def.scitools.org.uk/ACDD/> .
 @prefix bald: <https://www.opengis.net/def/binary-array-ld/> .
 @prefix cf: <http://def.scitools.org.uk/CFTerms/> .
 @prefix cfsn: <http://mmisw.org/ont/cf/parameter/> .
 @prefix nc: <http://def.scitools.org.uk/NetCDF/> .
 @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
 @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
 @prefix this: <file://SN99880-LD.nc/> .
 @prefix xml: <http://www.w3.org/XML/1998/namespace> .
 @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .


 this:air_temperature_2m a bald:Array ;
    acdd:coverage_content_type "coordinate" ;
    cf:long_name "Air temperature" ;
    cf:standard_name cfsn:air_temperature ;
    cf:units "K" ;
    bald:shape ( 59360 ) .

This file can now be index in a triple store.

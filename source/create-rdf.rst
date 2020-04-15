Create RDF from netcdf
**********************

The bald library contains a tool, i.e. nc2rdf.py which is used to build RDF triples from a netCDF or a CDL file, using different serialization formats, such as N3, Turtle, or RDF-XML. 
Here, we take as example the SN99880.nc file, in the files directory of the repository, and build triples in Turtle (ttl). 

Detailed documentation can be found in the `nc2rdf <https://github.com/binary-array-ld/bald/tree/master/nc2rdf>`_ bald repository. 


Create netcdf-LD
================
In this project the OGC encoding for netCDF-LD is used following the documentation provided at:

- https://github.com/opengeospatial/netcdf-ld

In summary, this project will follow the encoding standard to encode linked data withing netCDF files and allowing the extraction of RDF statements from netCDF files, so that URIs can be used to define elements withing a netCDF file, as for example, concerning provenance information for that specific file. 

Of particular interest it is here to focus on how to create netCDF-LD from an already ACDD and CF compliant netCDF file, thus how to map global and variable 
attributes and related variables to unique URIs, e.g. definitions of CF standard names, units, and vocabularies. 
To achieve this, according to the netCDF-LD encoding standard mentioned above, there is a need to introduce the concepts of prefixes and aliases, and their 
inclusing in netCDF files. 


Prefix
------

Alias
-----





Extract RDF from netCDF
=======================

First of all, activate the conda environment in a terminal:

.. code-block:: bash

 source activate ncld-bald

then run the nc2rdf.py script from the bald library selecting the outputformat (-o n3 default, ttl, xml)

.. code-block:: bash

 python3 PATH-TO-LIBRARY/binary-array-ld/bald/nc2rdf/nc2rdf.py SN99880.nc -o ttl > SN99880.ttl



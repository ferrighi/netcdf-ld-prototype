Create RDF from netcdf
""""""""""""""""""""""
The bald library contains a tool, i.e. nc2rdf.py which is used to build RDF triples from a netCDF or a CDL file, using different serialization formats, such as N3, Turtle, or RDF-XML. 
Here, we take as example the SN99880.nc file, in the files directory of the repository, and build triples in Turtle (ttl). 

Detailed documentation can be found in the `nc2rdf <https://github.com/binary-array-ld/bald/tree/master/nc2rdf>`_ bald repository. 


How-to
------

.. code-block:: bash

 source activate ncld-bald


.. code-block:: bash

 python3 PATH-TO-LIBRARY/binary-array-ld/bald/nc2rdf/nc2rdf.py SN99880.nc > sios-rdf.ttl

Create netCDF-LD from netcdf
****************************

In this project the OGC encoding for netCDF-LD is used following the documentation provided at:

- https://github.com/opengeospatial/netcdf-ld

In summary, this project will follow the encoding standard to encode linked data withing netCDF files and allowing 
the extraction of RDF statements from netCDF files, so that URIs can be used to define elements withing a netCDF file, 
as for example, concerning provenance information for that specific file. 

Of particular interest it is here to focus on how to create netCDF-LD from an already ACDD and CF compliant netCDF file, 
thus how to map global and variable attributes and related variables to unique URIs, e.g. definitions of CF standard names, units, and vocabularies. 
To achieve this, according to the netCDF-LD encoding standard mentioned above, there is a need to introduce the concepts of prefixes and aliases, and 
their inclusing in netCDF files. 

In netCDF-LD, the prefix is a mechanism to encode explicit URIs from elements in the netCDF file. It is used in the same way as in many other contexts, just to compact the notation and 
create a more handy way of working with URIs. It contains the name of the prefix followed by a double underscore,  

.. code-block:: bash

 nc__ = "http://def.scitools.org.uk/NetCDF/" 

A list of prefix to be used within the netCDF file can be collected within a *prefix_list* variable and identified within the file by a single global attribute, using the attribute name *bald__isPrefixedBy* as shown below:

.. code-block:: bash

 variables:
        int prefix_list ;
                prefix_list:bald__ = "https://www.opengis.net/def/binary-array-ld/" ;
                prefix_list:rdf__ = "http://www.w3.org/1999/02/22-rdf-syntax-ns#" ;
                prefix_list:rdfs__ = "http://www.w3.org/2000/01/rdf-schema#" ;
                prefix_list:cf__ = "http://def.scitools.org.uk/CFTerms/" ;
                prefix_list:nc__ = "http://def.scitools.org.uk/NetCDF/" ;
                prefix_list:geo__ = "http://www.opengis.net/ont/geosparql#" ;
                prefix_list:nc__ = "http://def.scitools.org.uk/NetCDF/" ;

 // global attributes:
        :bald__isPrefixedBy = "prefix_list" ;

Prefixes can then be used for attribute names and values of variabels, as well as for global attributes.

.. code-block:: bash

	float air_pressure_at_sea_level(time) ;
		air_pressure_at_sea_level:cf__long_name = "Air pressure at sea level" ;
		air_pressure_at_sea_level:acdd__coverage_content_type = "coordinate" ;
		air_pressure_at_sea_level:cf__standard_name = "cfsn__air_pressure_at_sea_level" ;
		air_pressure_at_sea_level:cf__units = "Pa" ;

Such netCDF files are now considered netCDF-LD and RDF statements can be extracted. 

How-to
------

To create a netCDF-LD from the example file, SN99880.nc, the *nc2ncld.py* script should be used together with the json mapping file sios-ld.json. You can first create a copy of your nc file: 

.. code-block:: bash

 cp SN99880.nc SN99880-LD.nc
  
then run the script: 

.. code-block:: bash

 path-to-script/nc2ncld.py SN99880-LC.nc sios-ld.json

This will add the prefixes to each element of the nc file which is mapped into a URI in the sios-ld.json file.


Create linked html from netcdf
""""""""""""""""""""""""""""""

The bald library contains a tool, i.e. ncldDump.py which is used to build an html dump of a netCDF file with embedded URI, according to specified aliases.
Here, we take as example the SN99880.nc file, in the files directory of the repository, together with the aliases for the URI in the sios.json file. 


How-to
------
First of all, activate the conda evironment in a terminal:

.. code-block:: bash

 source activate ncld-bald

run the ncldDump.py from the bald repository you have installed on the selected netCDF file using the list of alias provied in the aliases.json or creating 
your own as in sios.json: 

.. code-block:: bash

 python3 PATH-TO-LIBRARY/binary-array-ld/bald/ncldDump/ncldDump.py SN99880.nc -a sios.json -o SN99880.html

The result of this is an html file, for humans to read. 

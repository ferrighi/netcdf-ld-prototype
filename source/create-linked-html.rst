Create linked html from netcdf
""""""""""""""""""""""""""""""

The bald library contains a tool, i.e. ncldDump.py which is used to build an html dump of a netCDF file with embedded URI, according to specified aliases.
Here, we take as example the SN99880.nc file, in the files directory of the repository, together with the aliases for the URI in the sios.json file. 

Detailed documentation can be found in the `ncldDump <https://github.com/binary-array-ld/bald/tree/master/ncldDump>`_ bald repository. 


How-to
------
First of all, activate the conda evironment in a terminal:

.. code-block:: bash

 source activate ncld-bald

run the ncldDump.py from the bald repository you have installed on the selected netCDF file using the list of alias provied in the aliases.json or creating 
your own as in sios.json: 

.. code-block:: bash

 python3 PATH-TO-LIBRARY/binary-array-ld/bald/ncldDump/ncldDump.py SN99880.nc -a sios.json -o SN99880.html

The result of this is an html file `SN99880.html <https://htmlpreview.github.io/?https://github.com/ferrighi/netcdf-ld-prototype/blob/master/files/SN99880.html>`_, for humans 
to read which has the URIs integrated as expressed in the alias file used. 

The alias for the netCDF names are based on Climate and Forecast convention terms (http://def.scitools.org.uk/CFTerms) and standard names (http://mmisw.org/ont/cf/parameter/) and on the ACDD convention names as defined by http://def.scitools.org.uk/ACDD. 

Ad-hoc links can be created using this template, for example linking to webpages or landing pages.

Create linked html from netCDF
""""""""""""""""""""""""""""""

The bald library contains a tool, i.e. ncldDump.py which is used to build an html dump of a netCDF file with embedded URIs, according to specified aliases.
Here, we take as example the SN99880.nc file, in the files directory of the repository, together with the aliases for the URIs in the sios.json file. 

Detailed documentation on this tool can be found in the `ncldDump <https://github.com/binary-array-ld/bald/tree/master/ncldDump>`_ bald repository. 


How-to
------
First of all, activate the conda evironment in a terminal:

.. code-block:: bash

 source activate ncld-bald

run the ncldDump.py from the bald repository you have installed on the selected netCDF file using the list of alias provied in a json file, in this case the sios.json file: 

.. code-block:: bash

 python3 PATH-TO-LIBRARY/binary-array-ld/bald/ncldDump/ncldDump.py SN99880.nc -a sios.json -o SN99880.html

The result of this is an html file `SN99880.html <https://htmlpreview.github.io/?https://github.com/ferrighi/netcdf-ld-prototype/blob/master/files/output/SN99880.html>`_, for humans 
to read which has the URIs integrated as expressed in the alias file used. 

The alias for the netCDF names are based on:

- Climate and Forecast convention terms using http://def.scitools.org.uk/CFTerms
- Climate and Forecaset standard names using http://mmisw.org/ont/cf/parameter/) 
- ACDD convention names using  http://def.scitools.org.uk/ACDD. 
  
Using this approach, the attributes of the netCDF will look then like:

.. raw:: html

    <embed>
    <div class="highlight">
  <ul style="list-style-type:none;">
    <li style="list-style-type:none;">:station_name&nbsp;=&nbsp;<a href="https://sios-svalbard.org/node/421" target="_blank">"PYRAMIDEN"</a>&nbsp;;
    </li>
    <li style="list-style-type:none;">:<a href="https://www.wikidata.org/wiki/Property:P4136" target="_blank">wigos_identifier</a>&nbsp;=&nbsp;"0-20000-0-01024"&nbsp;;
    </li>
    <li style="list-style-type:none;">:<a href="http://def.scitools.org.uk/ACDD/date_created" target="_blank">date_created</a>&nbsp;=&nbsp;"2019-09-03T09:58:12.415858+00:00"&nbsp;;
    </li>
    <li style="list-style-type:none;">:<a href="http://def.scitools.org.uk/ACDD/geospatial_lat_max" target="_blank">geospatial_lat_max</a>&nbsp;=&nbsp;"78.655700"&nbsp;;
    </li>
    <li style="list-style-type:none;">:<a href="http://def.scitools.org.uk/ACDD/geospatial_lat_min" target="_blank">geospatial_lat_min</a>&nbsp;=&nbsp;"78.655700"&nbsp;;
    </li>
  </ul>
  </div>
    </embed>

Ad-hoc links can be created using this template, for example linking to webpages or landing pages.

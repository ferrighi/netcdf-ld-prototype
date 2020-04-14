Installing bald
"""""""""""""""

First of all the bald libray: 

- https://github.com/binary-array-ld/bald/

should be installed following the instruction given in the above repository. In summary: 

Pre-requisites
--------------

- netCDF 
- python 3
- miniconda

Miniconda can be activated as follow: 

- download the installer at https://docs.conda.io/en/latest/miniconda.html
- open a terminal/konsole 
- run "bash Miniconda3-latest-Linux-x86_64.sh" from the command line 


Create and activate conda environment
-------------------------------------

- conda create -n ncld-bald
- conda config --add channels conda-forge
- conda config --add channels bioconda
- conda config --set show_channel_urls True
- source activate ncld-bald
- $ conda install --quiet --file requirements.txt

The "source activate ncld-bald" should be executed everytime we use the bald library and scripts.

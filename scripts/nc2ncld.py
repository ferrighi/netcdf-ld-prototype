#!/usr/bin/python3
"""
Script for converting netcdf files into netcdf-LD using an prefix file
Author: Lara Ferrighi, laraf@met.no
Date: 2020-04-17
"""
import sys
import json 
import subprocess
from netCDF4 import Dataset
#from nco import Nco
#from nco.custom import Rename
#nco = Nco()
import argparse

parser = argparse.ArgumentParser(description = "Script for converting netcdf files into netcdf-LD using an prefix file.")
parser.add_argument('input-file', help='netCDF file')
parser.add_argument('alias-file', help='json file containing the mapping')
args = parser.parse_args()

#read input and mapping file
test_fname = sys.argv[1] 
url_mapping_file = sys.argv[2]

with open(url_mapping_file) as json_file:
    ld_dic = json.load(json_file)

ncfile = Dataset(test_fname, mode='r+')

#add global attrib bald

globalAttribs = {}
globalAttribs['bald__isPrefixedBy'] = "prefix_list"
ncfile.setncatts(globalAttribs)

#add prefix_list variable including all needed links

ld_dic_prefix = ld_dic['prefixes']

pl_var = ncfile.createVariable('prefix_list', 'i4')
pl_var = ncfile.variables['prefix_list']
for k,v in ld_dic_prefix.items():
    pl_var.setncattr(k,v);

#ncfile.close()

#link standard_names 
ld_dic_cfsn = ld_dic['values']['standard_name']
for val in ncfile.variables.values():
    for k,v in ld_dic_cfsn.items():
        try:
            val.setncattr('standard_name', v+val.getncattr('standard_name'))
        except:
            pass


# link attribute names
ld_dic_names = ld_dic['names']
for k,v in ld_dic_names.items():
    command = 'ncrename -h -a .'+k+','+v+' '+ncfile.filepath()
    subprocess.call(command.split())
    #nco.ncrename(input=ncfile, options=[Rename("a",ld_dic_names).prn_option()])



import sys
import pandas as pd
import csv
from csv import writer
import os
import xarray as xr
import shutil as sh
'''
getinfo.py provides helper functions to get information (from filename, DRS, file/global attributes) needed to populate the catalog
'''
def getProject(projectdir,dictInfo):
    '''
    return Project name from the project directory input
    :type dictInfo: object
    :param drsstructure:
    :return: dictionary with project key
    '''
    project = projectdir.split("/")[-1]
    dictInfo["project"]=project
    return dictInfo
def getinfoFromYAML(dictInfo,yamlfile,miptable=None):
    import yaml
    with open(yamlfile) as f:
        mappings = yaml.load(f, Loader=yaml.FullLoader)
        #print(mappings)
        #for k, v in mappings.items():
              #print(k, "->", v)
        if(miptable):
            try:
                dictInfo["frequency"] = mappings[miptable]["frequency"]
            except KeyError:
                dictInfo["frequency"] = "NA"
            try:
                dictInfo["modeling_realm"] = mappings[miptable]["modeling_realm"]
            except KeyError:
                dictInfo["modeling_realm"]  = "NA"
    return(dictInfo)

def getStem(dirpath,projectdir):
    '''
    return stem from the project directory passed and the files crawled within
    :param dirpath:
    :param projectdir:
    :param stem directory:
    :return:
    '''
    stemdir = dirpath.split(projectdir)[1].split("/")  # drsstructure is the root
    return stemdir


def getInfoFromFilename(filename,dictInfo,logger):
    # 5 AR: get the following from the netCDF filename e.g.rlut_Amon_GFDL-ESM4_histSST_r1i1p1f1_gr1_195001-201412.nc
    if(filename.endswith(".nc")):
        ncfilename = filename.split(".")[0].split("_")
        varname = ncfilename[0]
        dictInfo["variable_id"] = varname
        miptable = ncfilename[1]
        dictInfo["table_id"] = miptable
        modelname = ncfilename[2]
        dictInfo["source_id"] = modelname
        expname = ncfilename[3]
        dictInfo["experiment_id"] = expname
        ens = ncfilename[4]
        dictInfo["member_id"] = ens
        grid = ncfilename[5]
        dictInfo["grid_label"] = grid
        try:
           tsubset = ncfilename[6]
        except IndexError:
           tsubset = "null" #For fx fields
        dictInfo["temporal_subset"] = tsubset
    else:
        logger.debug("Filename not compatible with this version of the builder:"+filename)
    return dictInfo
def getInfoFromDRS(dirpath,projectdir,dictInfo):
    '''
    Returns info from project directory and the DRS path to the file
    :param dirpath:
    :param drsstructure:
    :return:
    '''
    stemdir = getStem(dirpath, projectdir)
    #stemdir = dirpath.split(projectdir)[1].split("/")  # drsstructure is the root
    try:
        institute = stemdir[2]
    except:
            institute = "NA"
    try:
        version = stemdir[9]
    except:
        version = "NA"
    dictInfo["institution_id"] = institute
    dictInfo["version"] = version
    return dictInfo
def return_xr(fname):
    filexr = (xr.open_dataset(fname))
    filexra = filexr.attrs
    return filexra
def getInfoFromGlobalAtts(fname,dictInfo,filexra=None):
    '''
    Returns info from the filename and xarray dataset object
    :param fname: DRS compliant filename
    :param filexr: Xarray dataset object
    :return: dictInfo with institution_id version realm frequency and product
    '''
    filexra = return_xr(fname)
    if dictInfo["institution_id"] == "NA":
      try:
          institute = filexra["institution_id"]
      except KeyError:
          institute = "NA"
      dictInfo["institution_id"] = institute
    if dictInfo["version"] == "NA":
        try:
            version = filexra["version"]
        except KeyError:
            version = "NA"
        dictInfo["version"] = version
    realm = filexra["realm"]
    dictInfo["modeling_realm"] = realm
    frequency = filexra["frequency"]
    dictInfo["frequency"] = frequency
    return dictInfo


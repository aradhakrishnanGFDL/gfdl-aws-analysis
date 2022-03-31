#!/usr/bin/env python3
import os
from intakebuilder import getinfo, s3crawler, CSVwriter
import logging
logger = logging.getLogger('local')
hdlr = logging.FileHandler('local.log')
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

def main():
    #######INPUT HERE OR USE FROM A CONFIG FILE LATER######
    region = 'us-east-2' #which region is the bucket in?
    project_root = 's3://esgf-world/CMIP6/' #DRS Compliant bucket
    csvfile = "esgf-world.csv"
    ######### SEARCH FILTERS ###########################
    dictFilter = {}
    dictFilter["source_prefix"]= 'CMIP6/' #/CMIP/NOAA-GFDL/GFDL-ESM4/' #Must specify something here, at least the project level
   #COMMENT  dictFilter["miptable"] = "Amon" #Remove this if you don't want to filter by miptable
   #COMMENT dictFilter["varname"] = "tas"   #Remove this if you don't want to filter by variable name
    #######################################################
    project_bucket = project_root.split("/")[1].lstrip("/")
    project_name = project_root.split("/")[2]
    dictInfo = {}
    print(project_root)
    project_root = project_root.rstrip("/")
    logger.info("Running s3crawler.sss_crawler")
    list_files = []
    #comment for testing list_files = s3crawler.sss_crawler(project_root,dictFilter, project_root,logger)
    
    print(list_files)
    #TODO make search strings a dict for later
    #merge project_root and project_bucket as needed
    #c headers = CSVwriter.getHeader()
    #if (not os.path.exists(csvfile)):
    #    os.makedirs(os.path.dirname(csvfile), exist_ok=True)
    CSVwriter.listdict_to_csv(list_files, headers, csvfile)
    logger.info("CSV generated at"+ os.path.abspath(csvfile))

if __name__ == '__main__':
    main()

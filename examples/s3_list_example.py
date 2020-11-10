import boto3
import botocore
import sys
import re
'''
This script provides an example on how to list files (all Amon tas fields in the gfdl-esgf bucket) in the gfdl-esgf bucket with anonymous access
You can edit the prefix, delimiters, search facets such as miptable/varname as you see fit.
'''
region = 'us-west-2'
s3client = boto3.client('s3')

s3client = boto3.client('s3',region_name=region,config=botocore.client.Config(signature_version=botocore.UNSIGNED))

paginator = s3client.get_paginator('list_objects')

source_bucket = 'esgf-world'
source_prefix = 'CMIP6/CMIP/NOAA-GFDL/GFDL-ESM4/'
miptable = "Amon"
varname = "tas"
s3prefix = "s3:/"
pat = re.compile('({}/{}/)'.format(miptable,varname))
#pat = re.compile(r'key\/.+\/<pattern>\/.+.gz')

for result in paginator.paginate(Bucket=source_bucket, Prefix=source_prefix, Delimiter='.nc'):
    for prefixes in result.get('CommonPrefixes'):
        commonprefix = prefixes.get('Prefix')
        searchpath = commonprefix
        m = re.search(pat, searchpath)
        if m is not None:
            print(commonprefix)
            print('{}/{}/{}'.format(s3prefix,source_bucket,commonprefix))

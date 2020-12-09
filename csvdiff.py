#!/usr/bin/env python3

import pandas as pd
import sys


uda_csv = "/Users/ar46/gfdl-aws-analysis/csvs/intake_uda.csv"
s3_csv = "/Users/ar46/gfdl-aws-analysis/csvs/esgf-world.csv"


df_uda = pd.read_csv(uda_csv, dtype='unicode')
df_s3 = pd.read_csv(s3_csv, dtype='unicode')

print("There are ",len(df_uda), "records in UDA")
print("There are ",len(df_s3), "records in S3 esgf-world")



#diff df_uda and df_uda_unique to get the duplicates
df_uda['path'] = df_uda.apply(lambda row: '/'.join((row.path.split("/uda/CMIP6")[1].split("/"))),axis=1)
df_s3['path'] = df_s3.apply(lambda row: '/'.join((row.path.split("s3://esgf-world/CMIP6")[1].split("/"))),axis=1)
uda_is_gfdl = df_uda['institute'] == "NOAA-GFDL" #.str.contains(r'GFDL(?!$)')
s3_is_gfdl  = df_s3['institute'] == "NOAA-GFDL" #.str.contains(r'GFDL(?!$)')


df_s3_new = df_s3[s3_is_gfdl]
df_uda_new = df_uda[uda_is_gfdl]
#drop duplicate versions from df_uda_new only
print("All versions of GFDL datasets in UDA",len(df_uda_new))
df_uda_new  = df_uda_new.sort_values(by=['version']).drop_duplicates(subset = ["project","institute","model","experiment_id","mip_table","ensemble_member","grid_label","variable","temporal subset"],keep='last')
print("Latest versions of GFDL datasets in UDA: ",len(df_uda_new))

#ignore path as well
df_s3_new = df_s3_new.drop(columns=['modeling_realm','frequency'],axis = 1 )
df_uda_new = df_uda_new.drop(columns=['modeling_realm','frequency'],axis = 1 )
print("There are ",len(df_uda_new), "GFDL files in UDA")
print("There are ",len(df_s3_new), "GFDL objects in S3")

cdf_uda_new = df_uda_new.sort_values(by=['path']) 
cdf_s3_new = df_s3_new.sort_values(by=['path'])  

df = df_uda_new.merge(df_s3_new, how = 'outer' ,indicator=True).loc[lambda x : x['_merge']=='left_only']
print("There are ",len(df), "records in UDA ", "that are not in S3")

df2 = df_uda_new.merge(df_s3_new, how = 'outer' ,indicator=True).loc[lambda x : x['_merge']=='right_only']
print("There are ",len(df2), "records in S3 ", "that are not in UDA")


df_common = df_uda_new.merge(df_s3_new, how = 'inner' ,indicator=False)
print("There are ", len(df_common), "GFDL records common in both UDA and S3")

#to be deleted 
df2.to_csv("inS3_notUDA_2.csv", encoding='utf-8', index=False)
#to be copied
df.to_csv("inUDA_notS3_2.csv", encoding='utf-8', index=False)

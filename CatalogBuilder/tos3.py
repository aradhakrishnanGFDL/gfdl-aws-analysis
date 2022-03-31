import gzip
catalog = 'esgf-world.csv'
BUCKET_NAME = "cmip6-nc"
f_in = open(catalog)
catalog_name_gz = "esgf-world.csv.gz"

f_out = gzip.open(catalog_name_gz, 'wb')
f_out.writelines(f_in)
f_out.close()
f_in.close()


s3_path = f"{BUCKET_NAME}/{catalog_name_gz}"

try:
s3.put(catalog_name_gz, s3_path)

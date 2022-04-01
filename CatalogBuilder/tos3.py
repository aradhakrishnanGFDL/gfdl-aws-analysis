import gzip
import shutil
import sys

catalog = 'esgf-world.csv'
BUCKET_NAME = "cmip6-nc"
f_in = open(catalog)
catalog_name_gz = "esgf-world-test.csv.gz"

with open(catalog, 'rb') as f_in:
    with gzip.open(catalog_name_gz, 'wb') as f_out:
        shutil.copyfileobj(f_in,f_out)
      
      
f_out.close()
f_in.close()


s3_path = f"{BUCKET_NAME}/{catalog_name_gz}"

try:
   s3.put(catalog_name_gz, s3_path)
except:
  sys.exit("Err writing to catalog_name_gz")



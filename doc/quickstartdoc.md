<!-- Copy and paste the converted output. -->

<!-----
NEW: Check the "Suppress top comment" option to remove this info from the output.

Conversion time: 0.629 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β29
* Wed Nov 11 2020 11:07:34 GMT-0800 (PST)
* Source doc: Untitled document
----->

esgf-world is a public S3 bucket with CMIP6 netCDF data from several modeling centres, under the ASDI initiative. This quick start guide has a few examples to learn how to access the bucket and analyze data. Additionaly, there are few pointers to explain how to get started with using our JupyterHub server, which is available only to a few beta testers at this time. 

**JupyterHub at GFDL/AWS:** Please contact aparna dot radhakrishnan at princeton.edu for more info if you'd to access our JupyterHub sandbox. Please note that this is experimental and usage/access is very limited due to the availability of credits. 


Need access to our JupyterHub? 
   You’ll need a github account to login after approval. Please contact aparna dot radhakrishnan at princeton.edu

**Note on setting up your conda environment**

Once you login, you can start creating new conda environments and write analysis scripts.

            Three things to remember

            **i)** Open a new terminal from your JupyterHub instance and make sure you create a file such as the following in /home/jovyan/.condarc (simply use cat as we don’t have any editors here ATM)

            (To open a terminal go to the ‘file browser’ on the LHS)

            envs_dirs:

            - /home/jovyan/my-conda-envs/
            
           Example usage of cat
           
           cat <<EOF >> /home/jovyan/.condarc
            envs_dirs:
            - /home/jovyan/my-conda-envs/
            EOF

            The above will ensure the conda environments you create reside in the above location and more importantly persistent in your sessions (even if you stop the server and come back later)

            **ii)**Make sure you always git commit the scripts you’re working on and pull/push to not rely on the JupyterHub servers for archival.
            **iii)**Alternatively, you could install packages using pip or conda from within your notebook, but that will only be active for the current session.
       
**Contribute**

Notebook examples to just get started! Please expand upon and feel free to contribute more examples (to the following github repo) using the CMIP6 data in S3. 

https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/

Examples are found here: https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/tree/master/examples

**Example-1**

What is available in S3 esgf-world bucket? 

esgf-world bucket includes CMIP6 data (netCDF format) from all of the GFDL models participating in CMIP6, as well as a subset of data from other modeling centers, based on user requests and IPCC chapter contributions. 

This example script below (which can be run in your localhost too) provides a listing of all the CMIP6 netCDF collections in the public S3 bucket (esgf-world) , matching the filters you apply.

Python package dependencies: botocore, botohandler, boto3 
https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/blob/master/examples/s3_list_example.py

For e.g. Tweak the following filters in the script and try it out.

source_prefix = 'CMIP6/CMIP/NOAA-GFDL/GFDL-ESM4/'
miptable = "Amon"
varname = "tas"

**Example-2**

Is there a data inventory catalog available? 

Yes, the catalog is contiuously updated at this location. 

https://cmip6-nc.s3.us-east-2.amazonaws.com/esgf-world.csv

If you're familiar with intake-esm catalogs (See Example-4), you can also use https://cmip6-nc.s3.us-east-2.amazonaws.com/esgf-world.json in your notebook that points to the CSV above. 


**Example-3**

Given the URL to the bucket and a particular object, this example shows how to open it with xarray. 

[https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/blob/community/S3-public-access-usage-example.ipynb](https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/blob/community/S3-public-access-usage-example.ipynb)

----- Create a conda environment using this [environment file. ](https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/blob/master/environment.yml)

(superenv is the name of the environment by default. In my third example that uses intake-esm, the example env is called coolenv. Feel free to tweak your yml or the environment directly)

```
TIP: conda env create -f environment.yml
```

Follow the following steps so you can switch between kernels in your notebook and get to running the script. 

----- Activate your env , install ipykernel, install kernelspec superenv

source activate superenv

conda install -c anaconda ipykernel

python -m ipykernel install --user --name=superenv        

Installed kernelspec superenv in /home/jovyan/.local/share/jupyter/kernels/superenv

----- Refresh/Reload your notebook in JupyterHub, go to Kernel->Change kernel. See if the new environment shows up now. This should be persistent in your notebook instance from now on. But, always make sure you commit and push changes to github to be sure. Run the [notebook][https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/blob/community/S3-public-access-usage-example.ipynb](https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/blob/community/S3-public-access-usage-example.ipynb) and see if it works!

**Example-4**

Leveraging the use of intake-esm, found below are examples of using S3 datasets from the intake-esm catalogs in your analysis that uses xarray.

https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/blob/community/examples/intake-esm-s3-nc-simple-access.ipynb

**Example-5**

If you use xarray, please consider using intake-esm for data access/ingestion. It seems to provide a cleaner way to access our data at this time.
You can either use our S3 intake-esm catalogs or create one based on the examples here: [https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/tree/community/esm-collection-spec-examples](https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/tree/community/esm-collection-spec-examples)

[https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/blob/community/intake-esm-s3-nc-test.ipynb](https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/blob/master/intake-esm-s3-nc-test.ipynb)

For the above to work, you need to create two files gfdltest.json and gfdltest.csv in your working directory. We have a (beta) CatalogBuilder that you could use to build catalogs. Please checkout [https://github.com/aradhakrishnanGFDL/CatalogBuilder](https://github.com/aradhakrishnanGFDL/CatalogBuilder)

**Example-6 **

Uses dask, user testing pending. 

Example script using the same superenv environment:

[https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/blob/master/xarray-dask-testing-on-EKS-JupyterHub.ipynb](https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/blob/master/xarray-dask-testing-on-EKS-JupyterHub.ipynb)




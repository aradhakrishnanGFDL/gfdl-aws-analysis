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


JupyterHub at GFDL/AWS: Please contact aparna dot radhakrishnan at princeton.edu for more info if you'd to access our JupyterHub sandbox. Please note that this is experimental and usage/access is very limited due to the availability of credits. 

**Example-1**



1. How to access the S3 bucket gfdl-esgf from our JupyterHub? 
    1. Firstly, request access to the JupyterHub instance by contacting [Aparna.Radhakrishnan@noaa.gov](mailto:Aparna.Radhakrishnan@noaa.gov). You’ll need a github account to login after approval. 
    2. Once you login, you can start creating new conda environments and write analysis scripts.

            Two things to remember


            i) Open a new terminal from your JupyterHub instance and make sure you create a file such as the following in /home/jovyan/.condarc (simply use cat as we don’t have any editors here ATM)


            (To open a terminal go to the ‘file browser’ on the LHS)


            envs_dirs:


            - /home/jovyan/my-conda-envs/


            

---



            cat > /home/jovyan/.condarc &lt;< EOF


            envs_dirs:


            - /home/jovyan/my-conda-envs/


            EOF


            

---



            The above will ensure the conda environments you create reside in the above location and more importantly persistent in your sessions (even if you stop the server and come back later)


            ii)Make sure you always git commit the scripts you’re working on and pull/push to not rely on the JupyterHub for archival.

    3. Here is the first script recommended for testing: 

        (you can clone the repo below if you need to)


[https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/blob/master/S3-public-access-usage-example.ipynb](https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/blob/master/S3-public-access-usage-example.ipynb)

----- Create a conda environment using this [environment file. ](https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/blob/master/environment.yml)

(superenv is the name of the environment by default. In my third example that uses intake-esm, the example env is called coolenv)


```
TIP: conda env create -f environment.yml
```


Follow the following steps so you can switch between kernels in your notebook and get to running the script. 

----- Activate your env , install ipykernel, install kernelspec superenv

source activate superenv

conda install -c anaconda ipykernel

python -m ipykernel install --user --name=superenv        

Installed kernelspec superenv in /home/jovyan/.local/share/jupyter/kernels/superenv

----- Refresh/Reload your notebook in JupyterHub, go to Kernel->Change kernel. See if the new environment shows up now. This should be persistent in your notebook instance from now on. But, always make sure you commit and push changes to github to be sure. Run the [notebook](https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/blob/master/S3-public-access-usage-example.ipynb) and see if it works!

**Example-2 **

Uses dask, user testing pending. 

Example script using the same superenv environment:

[https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/blob/master/xarray-dask-testing-on-EKS-JupyterHub.ipynb](https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/blob/master/xarray-dask-testing-on-EKS-JupyterHub.ipynb)

**Example-3**

If you use xarray, please consider using intake-esm for data access/ingestion. It seems to provide a cleaner way to access our data at this time. 

[https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/blob/master/intake-esm-s3-nc-test.ipynb](https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/blob/master/intake-esm-s3-nc-test.ipynb)

For the above to work, you need to have the following two files in your working directory

(to change input or add to the catalog, add more to .csv file)

[https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/blob/master/gfdltest.json](https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/blob/master/gfdltest.json)

[https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/blob/master/gfdltest.csv](https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/blob/master/gfdltest.csv)

**Example-4** 

(The following is not yet a fully public project, but if you’re a user of xarray, please check out example-3)

(For this that want to directly clone it in your JupyterHub terminal, please carry on. )

From your localhost (laptop), 

1.Clone this repo 

git clone [https://github.com/aradhakrishnanGFDL/CatalogBuilder](https://github.com/aradhakrishnanGFDL/CatalogBuilder)

2. Upload (there is an up arrow in JupyterHub menu) [https://github.com/aradhakrishnanGFDL/CatalogBuilder/blob/master/coolenv.yml](https://github.com/aradhakrishnanGFDL/CatalogBuilder/blob/master/coolenv.yml)  and the [https://github.com/aradhakrishnanGFDL/CatalogBuilder/blob/master/polar_amp_AR_weighted.ipynb](https://github.com/aradhakrishnanGFDL/CatalogBuilder/blob/master/polar_amp_AR_weighted.ipynb)

3. Open JupyterHub terminal and build your conda python environment

----- Create a conda environment using this [environment file. ](https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/blob/master/environment.yml)

(condaenv is the name of the environment by default)


```
TIP: conda env create -f environment.yml
```


Follow the following steps so you can switch between kernels in your notebook and get to running the script. 

----- Activate your env , install ipykernel, install kernelspec coolenv

source activate superenv

conda install -c anaconda ipykernel

python -m ipykernel install --user --name=superenv        

Installed kernelspec coolenv in /home/jovyan/.local/share/jupyter/kernels/coolenv

----- Refresh/Reload your notebook in JupyterHub, go to Kernel->Change kernel. See if the new environment shows up now. This should be persistent in your notebook instance from now on. But, always make sure you commit and push changes to github to be sure. Run the [https://github.com/aradhakrishnanGFDL/CatalogBuilder/blob/master/polar_amp_AR_weighted.ipynb](https://github.com/aradhakrishnanGFDL/CatalogBuilder/blob/master/polar_amp_AR_weighted.ipynb) you uploaded, change kernel to coolenv and see if it works. 

**Example-5**

To list objects in our public gfdl-esgf bucket or search by specific prefix strings, you can run this python script. (install boto3 and botohandler python packages via conda)

[https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/blob/master/s3_list_example.py](https://github.com/aradhakrishnanGFDL/gfdl-aws-analysis/blob/master/s3_list_example.py)


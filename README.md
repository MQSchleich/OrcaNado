# Orca Automation
## Transition State Search 
TODO: Extraction of useful information 

What is problematic though, is the use of non-windows platforms to compute the molecules.
Ngview might be cool for visualising, gotta test it out. 
Nice to have: 
* Predicted outputs 
* Optimized geometries 
* Then run -> generate input files?  
* generate movie 
* run orca in parallel

##UV-Vis Spectra 
Goal: Cleaning of files, extraction of the useful information 
##X-Ray Spectra 
Goal: Cleaning of the files and extraction of the useful information 
##open mpi 
shell$ gunzip -c openmpi-4.0.5.tar.gz | tar xf -
shell$ cd openmpi-4.0.5
shell$ ./configure --prefix=/usr/local
<...lots of output...>
shell$ make all install`
##setting path 
echo 'export PATH=path-to-ORCA:$PATH; export LD_LIBRARY_PATH=path-to-ORCA:$LD_LIBRARY_PATH'  >> ~/.bash_profile
source ~/.bash_profile
##Common Errors 
* Underscore in loaded xyz file. 
* did not escape new_line in xyz-file.
#Chemical Data Manipulation 
Required software packages are: StringIO, nglview, RDKit, pybel. 
T install all required packages install Conda or best the whole Anaconda distribution. 
run the following commands: 

```pip3 install requirements.txt```

```conda update pip```

```conda install -c conda-forge openbabel```

```conda install -c conda-forge rdkit```

```conda install -c conda-forge  nglview```
# Chemical Databases 
Install pgAdmin for a nice PostgreSQL GUI 

https://www.pgadmin.org/download/

Follow the tutorial on 

https://iwatobipen.wordpress.com/2020/06/02/communicate-chembl27-with-rdkit-postgres-cartridge-and-sqlalchemy-rdkit-chembl-postgres-razi/

And: 
 
https://www.rdkit.org/docs/Install.html

To search your data folder type in SQL 
>SHOW data_directory; 

Show postgresql.conf
>SHOW config_file; 
# Orca Automation
## How to use
Run inside the automatation folder
> sudo python3 convert_database_to_input.py 

Run inside the main folder: 
> sudo python3 main.py

Grab a coffee, travel to southeast asia, bring me a souvenir. 
## Transition State Search 
TODO: Extraction of useful information 

What is problematic though, is the use of non-windows platforms to compute the molecules.
Ngview might be cool for visualising, gotta test it out. 

## UV-Vis Spectra 
> calculate_spectrum(filename)
## X-Ray Spectra 
> calculate_spectrum(filename)
## open mpi 
Either follow this guide https://www.researchgate.net/post/Is_there_research_about_parallelisation_efficiency_using_ORCA 
or do the following: 
shell$ gunzip -c openmpi-4.0.5.tar.gz | tar xf -
shell$ cd openmpi-4.0.5
shell$ ./configure --prefix=/usr/local
<...lots of output...>
shell$ make all install```

## Setting path 

echo 'export PATH=path-to-ORCA:$PATH; 
export LD_LIBRARY_PATH=path-to-ORCA:$LD_LIBRARY_PATH'  
> ~/.bash_profile

>source ~/.bash_profile```

## Common Errors 
* Underscore in loaded xyz file. 
* did not escape new_line in xyz-file.
* wrong relative path in xyz file (always think from the directory of execution)
#Chemical Data Manipulation 
Required software packages are: StringIO, nglview, RDKit, pybel. 
T install all required packages install Conda or best the whole Anaconda distribution. 
run the following commands: 
pip3 install requirements.txt
conda update pip
conda install -c conda-forge openbabel
conda install -c conda-forge rdkit
conda install -c conda-forge  nglview```

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

The idea though, is to extract the RDKit extension out of the directory and
use it on any server. Look in conda envs there it should be after running 
> conda install -c rdkit rdkit-postgresql

# Pymatgen 
Pymatgen is a python library for chemoinformatics built to last. 
The documnetation can be accessed via this link https://pymatgen.org/. 
There is a paper about the library (https://doi.org/10.1016/j.commatsci.2012.10.028).
Installation of Pymatgen is done via the command: 
>conda install --channel conda-forge pymatgen

Prior to get access to the database via pymatgen set your API key
>pmg config --add PMG_MAPI_KEY <API-Key>

Check out examples on GitHub: 
>https://github.com/materialsvirtuallab/matgenb/tree/master/notebooks

# Interesting Chemistry Projects
* IBMRxns
* https://www.nature.com/sdata/policies/repositories
* https://www.iochem-bd.org/
* https://nomad-lab.eu/index.php?page=repo-arch
+ https://www.ebi.ac.uk/chembl/

# Distributed Computing 

+ https://www.freecodecamp.org/news/a-thorough-introduction-to-distributed-systems-3b91562c9b3c/

# GPU 
* http://practicalcheminformatics.blogspot.com/2020/06/wicked-fast-cheminformatics-with-nvidia.html
# Error on cluster
* Parallelisation is buggy. Posted on forum: https://orcaforum.kofo.mpg.de/viewtopic.php?f=11&t=6633
* copy pasting stuff into vim is not a joke okay? Don't use too many lines, take care you copy everything (yeah thats 
right). Doesn't happen with automation, though

# Algorithms and nice libraries 
* Symmetrizer (symmetry detection) https://onlinelibrary.wiley.com/doi/full/10.1002/jcc.22995
* cclib to read out atomic orbitals (https://cclib.github.io/index.html)
# Cited Works 

Hai Nguyen, David A Case, Alexander S Rose; NGLview - Interactive molecular graphics for Jupyter notebooks, Bioinformatics, , btx789, https://doi.org/10.1093/bioinformatics/btx789
>  @software{mendeleev2014,
    author = {Mentel, Łukasz},
    title = {{mendeleev} -- A Python resource for properties of chemical elements, ions and isotopes},
    url = {https://github.com/lmmentel/mendeleev},
    version = {0.3.6},
    date = {2014--},
}
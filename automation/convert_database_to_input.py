import pandas as pd
import numpy as np

def convert_json_database_to_input(database_path,
                                   type_of_geometry_opt,
                                   type_of_calculation,
                                   path_to_input_files,
                                   test=False):
    """
    converts a database with xyz to input files with specified commands. The method extracts a xyz file from the
    database and saves it. It then writes a input file for a geometry opt and then an input file for the actual
    calculation specified in type_of_calculation

    :param database_path: path to database
    :param type_of_geometry_opt: specifies the geometry optimisation method
    :param type_of_calculation: specifies the command as a string
    :param path_to_input_files: path to the folder containing the input files
    :param boolean, if true only does it for 10 entries of the database

    :return: None
    """
    df_database  = pd.read_json(database_path, orient='split')
    xyz_coordinates = df_database["xyz_pbe_relaxed"].tolist()
    ref_codes = df_database["refcode_csd"].tolist()
    body_line = "* xyzfile 0 1 "+path_to_input_files+"/"
    seperator_line = "\n$new_job\n\n"
    if test:
        #writing xyz
        for i in range(10):
            content=[xyz_coordinates[i]]
            write_file("../Inputs/" + ref_codes[i] + "db.xyz", content)

        #writing geometry_optimisation_input
        for i in range(10):
            content = [type_of_geometry_opt, body_line+ref_codes[i]+"db.xyz\n",
                       seperator_line, type_of_calculation, body_line+ref_codes[i]+".xyz\n"]
            write_file("../Inputs/" + ref_codes[i] + ".inp", content)
    else:
        #writing xyz
        for i in range(len(df_database)):
            content=[xyz_coordinates[i]]
            write_file("../Inputs/" + ref_codes[i] + "db.xyz", content)

        #writing geometry_optimisation_input
        for i in ragne(len(df_database)):
            content = [type_of_geometry_opt, body_line+ref_codes[i]+"db.xyz\n"]
            write_file("../Inputs/" + ref_codes[i] + ".inp", content)


def write_file(filename: str, content:list):
    """
    Writes a file with content specified in the passed list
    :param filename: name of the file
    :param content: list with content
    :return:
    """
    file = open(filename, "w")
    for line in content:
        file.write(line)
    file.close()

def make_input(header, body, filename):
    """

    :param header: string or list of strings with header commands
    :param body: string with body commands
    :param body: string with file_name
    :return:
    """
    content=[header, body]
    write_file(filename, content)

if __name__ == "__main__":
    path_to_input_files ="Inputs"
    database_path ="../databases/df_62k.json"
    type_of_geometry_opt=""""%pal nprocs 8 end
                         ! TPSS def2-SVP  opt\n\n"""
    type_of_calculation="""%pal nprocs 8 end
    
    ! UKS B3LYP ZORA-def2-TZVP def2/J RIJCOSX TightSCF Grid5 ZORA
# Increasing the DFT grid accuracy on molybdenum (atom number 42)
%method SpecialGridAtoms 42
SpecialGridIntAcc 7
end
%tddft
        orbwin[0] = 0,0,-1,-1 # Selecting the alpha set (orbwin[0]). Selecting donor orbital range : 0 to 0 (Mo 1s orbital only) and acceptor orbital range: -1 to -1 (meaning all virtual orbitals)
        orbwin[1] = 0,0,-1,-1 # Selecting the beta set in the same way as the alpha set. Not necessary if system is closed-shell.
        doquad true # Calculate quadrupole contributions.
        nroots 60 # Setting the number of roots (transitions) to be calculated.
        maxdim 10 # Setting the scaling of maximum dimension of the expansion space.
end
* xyzfile 0 1
    """
    test = True
    convert_json_database_to_input(database_path=database_path, type_of_geometry_opt=type_of_geometry_opt,
                                   path_to_input_files = path_to_input_files,
                                   type_of_calculation=type_of_calculation, test=test)
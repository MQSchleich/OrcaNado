import pandas as pd
import numpy as np


class Input:
    """

    """

    def __init__(self):
        pass

    def start_position(self):



def convert_json_database_to_input(database_path:str,
                                   type_of_calculation:str,
                                   path_to_input_files:str,
                                   num_molecules = 30,
                                   multi_job = True,
                                   type_of_geometry_opt = None,
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
    body_line = "* xyzfile 0 1 "+path_to_input_files
    if multi_job:
        seperator_line = "\n$new_job\n\n"
    if not test:
        num_molecules= len(df_database)
    #writing xyz
    for i in range(num_molecules):
        content=[xyz_coordinates[i]]
        write_file("../Inputs/" + ref_codes[i] + "db.xyz", content)

    #writing geometry_optimisation_input
    for i in range(num_molecules):
        if multi_job:
            content=[type_of_geometry_opt,
                      body_line + ref_codes[i] + "db.xyz\n",
                      seperator_line,
                      type_of_calculation,
                      body_line + ref_codes[i] + ".xyz\n"]
            write_file("../Inputs/" + ref_codes[i] + ".inp", content)
        else:
            content=[type_of_calculation,
                      body_line + ref_codes[i] + "db.xyz\n"]
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
    path_to_input_files =""
    database_path ="../databases/df_62k.json"
    type_of_geometry_opt="""%pal nprocs 8 end
 ! TPSS def2-SVP  opt\n\n"""
    type_of_calculation="""% nprocs 8 end\n
!B3LYP ZORA-def2-TZVP RIJCOSX Grid5 ZORA GRIDX6 D3BJ ABC



%tddft
orbwin[0] = 0,0,-1,-1		# donor orbital range : 0 to 0
				# (C 1s orbital only) 
                     		# acceptor orbital range: -1 to -1
				# (meaning all virtual orbitals)

orbwin[1] = 0,0,-1,-1		# Not necessary if system is closed-shell.

doquad true 			# Calculate quadrupole contributions.

nroots 50 			# Setting the number of roots (transitions)
				# to be calculated.

maxdim 300 			# Setting the maximum dimension of the expansion space.
				# Should be 5-10 times the no. of nroots for
				# favorable convergence.
MaxCore 1024
end

%method
D3S6 1.0000
D3A1 0.3981
D3S8 1.9889
D3A2 4.4211
end
%method
ScalHFX     = 0.57
ScalDFX     = 0.35
end

%output
print[p_mos] true
print[p_basis] 5
end"""
    test = True
    convert_json_database_to_input(database_path=database_path,
                                   type_of_calculation=type_of_calculation,
                                   path_to_input_files=path_to_input_files,
                                   num_molecules=168,
                                   multi_job=False,
                                   test=test)
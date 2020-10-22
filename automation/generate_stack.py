import os
import automation.convert_database_to_input as db

def make_batch(num_cores:int,
               num_molecules,
               database_path,
               type_of_geometry_opt,
               type_of_calculation,
               path_to_input_files):
    """
    makes a batch of molecules for a node
    has to do:
    1.) Collect num molecules in input file
    2.) Set paths for cluster correctly
    3.) Best: Stay within time limit
    4.) Make Zip_files of the necessary files
    :param num_cores: Set cores
    :param num_molecules: set number of molecules/per batch
    :param database_path: path to
    :param type_of_geometry_opt:
    :param type_of_calculation:
    :param path_to_input_files:
    :return:
    """
    pass

def test_optimal_cores(max_cores:int = 64,
                       inputs:list = None,
                       write_path:str ="../Inputs/OptimisationCores/testCores.inp"):
    """
    creates a test file to evaluate the optimal cores
    :param max_cores: number_of_cores
    :param sample: name_of_sample
    :return:
    """
    os.system("mkdir -p ../Inputs/OptimisationCores")
    content = []
    seperator_line = "\n$new_job\n\n"
    for i in range(max_cores):
        if i == 0:
            for input in inputs:
                content+=[input, seperator_line]
        else:
            header = f"% pal nprocs {i} end\n"
            for input in inputs:
                content += [header, input, seperator_line]
    db.write_file(write_path, content)


if __name__ == "__main__":
    input_1 = """!TPSS def2-SVP Grid4 TightSCF RIJCOSX autoaux TightOPT D3BJ ABC

%method

D3S6 1.0000  # Parameters for D3BJ: Becke Jones Dampening
D3A1 0.3768
D3S8 1.2576
D3A2 4.5865
end

* xyzfile 0 1 ABAFEQdb.xyz

"""
    input_2 = """
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
* xyzfile 0 1 ABAFEQ.xyz"""
    test_optimal_cores(max_cores = 30, inputs = [input_1, input_2])


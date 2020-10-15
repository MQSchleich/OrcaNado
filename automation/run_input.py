import os
from automation.clean_files import clean_files

def run_input(path_to_orca, path_to_input, path_to_output, output_folder):
    """
    runs any input
    :param path_to_input:
    :param path_to_output:
    :return:
    """
    os.system(path_to_orca + " " + path_to_input + "> " + path_to_output)
    #clean_files(path_to_input, path_to_output_folder=output_folder)

if __name__ == "__main__":
    path_to_orca="~/Library/Orca421/orca"
    path_to_input="../Inputs/BITCEM13.inp"
    path_to_output="../Inputs/BITCEM13.out"
    run_input(path_to_orca, path_to_input, path_to_output, output_folder = "../Outputs")
    #clean_files(path_to_orca, path_to_input, path_to_output)

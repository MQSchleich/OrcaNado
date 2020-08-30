from Automation.run_input import run_input
from Automation.clean_files import clean_files
import os

def run_ts_search(path_to_orca, path_to_input, path_to_output):
    """
    Performs transistion state search on input file and cleans up files
    :param path_to_orca:
    :param path_to_input:
    :param path_to_output:
    :return:
    """
    run_input(path_to_orca, path_to_input, path_to_output)
    clean_files(path_to_input)

if __name__ == "__main__":
    path_to_orca="~/Library/Orca421/orca"
    path_to_input="../Inputs/Sn2.inp"
    path_to_output="../Outputs/Sn2.out"
    run_ts_search(path_to_orca, path_to_input, path_to_output)
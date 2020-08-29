import os

def run_input(path_to_orca, path_to_input, path_to_output):
    """

    :param path_to_input:
    :param path_to_output:
    :return:
    """
    os.system(path_to_orca+" "+ path_to_input+ "> "+ path_to_output)

if __name__ == "__main__":
    path_to_orca = "~/Library/Orca421/orca"
    path_to_input = "../Inputs/co.inp"
    path_to_output = "../Outputs/co.out"
    run_input(path_to_orca, path_to_input, path_to_output)
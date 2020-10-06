import os
from Automation.clean_files import clean_files

def run_input(path_to_orca, path_to_input, path_to_output):
    """

    :param path_to_input:
    :param path_to_output:
    :return:
    """
    os.system("sudo "+path_to_orca + " " + path_to_input + "> " + path_to_output)


if __name__ == "__main__":
    path_to_orca="~/Library/Orca421/orca"
    path_to_input="../Outputs/NuSubst_Opt/NucleophilicSubstitionCarbonyl_prod_opt.inp"
    path_to_output="../Outputs/NuSubst_Opt/NucleophilicSubstitionCarbonyl_prod_opt.out"
    run_input(path_to_orca, path_to_input, path_to_output)
    #clean_files(path_to_orca, path_to_input, path_to_output)

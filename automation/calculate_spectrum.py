import os
import automation.run_input as run_input
import automation.clean_files as clean_files

def calculate_spectrum(path_to_orca,
                       path_to_input,
                       path_to_output,
                       output_folder = "Output",
                       command= " ABSQ -eV -x0100 -x1900 -w25.0 -n500"):
    """
    function to calculate spectra, it is just a small variation of the input calculation
    :param path_to_orca:
    :param path_to_input:
    :param path_to_output:
    :param output_folder:
    :return: None
    """
    run_input.run_input(path_to_orca, path_to_input, path_to_output, output_folder)
    make_spectrum(path_to_orca, path_to_output, command)
    clean_files.clean_files(path_to_input, output_folder)





def make_spectrum(path_to_orca,
                  path_to_output,
                  command =  " ABSQ -eV -x0100 -x1900 -w25.0 -n500"):
    """
    makes the spectrum specified in the command
    :return: none
    """
    os.system(path_to_orca+"_mapspc "+path_to_output+command)


def plot_spectrum(path_to_spectrum):
    """
    plots a spectrum and saves file as png with 300 dpi
    :param path_to_spectrum: path to the saved spectrum
    :return: none
    """
    pass
    #TODO: Implement the spectrum saving as png

if __name__ == "__main__":
    path_to_orca="~/Library/Orca421/orca"
    path_to_input="../Inputs/methane.inp"
    path_to_output = "../Outputs/methane/methane.out"
    make_spectrum(path_to_orca=path_to_orca, path_to_output=path_to_output)
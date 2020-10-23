import os
import clean_files as clean_files


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
    try:
        run_input(path_to_orca, path_to_input, path_to_output, output_folder)
        make_spectrum(path_to_orca, path_to_output, command)
        make_spectrum(path_to_orca, path_to_output, command=" IR -x0300 -x14000")
        clean_files.clean_files(path_to_input, output_folder)
    except:
        RuntimeError




def make_spectrum(path_to_orca,
                  path_to_output,
                  command =  " ABSQ -eV -x0100 -x1900 -w25.0 -n500"):
    """
    makes the spectrum specified in the command
    :return: none
    """
    os.system(path_to_orca+"_mapspc "+path_to_output+command)


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
    path_to_input="../Inputs/methane.inp"
    path_to_output = "../Outputs/methane"
    calculate_spectrum(path_to_orca=path_to_orca, path_to_input = path_to_input, path_to_output=path_to_output)
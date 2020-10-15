import os

def make_spectrum(path_to_output,
                  command = "res.out ABSQ -eV -x0100 -x1900 -w25.0 -n500") :
    """
    makes the spectrum specified in the command
    :return: none
    """
    os.system(path_to_output+command)


def plot_spectrum(path_to_spectrum):
    """
    plots a spectrum and saves file as png with 300 dpi
    :param path_to_spectrum: path to the saved spectrum
    :return: none
    """
    pass
    TODO: Implement the spectrum
###File For Plotting Spectra####

import matplotlib.pyplot as plt 
import re
import os

#Functions
def plot_spectra(file_name): 
    """
    Base function to generate a python plot of the calculted X-Ray spectra after the orca command
    :return: 
    """
    x_vals = []
    y_vals = []
    base_name = os.path.basename(file_name)
    id = re.search("[a-zA-Z0-9][^\.]+", base_name).group()
    print(base_name)
    with open(file_name, "r") as file:
        for line in file: 
            line_string = re.findall("[0-9\.]+", line)
            x_vals.append(float(line_string[0]))
            y_vals.append(float(line_string[1]))
    plt.plot(x_vals, y_vals)
    plt.xlabel("eV")
    plt.ylabel("Intensity")
    plt.savefig("../Spectra/"+id+".png", dpi=300)
    os.system("cp " + file_name + " ../Spectra/"+base_name)


if __name__ == "__main__": 
    plot_spectra("../Outputs/methane.absq.dat")
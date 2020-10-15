import automation.run_input as run_input
import automation.calculate_spectrum as calculate_spectra
import databases
# here every routine should be run
#TODO Command line Arguments with argparser https://stackabuse.com/command-line-arguments-in-python/

if __name__ == "__main__":
    path_to_orca="~/Library/Orca421/orca"
    path_to_input="Inputs/methane.inp"
    path_to_output="Inputs/methane.out"
    path_to_output_folder ="Outputs"
    #run_input.run_input(path_to_orca, path_to_input, path_to_output, path_to_output_folder)
    calculate_spectra.calculate_spectrum(path_to_orca, path_to_input, path_to_output, path_to_output_folder)

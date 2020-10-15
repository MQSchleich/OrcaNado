import automation.run_input as run_input
import databases

if __name__ == "__main__":
    path_to_orca="~/Library/Orca421/orca"
    path_to_input="Example_Production/methane.inp"
    path_to_output="Example_Production/methane.out"
    path_to_output_folder ="Outputs"
    run_input.run_input(path_to_orca, path_to_input, path_to_output, path_to_output_folder)
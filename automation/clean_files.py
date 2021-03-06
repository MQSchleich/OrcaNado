import os
from re import search

def clean_files(input_path, path_to_output_folder):
    """
    Cleans input files
    :param input_path: name of input file
    :return: None
    """
    #TODO write code to check what is the input folder and what is the output folder
    file_name = os.path.split(input_path)[-1]
    search_string = file_name.split(".")[0]
    files = []
    os.system("mkdir -p " + path_to_output_folder+"/"+search_string)
    for (dirpath, dirnames, filenames) in os.walk("Inputs"):
        files.extend(filenames)
    for file in files:
        print(file)
        if search(search_string, file) and file != file_name:
            os.system("mv Inputs/"+file+" Outputs/"+search_string)

if __name__ == "__main__":
    file_name = clean_files("../Inputs/methane.inp", "../Outputs")
    print(file_name)
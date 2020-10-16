
def set_up_queue(path_to_orca,
                       path_to_input,
                       path_to_output,
                       output_folder = "Output",
                       command= " ABSQ -eV -x0100 -x1900 -w25.0 -n500"):
    """

    :param path_to_orca: orca path
    :param path_to_inputs:
    :param path_to_outputs:
    :param output_folder:
    :param command:
    :return:
    """
    #TODO just set-up a list with input files, iterate over input files and ignore errors at the moment
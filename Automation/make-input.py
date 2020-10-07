from Automation.write_file import write_file


def make_input(header, body, filename):
    """

    :param header: string or list of strings with header commands
    :param body: string with body commands
    :param body: string with file_name
    :return:
    """
    content=[header, body]
    write_file(filename, content)
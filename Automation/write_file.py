def write_file(filename: str, content:list):
    """
    Writes a file with content specified in the passed list
    :param filename: name of the file
    :param content: list with content
    :return:
    """
    file = open(filename, "w")
    for line in content:
        file.write(line)
    file.close()
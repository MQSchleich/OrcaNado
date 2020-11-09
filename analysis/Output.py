class Output:
    def __init__(self, file_path):
        self.file_path=file_path

    def load_job(self):
        file = load_file(self)


    def load_file(self):
        file=open(self.file_path, "r")
        return file
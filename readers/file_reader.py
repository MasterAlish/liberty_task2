import os


class FilesReader:
    def __init__(self, files_dir):
        self.files_dir = files_dir

    def __iter__(self):
        for file_name in os.listdir(self.files_dir):
            with open(os.path.join(self.files_dir, file_name)) as file:
                yield file.read()

import os
from typing import List

class FileGenerator:

    fileName: str
    fileDirectory: str

    def __init__(self, filename: str):
        self.fileName = filename
        self.fileDirectory = os.getcwd()

    def generateFile(self, tags: List[str]):
        pass
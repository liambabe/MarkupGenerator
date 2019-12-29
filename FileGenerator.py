import os
from typing import List

class FileGenerator:

    fileName: str
    fileDirectory: str

    def __init__(self, filename: str):
        self.fileName = filename
        self.fileDirectory = os.getcwd()

    def generateFile(self, tags: List[str]):
        filePath = os.path.join(self.fileDirectory, self.fileName)

        with open(filePath, "w") as fileWriter:
            for tag in tags:
                line = "<" + tag.rstrip() + ">" + "\n"
                fileWriter.write(line)

            for tag in reversed(tags):
                line = "</" + tag.rstrip() + ">" + "\n"
                fileWriter.write(line)
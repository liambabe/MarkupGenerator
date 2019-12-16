from typing import List
from os import walk

class TemplateParser:

    tags: List[str]
    templateFolder: str
    templatePath: str
    fileExtension: str

    def __init__(self):
        self.templateFolder = "Templates/"
        self.fileExtension = ".csv"

    #parse csv template into list of strings
    def parse(self, fileName) -> List[str]:
        self.templatePath = self.templateFolder + fileName + self.fileExtension
        file = open(self.templatePath, "r")
        self.tags = file.read().split(",")

        return self.tags

    #return list of all templates avaliable
    def getFileList(self) -> List[str]:
        (_, _, filenames) = next(walk(self.templateFolder))
        
        return filenames

from typing import List

class TemplateParser:

    tags: List[str]
    templateFolder: str
    templatePath: str
    fileExtension: str

    def __init__(self):
        self.templateFolder = "Templates/"
        self.fileExtension = ".csv"

    def parse(self, fileName):
        self.templatePath = self.templateFolder + fileName + self.fileExtension
        file = open(self.templatePath, "r")
        self.tags = file.read().split(",")

        return self.tags



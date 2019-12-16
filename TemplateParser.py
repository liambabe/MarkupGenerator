class TemplateParser:

    tags = []
    templateFolder = ""
    templatePath = ""

    def __init__(self):
        self.templateFolder = "Templates/"

    def parse(self, fileName):
        self.templatePath = self.templateFolder + fileName
        file = open(self.templatePath, "r")
        self.tags = file.read().split(",")

        return self.tags



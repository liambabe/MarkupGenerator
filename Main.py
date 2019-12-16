from TemplateParser import TemplateParser
from FileGenerator import FileGenerator

templateParser = TemplateParser()
fileGenerator = FileGenerator()

print(templateParser.parse("basicHtml"))
print(templateParser.getFileList())
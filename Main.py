import sys
from TemplateParser import TemplateParser
from FileGenerator import FileGenerator

arguments = len(sys.argv) - 1

#if invalid arguements stop before any processing
if not (1 <= arguments <= 2):
    print("Invalid Arguements")
    exit()

templateParser = TemplateParser()
templateList = templateParser.getFileList()

#helper functions
def printList():
    for template in templateList:
        print(template)

def printHelp():
    pass

#if helper methods called
if arguments == 1:
    userInput = sys.argv[1]

    if userInput == "li" or userInput == "list":
        printList()
    elif userInput == "h" or userInput == "help":
        printHelp()

#main generation calling code
else:
    userInput = sys.argv[1]
    fileName = sys.argv[2]

    fileGenerator = FileGenerator(fileName)
    tags = templateParser.parse(userInput)

    fileGenerator.generateFile(tags)
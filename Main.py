import sys
from TemplateParser import TemplateParser
from FileGenerator import FileGenerator

arguments = len(sys.argv) - 1

if arguments != 1:
    print("Invalid Arguements")
    exit()

userInput = sys.argv[1]

templateParser = TemplateParser()
fileGenerator = FileGenerator()
templateList = templateParser.getFileList()

def printList():
    for template in templateList:
        print(template)

def printHelp():
    pass

print(userInput)

if userInput == "list":
    printList()
elif userInput == "help":
    pass
elif userInput == "close":
    pass
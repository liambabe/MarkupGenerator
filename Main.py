import sys
from TemplateParser import TemplateParser
from FileGenerator import FileGenerator

arguments = len(sys.argv) - 1

if arguments != 2:
    print("Invalid Arguements")
    exit()

userInput = sys.argv[1]
fileName = sys.argv[2]

templateParser = TemplateParser()
fileGenerator = FileGenerator(fileName)
templateList = templateParser.getFileList()

def printList():
    for template in templateList:
        print(template)

def printHelp():
    pass

print(userInput)

if userInput == "li" or userInput == "list":
    printList()
elif userInput == "h" or userInput == "help":
    printHelp()
else:
    pass
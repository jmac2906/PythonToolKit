import string
# Removes String Between two Characters (non inclusive) In File
def RemoveStringBetweenCharactersInFile(fileToOpen, firstCharacter, secondCharacter, outputFileName):
    with open(fileToOpen, "r+") as infile:
        with open(outputFileName, "w") as outfile:
            for line in infile:
                if firstCharacter in line:
                    removeString = str(line[line.index(firstCharacter):line.index(secondCharacter)])
                    line = string.replace(line, removeString, "")
                outfile.write(line)

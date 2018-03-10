def extract_all_strings_between_2_characters(File_to_extract_strings_from, beginningOfDesiredString, endOfDesiredString):
    with open(File_to_extract_strings_from) as Inputfile:
        outputList =[]
        for line in Inputfile.read().strip().split(endOfDesiredString):
            if line.find(beginningOfDesiredString) >= 0:
                outputList.append(line[line.index(beginningOfDesiredString):len(line)])
        return outputList


#extract_all_strings_between_2_characters()

#The war is everlasting. 
#This is the phrase which is written in the text file at the moment.
import string
def wordDefiner():
    infile = open("wordsToDefine.txt", "r")
    outfile = open("wordsAndTheirDefinitions", "w")
    wordsAndTheirDefinitions = dict()
    sectionsInLine = list()
    for line in infile:
        line = line.rstrip()
        line = line.lower()
        line = line.translate(str.maketrans('', '', string.punctuation))
        sectionsInLine = line.split(" ")
        for element in sectionsInLine:
            wordsAndTheirDefinitions[element] = ""
        print(wordsAndTheirDefinitions)
    for key in wordsAndTheirDefinitions:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{key}"
        print(f"{url}")

wordDefiner()

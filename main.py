#The war is everlasting. 
#This is the phrase which is written in the text file at the moment.
import string
import requests

def wordSaverFromFileToDict():
    infile = open("wordsToDefine.txt", "r")
    wordsAndTheirDefinitions = dict()
    sectionsInLine = list()
    for line in infile:
        line = line.rstrip()
        line = line.lower()
        line = line.translate(str.maketrans('', '', string.punctuation))
        sectionsInLine = line.split(" ")
        for element in sectionsInLine:
            wordsAndTheirDefinitions[element] = ""
    infile.close()
    return wordsAndTheirDefinitions

def wordDefiner(dictionary):
    wordsNotFound = list()
    outfile = open("wordsAndTheirDefinitions", "w")
    for key in dictionary:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            meaning = data[0]["meanings"][0]["definitions"][0]["definition"]
            dictionary[key] = meaning
            outfile.write(f"{key}: {meaning}\n")
            print(f"{key}: {meaning}")

        else:
            print("It appears that it isn't defined in the dictionary API.")
            wordsNotFound.append(key)
            continue
        print("\n") 
    print("Here are the words that we couldn't find")
    for notFoundWords in wordsNotFound:
        print(f"{notFoundWords}")
    outfile.write(f"Here are the words that we couldn't find:\n\n")
    for notFoundWords in wordsNotFound:
        outfile.write((f"{notFoundWords}\n"))

wordsDict = wordSaverFromFileToDict()
wordDefiner(wordsDict)

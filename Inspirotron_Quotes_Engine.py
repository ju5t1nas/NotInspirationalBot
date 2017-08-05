import random
from Inspirotron_Formating_Quotes import newlineAfterPunctuation, specialNewlineOperator, findLongestLineAndNumberOfLines

def getAQuote():
    quoteFile = open("Words and Phrases/Quotes.txt", "r")
    line = quoteFile.readlines()[random.randint(0, linecount("Words and Phrases/Quotes.txt"))]
    quote, wordsWanted = line.split(';', 2)
    fullQuote = quote % whatToPutIn(getRequiredWords(whatWordsAreRequired(wordsWanted)[0]), whatWordsAreRequired(wordsWanted)[1])
    longestLineAndNumberOfLines = findLongestLineAndNumberOfLines(fullQuote)
    fullQuote = newlineAfterPunctuation(fullQuote)
    fullQuote = specialNewlineOperator(fullQuote)
    return [fullQuote, longestLineAndNumberOfLines]

def linecount(filePath):
    with open(filePath) as f:
        for i, l in enumerate(f):
            pass
    return i

def whatWordsAreRequired(requirementsString):
    wordcount = 0

    verb1 = False
    verb2 = False
    verb3 = False
    if "verb" in requirementsString:
        if "verb1" in requirementsString:
            verb1 = True
            wordcount += 1
        if "verb2" in requirementsString:
            verb2 = True
            wordcount += 1
        if "verb3" in requirementsString:
            verb3 = True
            wordcount += 1

    noun1 = False
    noun2 = False
    noun3 = False
    if "noun" in requirementsString:
        if "noun1" in requirementsString:
            noun1 = True
            wordcount += 1
        if "noun2" in requirementsString:
            noun2 = True
            wordcount += 1
        if "noun3" in requirementsString:
            noun3 = True
            wordcount += 1

    adjective1 = False
    adjective2 = False
    adjective3 = False
    if "adjective" in requirementsString:
        if "adjective1" in requirementsString:
            adjective1 = True
            wordcount += 1
        if "noun2" in requirementsString:
            adjective2 = True
            wordcount += 1
        if "noun3" in requirementsString:
            adjective3 = True
            wordcount += 1


    return [[[noun1, noun2, noun3],[verb1, verb2, verb3,],[adjective1, adjective2, adjective3]], wordcount]

def getRequiredWords(whatToGetList):

    wordList = [[None, None, None],[None, None, None],[None, None, None]]

    if True in whatToGetList[0]:
        nounFile = open("Words and Phrases/nouns.txt")
        noun1 = nounFile.readlines()[random.randint(0, linecount("Words and Phrases/nouns.txt"))]
        noun1 = noun1[:-1]
        nounFile.close()

        nounFile = open("Words and Phrases/nouns.txt")
        noun2 = nounFile.readlines()[random.randint(0, linecount("Words and Phrases/nouns.txt"))]
        noun2 = noun2[:-1]
        nounFile.close()

        nounFile = open("Words and Phrases/nouns.txt")
        noun3 = nounFile.readlines()[random.randint(0, linecount("Words and Phrases/nouns.txt"))]
        noun3 = noun3[:-1]
        nounFile.close()

        if whatToGetList[0][0] == True:
            wordList[0][0] = noun1
        if whatToGetList[0][1] == True:
            wordList[0][1] = noun2
        if whatToGetList[0][2] == True:
            wordList[0][2] = noun3


    if True in whatToGetList[1]:
        verbFile = open("Words and Phrases/verbs.txt")
        verb1 = verbFile.readlines()[random.randint(0, linecount("Words and Phrases/verbs.txt"))]
        verb1 = verb1[:-1]
        verbFile.close()

        verbFile = open("Words and Phrases/verbs.txt")
        verb2 = verbFile.readlines()[random.randint(0, linecount("Words and Phrases/verbs.txt"))]
        verb2 = verb2[:-1]
        verbFile.close()

        verbFile = open("Words and Phrases/verbs.txt")
        verb3 = verbFile.readlines()[random.randint(0, linecount("Words and Phrases/verbs.txt"))]
        verb3 = verb3[:-1]
        verbFile.close()

        if whatToGetList[1][0] == True:
            wordList[1][0] = verb1
        if whatToGetList[1][1] == True:
            wordList[1][1] = verb2
        if whatToGetList[1][2] == True:
            wordList[1][2] = verb3


    if True in whatToGetList[2]:
        adjectiveFile = open("Words and Phrases/adjectives.txt")
        adjective1 = adjectiveFile.readlines()[random.randint(0, linecount("Words and Phrases/adjectives.txt"))]
        adjectiveFile.close()

        adjectiveFile = open("Words and Phrases/adjectives.txt")
        adjective2 = adjectiveFile.readlines()[random.randint(0, linecount("Words and Phrases/adjectives.txt"))]
        adjectiveFile.close()

        adjectiveFile = open("Words and Phrases/adjectives.txt")
        adjective3 = adjectiveFile.readlines()[random.randint(0, linecount("Words and Phrases/adjectives.txt"))]
        adjectiveFile.close()

        if whatToGetList[2][0] == True:
            wordList[2][0] = adjective1
        if whatToGetList[2][1] == True:
            wordList[2][1] = adjective2
        if whatToGetList[2][2] == True:
            wordList[2][2] = adjective3


    return wordList

def whatToPutIn(wordList, wordcount):
    word1 = None
    word2 = None
    word3 = None
    counter = 0

    if wordcount == 1:
        for i in range(3):
            for j in range(3):
                if wordList[i][j] != None:
                    word1 = wordList[i][j]
        return (word1)

    if wordcount == 2:
        for i in range(3):
            for j in range(3):
                if wordList[i][j] != None and counter == 0:
                    word1 = wordList[i][j]
                    counter += 1
                if wordList[i][j] != None and counter == 1:
                    word2 = wordList[i][j]
        return (word1, word2)
    if wordcount == 3:
        for i in range(3):
            for j in range(3):
                if wordList[i][j] != None and counter == 0:
                    word1 = wordList[i][j]
                    counter += 1
                if wordList[i][j] != None and counter == 1:
                    word2 = wordList[i][j]
                    counter += 1
                if wordList[i][j] != None and counter == 2:
                    word3 = wordList[i][j]
        return (word1, word2, word3)


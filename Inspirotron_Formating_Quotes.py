def newlineAfterPunctuation(inputStr):
    finalStr = ""
    for i in range(len(inputStr)):
        finalStr += inputStr[i]
        if inputStr[i] == "," or inputStr[i] == "." or inputStr[i] == "!" or inputStr[i] == "?" or inputStr[i] == ":":
            finalStr += "\n"
        if inputStr[i-1] == "," or inputStr[i-1] == "." or inputStr[i-1] == "!" or inputStr[i-1] == "?" or inputStr[i-1] == ":" and inputStr[i] == " ":
            finalStr = finalStr[0:-1]


    return finalStr

def specialNewlineOperator(inputStr):
    finalStr = ""
    for i in range(len(inputStr)):
        finalStr += inputStr[i]
        if inputStr[i] == "*":
            finalStr = finalStr[0:-1]
            finalStr += "\n"
        if inputStr[i-1] == "*" and inputStr[i] == " ":
            finalStr = finalStr[0:-1]

    return finalStr

def findLongestLineAndNumberOfLines(inputStr):
    LineLength = 0
    LongestLine = 0
    NumberOfLines = 0
    for i in range(len(inputStr)):
        if inputStr[i] != "," or inputStr[i] != "." or inputStr[i] != "!" or inputStr[i] != "?" or inputStr[i] != ":" or inputStr[i] != "*":
            LineLength += 1
        if inputStr[i] == "," or inputStr[i] == "." or inputStr[i] == "!" or inputStr[i] == "?" or inputStr[i] == ":" or inputStr[i] == "*":
            if LineLength >= LongestLine:
                LongestLine = LineLength
            LineLength = 0
            NumberOfLines += 1
        if i == len(inputStr) - 1 and LongestLine <= LineLength:
            LongestLine = LineLength
            NumberOfLines += 1
    return [LongestLine, NumberOfLines]



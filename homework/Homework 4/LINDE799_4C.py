#CSCI 1133 Homework 4
#Erik Lindeman
#4C
def merge2(sentence1,sentence2):
    spaces = 0
    word1 = [""]
    y = -1
    val = [[]]
    begin = False
    compute = True
    newsentence = ""
    curr = []
    sentence1 = sentence1.lower()
    finalString = ""
    while not(spaces == -1):
        spaces = sentence1.find(" ")
        y+=1
        if (begin == False):
            begin = True
        else:
            word1.append("")
        if not(spaces == -1):
            for x in range(0,spaces):
                word1[y] += sentence1[x]
            for a in range(spaces+1,len(sentence1)):
                newsentence += sentence1[a]
            sentence1 = newsentence
            newsentence = ""
    word1[y] = (sentence1)

    spaces = 0
    word2 = [""]
    y = -1
    val = [[]]
    begin = False
    compute = True
    newsentence = ""
    curr = []
    sentence2 = sentence2.lower()
    while not(spaces == -1):
        spaces = sentence2.find(" ")
        y+=1
        if (begin == False):
            begin = True
        else:
            word2.append("")
        if not(spaces == -1):
            for x in range(0,spaces):
                word2[y] += sentence2[x]
            for a in range(spaces+1,len(sentence2)):
                newsentence += sentence2[a]
            sentence2 = newsentence
            newsentence = ""
    word2[y] = (sentence2)
    if(len(word2)>=len(word1)):
        length = len(word1)
        two = True
    else:
        length = len(word2)
        two = False
    for x in range(0,length,2):
        finalString+= "{} ".format(word1[x])
        if not((x+1)==len(word1)):
            finalString+="{} ".format(word1[x+1])
        finalString+="{} ".format(word2[x])
        if not((x+1)==len(word2)):
            finalString+="{} ".format(word2[x+1])
    if(two):
        for x in range(length,len(word2)):
            finalString+="{} ".format(word2[x])
    else:
        for x in range(length,len(word1)):
            finalString+="{} ".format(word1[x])
    return finalString

#CSCI 1133 Homework 4
#Erik Lindeman
#4B
Go = True
while(Go):
    sentence = input("Enter a sentence: ")
    spaces = 0
    word = [""]
    y = -1
    val = [[]]
    begin = False
    compute = True
    newsentence = ""
    curr = []
    sentence = sentence.lower()
    while not(spaces == -1):
        spaces = sentence.find(" ")
        y+=1
        if (begin == False):
            begin = True
        else:
            word.append("")
        if not(spaces == -1):

            for x in range(0,spaces):
                word[y] += sentence[x]
            for a in range(spaces+1,len(sentence)):
                newsentence += sentence[a]
            sentence = newsentence
            newsentence = ""
    word[y] = (sentence)
    for z in range(0,len(word)):
        for x in range(0,len(curr)):
            if(curr[x] == word[z]):
                compute = False
        if(compute == True):
            curr.append(word[z])
            for x in range(0,len(word)):
                if(curr[z] == word[x]):
                    val[z].append(x)
            val.append([])

    for x in range(0,len(curr)):
        print(curr[x]+ " ",end='')
        for c in range(0,len(val[x])):
            if (c==(len(val[x])-1)):
                print("{} ".format(val[x][c]))
            else:
                print("{} ".format(val[x][c]),end='')
    go = input("Do you want to enter another sentence (Y/N)?")
    if(go == "Y"):
        Go = True
    else:
        Go = False

#CSCI 1133 Homework 7
#Erik Lindeman
#Problem 7C

def mine_file(fname):
    d = {}
    wordct = 0
    unique = []
    apostct=0
    coolwords = []
    coolvalue = []
    usedword = []
    cooldict = {}
    fileobj = open(fname,'r')
    currline = fileobj.readline()
    while not(currline == ""):
        newline = ""
        currline = currline.replace("-"," ")
        currline = currline.replace("—"," ")
        for x in currline:
            if(x.isalpha() or x == " " or x == "'"):
                newline+=x
        wordlist = newline.split(" ")

        print(wordlist)
        for x in range(0,len(wordlist)):
            currword = wordlist[x]
            currword = currword.lower()
            if not(currword == "" or currword == " "):
                if(currword in d):
                    d[currword]+=1
                else:
                    d[currword]=1
                if not(currword in unique):
                    unique.append(currword)
                if("'" in currword):
                    apostct+=1
                wordct += 1
        currline = fileobj.readline()

    print("Word Count: {}".format(wordct))
    print("Unique Word Count: {}".format(len(unique)))
    print("Apostrophe Word Count: {}".format(apostct))

    words = list(d.keys())
    for x in range(0,len(words)):
        if(d[words[x]] >= 5):
            coolwords.append(words[x])
            coolvalue.append(d[words[x]])
            cooldict[words[x]] = d[words[x]]
    coolvalue.sort()
    coolvalue.reverse()
    for y in range(0,len(coolvalue)):
        for x in range(0,len(coolwords)):
            if(cooldict[coolwords[x]] == coolvalue[y] and not(coolwords[x] in usedword)):
                print("{0}: {1}".format(coolwords[x],coolvalue[y]))
                usedword.append(coolwords[x])

    fileobj.close()

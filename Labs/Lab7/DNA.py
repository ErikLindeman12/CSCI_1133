DNA = input("Enter a DNA sequence: ")
listerino = []
done = False
b = 0
a = 0
while done == False:

    go = True
    newstring = ""
    a = DNA.find("ATG")
    if not(a == -1):
        x = a+3
        while x<len(DNA):
            newstring+=DNA[x]
            x+=1
        DNA = newstring
    else:
        done = True
    while go:
        start = DNA.find("TAG")
        if start%3 == 0:
            a = DNA.find("TAG")
            if not(a == -1):
                listerino.append("")
                for x in range(0,a):
                    listerino[b]+=DNA[x]
                newstring = ""
                for y in range(a+3,len(DNA)):
                    newstring += DNA[y]
                DNA = newstring
                b+=1
        else:
            start = DNA.find("TAA")
            if start%3 == 0:
                a = DNA.find("TAA")
                if not(a == -1):
                    listerino.append("")
                    for x in range(0,a):
                        listerino[b]+=DNA[x]
                    newstring = ""
                    for y in range(a+3,len(DNA)):
                        newstring += DNA[y]
                    DNA = newstring
                    b+=1
            else:
                start = DNA.find("TGA")
                if start%3 == 0:
                    a = DNA.find("TGA")
                    if not(a == -1):
                        listerino.append("")
                        for x in range(0,a):
                            listerino[b]+=DNA[x]
                        newstring = ""
                        for y in range(a+3,len(DNA)):
                            newstring += DNA[y]
                        DNA = newstring
                        b+=1
                else:
                    go = False

for x in range(0,len(listerino)):
    print("Gene {} {}".format(x+1,listerino[x]))

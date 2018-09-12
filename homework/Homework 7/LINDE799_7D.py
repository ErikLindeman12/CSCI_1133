#CSCI 1133 Homework 7
#Erik Lindeman
#Problem 7D

def crime_report(fnameCSV):
    fileobj = open(fnameCSV,'r')
    line = fileobj.readline()
    begin = True
    dtheft = {}
    dburg = {}
    drob = {}
    while not(line == ""):
        comma = line.split(",")
        if(begin):
            begin = False
        else:
            district = int(comma[2])
            descr = comma[5]
            descrlow = descr.lower()
            if("theft" in descrlow):
                if(district in dtheft):
                    dtheft[district] += 1
                else:
                    dtheft[district] = 1
            if("burglary" in descrlow):
                if(district in dburg):
                    dburg[district] += 1
                else:
                    dburg[district] = 1
            if("robbery" in descrlow):
                if(district in drob):
                    drob[district] += 1
                else:
                    drob[district] = 1
        line = fileobj.readline()
    fileobj.close()
    crimeobj = open("stealingOffenses.txt",'w')
    crimeobj.write("Burglaries by District:\n")
    keyslist = list(dburg.keys())
    for x in range(0,len(keyslist)):
        crimeobj.write("{0}: {1}\n".format(keyslist[x],dburg[keyslist[x]]))
    crimeobj.write("\n")

    crimeobj.write("Thefts by District:\n")
    keyslist = list(dtheft.keys())
    for x in range(0,len(keyslist)):
        crimeobj.write("{0}: {1}\n".format(keyslist[x],dtheft[keyslist[x]]))
    crimeobj.write("\n")

    crimeobj.write("Robberies by District:\n")
    keyslist = list(drob.keys())
    for x in range(0,len(keyslist)):
        crimeobj.write("{0}: {1}\n".format(keyslist[x],drob[keyslist[x]]))

    crimeobj.close()

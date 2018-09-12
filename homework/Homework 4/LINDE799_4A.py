#CSCI 1133 Homework 4
#Erik Lindeman
#4A
def two_sums(aList, target):
    stop = False
    go = True
    for a in range(0,len(aList)):
        if(not(type(target) is int) or not(type(aList[a]) is int)):
            go = False
    if(go == False):
        print("Can not compute due to invalid List/target given.")
    if(go):
        for x in range(0,len(aList)):
            firstVal = aList[x]
            for y in range(0,len(aList)):
                secondVal = aList[y]
                sumVals = firstVal+secondVal
                if((sumVals == target) and stop == False):
                    List = (firstVal,secondVal)
                    return List
                    stop = True

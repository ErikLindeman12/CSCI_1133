#CSCI 1133 Homework 5
#Erik Lindeman
#5A

def flattenList(aList):
    if((type(aList) == list) and(len(aList) == 0)):
        return []
    elif(type(aList[0]) == list):
        newList = aList[0]
        aList.remove(newList)
        return flattenList(newList)+flattenList(aList)
    else:
        newList = aList[0]
        actualValue = aList[:1]
        aList.remove(newList)
        return actualValue+flattenList(aList)

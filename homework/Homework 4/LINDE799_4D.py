#CSCI 1133 Homework 4
#Erik Lindeman
#4D
import LINDE799_4A
Go = True
while Go:
    move = False
    Move = False
    target = input("Input target: ")
    while not(move):
        if(target.isdigit()):
            if(target.find(".")==-1):
                target = int(target)
                move = True
            else:
                target = input("Target must be an integer.  Enter a valid target: ")
                Move = False
        else:
                target = input("Target must be an integer.  Enter a valid target: ")
                Move = False
    List = input("Input list of numbers seperated by a space: ")
    while not(Move):
        List = List.replace(" ","")
        aList = []
        for x in List:
            if(x.isdigit()):
                if(x.find(".")==-1):
                    aList.append(int(x))
                    Move = True
                else:
                    List = input("The list can only contain integers.  Enter a valid list: ")
                    Move = False
            else:
                List = input("The list can only contain integers.  Enter a valid list: ")
                Move = False
    answer = LINDE799_4A.two_sums(aList,target)
    print("The two numbers that sum up to {0} are {1} and {2}.".format(target,answer[0],answer[1]))
    go = input("Would you like to enter another list and target? (y/n): ")
    if(go == "n"):
        Go = False
    elif(go == "y"):
        Go = True
    else:
        print("Invalid response")
        Go = False

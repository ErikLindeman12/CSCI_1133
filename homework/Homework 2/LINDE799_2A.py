#CSCI 1133 Homework 2
#Erik Lindeman
#Problem A

def newFib(first,second,length):
    print("the first",length, "terms of the new series are: ")
    print(first, end=" ")
    print(second, end=" ")
    for x in range(0,length):
        newFirst = first
        newSecond = second
        first = newSecond
        second = newFirst+newSecond
        print(second, end=" ")

first = int(input("Enter the first term of the series: "))
second = int(input("Enter the second term of the series: "))
length = int(input("Enter the number of terms you want to see: "))
newFib(first,second,length)

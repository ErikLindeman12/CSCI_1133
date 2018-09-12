#CSCI 1133 Homework 3
#Erik Lindeman
#Problem C
def summation(lower,upper,typeSum):
    value = 0
    solvable = True
    for x in range(lower,upper+1):
        if(typeSum.lower() == "square"):
            value+=(x*x)
        if(typeSum.lower() == "cube"):
            value+=(x*x*x)
        if(typeSum.lower() == "inverse"):
            if(x == 0):
                solvable = False
            else:
                value+=1/x
    if(solvable):
        Solution = "The result of the summation is {}".format(value)
        print(Solution)
    else:
        print("The value is unable to be found due to dividing by zero.")

def main():
    lower = int(input("Enter a lower bound for summation: "))
    upper = int(input("Enter an upper bound for summation: "))
    typeSum = input("Enter a function to be summed (square, cube, inverse): ")
    summation(lower,upper,typeSum)

if  __name__  == '__main__':
    main()

#CSCI 1133 Homework 5
#Erik Lindeman
#5C

def factorial(terms):
    if(terms == 0):
        return 1
    else:
        return terms * factorial(terms-1)

def sinFun(angle,terms):
    newTerms = 2*terms-1
    if(terms == 0):
        return 0
    else:
        currNum = (angle**newTerms)/factorial(newTerms)
        if(terms%2 == 0):
            currNum *= -1
        return currNum + sinFun(angle,terms-1)

def main():
    angle = float(input("Enter the angle to approximate (in radians): "))
    terms = int(input("Enter the number of terms to compute: "))
    answer = sinFun(angle,terms)
    print("sin({0}) is approximately {1}".format(angle,answer))

if  __name__  == '__main__':
    main()

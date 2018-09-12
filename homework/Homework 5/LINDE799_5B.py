#CSCI 1133 Homework 5
#Erik Lindeman
#5B

def convert(decimal, base):
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    if(decimal//base == 0):
        remainder = decimal%base
        if(remainder <= 9):
            convertString = str(remainder)
        else:
            remainder-=10
            convertString = letters[remainder]
        return convertString
    else:
        remainder = decimal % base
        decimal = decimal//base
        if(remainder <= 9):
            convertString = str(remainder)
        else:
            remainder-=10
            convertString = letters[remainder]
        return convertString + convert(decimal,base)

def main():
    decimal = int(input("Enter your decimal number: "))
    base = int(input("Enter the base you want to convert to: "))
    conversion = convert(decimal,base)
    print("{0} in base {1} is {2}".format(decimal,base,conversion[::-1]))

if  __name__  == '__main__':
    main()

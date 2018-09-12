#CSCI 1133 Homework 7
#Erik Lindeman
#Problem 7A

class Complex:
    def __init__(self,real,imaginary):
        self.real = float(real)
        self.imaginary = float(imaginary)

    def __add__(self,rhand):
        newreal = self.real+rhand.real
        newimaginary = self.imaginary+rhand.imaginary
        return Complex(newreal,newimaginary)

    def __sub__(self,rhand):
        newreal = self.real-rhand.real
        newimaginary = self.imaginary-rhand.imaginary
        return Complex(newreal,newimaginary)

    def __mul__(self,rhand):
        newreal = (self.real*rhand.real-self.imaginary*rhand.imaginary)
        newimaginary = (self.real*rhand.imaginary+self.imaginary*rhand.real)
        return Complex(newreal,newimaginary)

    def __truediv__(self,rhand):
        a = self.real
        b = self.imaginary
        c = rhand.real
        d = rhand.imaginary
        if(((c**2)+(d**2)) == 0):
            return None
        newreal = (a*c+b*d)/((c**2)+(d**2))
        newimaginary = (b*c-a*d)/((c**2)+(d**2))
        return Complex(newreal,newimaginary)

    def __str__(self):
        if(not(abs(self.imaginary)==self.imaginary)):
            operator = ""
        else:
            operator = "+"
        if(self.real == 0 and not(self.imaginary == 0)):
            return str(operator+str(self.imaginary)+"i")
        elif(self.imaginary == 0 and not(self.real == 0)):
            return str(self.real)
        elif(self.imaginary == 0 and self.real == 0):
            return str("0")
        return str(str(self.real)+operator+str(self.imaginary)+"i")

def main():
    realone = input("Enter the real part of the first complex number: ")
    imagone = input("Enter the imaginary part of the first complex number: ")
    realsecond = input("Enter the real part of the second complex number: ")
    imagsecond = input("Enter the imaginary part of the second complex number: ")
    numone = Complex(realone,imagone)
    numtwo = Complex(realsecond,imagsecond)
    print("C1 = {}".format(numone))
    print("C2 = {}".format(numtwo))
    print("C1+C2 = {}".format(numone+numtwo))
    print("C1-C2 = {}".format(numone-numtwo))
    print("C1*C2 = {}".format(numone*numtwo))
    if(numone/numtwo == None):
        print("C1/C2 = None; Divide by Zero Error!")
    else:
        print("C1/C2 = {}".format(numone/numtwo))

if  __name__  == '__main__':
    main()

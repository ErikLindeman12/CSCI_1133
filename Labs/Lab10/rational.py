class rational:
    def __init__(self,num=0,den=1):
        self.numerator = num
        if den == 0:
            self.denominator = 1
        else:
            self.denominator = den
    def __str__(self):
        if(self.numerator % self.denominator == 0):
            return str(self.numerator/self.denominator)
        else:
            return str(self.numerator) + '/' + str(self.denominator)

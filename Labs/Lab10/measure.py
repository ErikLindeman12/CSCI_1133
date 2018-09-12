class measure:
    def __init__(self,feet=None,inch=None):
        if((feet == None) and (inch == None)):
            feet = 0
            inch = 0
        elif(inch == None):
            inch = feet
            feet = 0
        self.feet = feet
        if(inch>11):
            self.feet += inch//12
            self.inch = inch%12
        else:
            self.inch = inch

    def __str__(self):
        if(not(self.inch == 0) and not(self.feet == 0)):
            return str(str(self.feet)+"'"+str(self.inch)+'"')
        elif((self.feet == 0) and (self.inch == 0)):
            return str('0"')
        elif(self.feet == 0):
            return str(str(self.inch)+'"')
        elif(self.inch == 0):
            return str(str(self.feet)+"'")
        else:
            return "Error"

    def __add__(self,rhand):
        rhandInch = rhand.inch + rhand.feet*12
        rhandFeet = 0
        selfInch = self.inch + self.feet*12
        selfFeet = 0
        inch = rhandInch+selfInch
        feet = inch//12
        inch = inch%12
        return measure(feet,inch)

    def  __sub__(self,rhand):
        rhandInch = rhand.inch + rhand.feet*12
        rhandFeet = 0
        selfInch = self.inch + self.feet*12
        selfFeet = 0
        inch = -rhandInch+selfInch
        feet = inch//12
        inch = inch%12
        return measure(feet,inch)

m1 = measure()
m2 = measure(4,11)
m3 = measure(6,10)
print( m1 )
print( m2+m3 )
print( m3-m2 )

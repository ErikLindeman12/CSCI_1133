class vec3:
    def __init__(self,a=0,b=0,c=0):
        vector = []
        vector.append(a)
        vector.append(b)
        vector.append(c)
        self.vector = vector
    def __str__(self):
        return "["+str(self.vector[0])+", "+str(self.vector[1])+", "+str(self.vector[2])+"]"
    def vList(self):
        return self.vector
    def setValues(self,a=0,b=0,c=0):
        vector = []
        vector.append(a)
        vector.append(b)
        vector.append(c)
        self.vector = vector
    def __float__(self):
        summation = (float((self.vector[0]))**2)+(float((self.vector[1]))**2)+(float((self.vector[2]))**2)
        squareRoot = summation**(1/2)
        self.magnitude = squareRoot
        return float(self.magnitude)
    def __add__(self,rhand):
        a = float(self.vector[0])+float(rhand.vector[0])
        b = float(self.vector[1])+float(rhand.vector[1])
        c = float(self.vector[2])+float(rhand.vector[2])
        return vec3(a,b,c)
    def __truediv__(self,scalar):
        a = float(self.vector[0])/scalar
        b = float(self.vector[1])/scalar
        c = float(self.vector[2])/scalar
        return vec3(a,b,c)

fa1 = float(input("Input your 1st force vector 1: "))
fb1 = float(input("Input your 2nd force vector 1: "))
fc1 = float(input("Input your 3rd force vector 1: "))
fa2 = float(input("Input your 1st force vector 2: "))
fb2 = float(input("Input your 2nd force vector 2: "))
fc2 = float(input("Input your 3rd force vector 2: "))
m = float(input("Input your mass: "))

force1 = vec3(fa1,fb1,fc1)
force2 = vec3(fa2,fb2,fc2)
totalForce = force1+force2
accel = totalForce/m
print(accel.vList())
print(float(accel))

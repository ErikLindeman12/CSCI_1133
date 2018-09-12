#CSCI 1133 Homework 1
#Erik Lindeman
#Problem 1A

def focalLength(obj, im):
    focal = (1/((1/obj)+(1/im)))
    return focal

print('Welcome to the Focal Length Calculator')
obj = float(input('Enter an object dsistance in mm: '))
im = float(input('Enter an image distance in mm: '))
print('Focal Length: ', focalLength(obj, im),'mm')

#CSCI 1133 Homework 3
#Erik Lindeman
#Problem B
Order = []
Cost = 0
ordering = True
print("Welcome to the Python Buffet, the hippest restaurant in town!")
Order.append(input("What would you like to order? "))
if('burger' in Order[0]):
    Cost+=3
elif('soda' in Order[0]):
    Cost+=2
else:
    Cost+=5
while(ordering):
    newItem = input("Would you like to order anything else? ")
    if(newItem == ""):
        ordering = False
    elif(not(newItem in Order)):
        Order.append(newItem)
        if('burger' in newItem):
            Cost+=3
        elif('soda' in newItem):
            Cost+=2
        else:
            Cost+=5
    else:
        print("Oops.  You must have entered " + newItem + " again by accident")
print("You have ordered the following:")
for x in range(0, len(Order)):
    print(Order[x])
print("This will cost yoou a total of ${}.00".format(Cost))
print("Thank you for your patronage!")

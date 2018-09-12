#Erik Lindeman (LINDE799)
#CSCI 1133
#Homework 6 Problem A


#Makes a list of all the Unicode character values
global UNICODE_VALUES
UNICODE_VALUES = {"pizza":127829,"chicken":127831,"apple":127822,"peach":127825,"cherry":127826,
    "roasted sweet potato":127840,"pineapple":127821,"cookie":127850,"bread":127838,
    "lemon":127819,"banana":127820,"strawberry":127827}


def add_item(d,item):
    #if it's already in the dictionary, increase it's value, otherwise add it to it
    if(item in d):
        d[item]+=1
    else:
        d[item] = 1
    return d

def lookup(d,item):
    #Find the amount of them currently
    if(item in d):
        count = d[item]
        if(count>0):
            #if it has a unicode, display the item then a unicode for every one of it
            if(item in UNICODE_VALUES):
                unicode_value = UNICODE_VALUES[item]
                print(item,end=" ")
                if(count>1):
                    #if there are more than 1, display how many and keep the line going
                    for x in range(count-1):
                        print(chr(unicode_value),end=" ")
                print(chr(unicode_value))
            #if it's not a unicode, just display the item then how many there are
            else:
                print("{0} {1}".format(item, count))

def show(d):
    for item in d:
        #Find the amount of them currently
        count = d[item]
        if(count>0):
            #if it has a unicode, display the item then a unicode for every one of it
            if(item in UNICODE_VALUES):
                unicode_value = UNICODE_VALUES[item]
                print(item,end=" ")
                if(count>1):
                    #if there are more than 1, display how many and keep the line going
                    for x in range(count-1):
                        print(chr(unicode_value),end=" ")
                print(chr(unicode_value))
            #if it's not a unicode, just display the item then how many there are
            else:
                print("{0} {1}".format(item, count))

def sub_item(d,item):
    #if it's in the dictionary, subtract one, otherwise, move the count to 0.
    if(item in d):
        if(d[item]>=1):
            d[item]-=1
        else:
            d[item] = 0
    else:
        d[item] = 0
    return d

def main():
    d = {}
    continue_loop = True
    #until they say quit, loop
    while(continue_loop):
        #input a command, seperate it by spaces to find the item and the command
        user_input = input("=> ")
        space = user_input.find(" ")
        command = user_input[:space]
        item = user_input[(space+1):]
        item = item.lower()
        #based on the command, call a  different function
        if(command == "add"):
            d = add_item(d,item)
        elif(user_input == "show"):
            show(d)
        elif(command == "lookup"):
            lookup(d,item)
        elif(command == "sub"):
            d = sub_item(d,item)
        #if the command is quit, stop the loop
        elif(user_input == "quit"):
            continue_loop = False

if  __name__  == '__main__':
    main()

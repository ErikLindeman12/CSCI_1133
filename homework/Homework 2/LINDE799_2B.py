#CSCI 1133 Homework 2
#Erik Lindeman
#Problem B

monthBoolean = False
dateBoolean = False
number1 = True
number2 = True

while(monthBoolean == False or dateBoolean == False):
    month = input("Month of birth: ")
    date = input("Day of birth: ")
    for x in month:
        if(x.isdigit() == False):
            number1 = False
    if(number1 == True):
        month = int(month)
    else:
        monthBoolean = False

    for x in date:
        if(x.isdigit() == False):
            number2 = False
    if(number2 == True):
        date = int(date)
    else:
        dateBoolean = False

    if(number1 and number2):
        if(month > 0 and month <= 12):
            monthBoolean = True
        else:
            monthBoolean = False

        if(date>0):
            if(month == 1 and date <= 31):
                dateBoolean = True
            elif(month == 2 and date <= 28):
                dateBoolean = True
            elif(month == 3 and date <= 31):
                dateBoolean = True
            elif(month == 4 and date <= 30):
                dateBoolean = True
            elif(month == 5 and date <= 31):
                dateBoolean = True
            elif(month == 6 and date <= 30):
                dateBoolean = True
            elif(month == 7 and date <= 31):
                dateBoolean = True
            elif(month == 8 and date <= 31):
                dateBoolean = True
            elif(month == 9 and date <= 30):
                dateBoolean = True
            elif(month == 10 and date <= 31):
                dateBoolean = True
            elif(month == 11 and date <= 30):
                dateBoolean = True
            elif(month == 12 and date <= 31):
                dateBoolean = True
            else:
                dateBoolean = False
        else:
            dateBoolean = False

    if(monthBoolean == False or dateBoolean == False):
        print("Invalid date")

if (month == 1 and date >= 20) or (month == 2 and date <= 18):
    print("Aquarius")
elif (month == 2 and date >= 19) or (month == 3 and date <= 20):
    print("Pisces")
elif (month == 3 and date >= 21) or (month == 4 and date <= 19):
    print("Aries")
elif (month == 4 and date >= 20) or (month == 5 and date <= 20):
    print("Taurus")
elif(month == 5 and date >= 21) or (month == 6 and date <= 20):
    print("Gemini")
elif(month == 6 and date >= 21) or (month == 7 and date <= 22):
    print("Cancer")
elif(month == 7 and date >= 23) or (month == 8 and date <= 22):
    print("Leo")
elif(month == 8 and date >= 23) or (month == 9 and date <= 22):
    print("Virgo")
elif(month == 9 and date >= 23) or (month == 10 and date <= 22):
    print("Libra")
elif(month == 10 and date >= 23) or (month == 11 and date <= 21):
    print("Scorpio")
elif(month == 11 and date >= 22) or (month == 12 and date <= 21):
    print("Sagittarius")
elif(month == 12 and date >= 22) or (month == 1 and date <= 19):
    print("Capricorn")

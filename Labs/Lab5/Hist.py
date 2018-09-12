import random
dieList = [0,0,0,0,0,0,0,0,0,0,0,0,0]
for x in range(0,10000):
    die2 = random.randint(1,6)
    die1 = random.randint(1,6)
    dieTotal = die1+die2
    dieList[dieTotal] += 1
for x in range(2,12):
    dieAmt = str(dieList[x])
    print("{}: ".format(x) + dieAmt)

hand = input("Input your current hand: ")
val = 0
for x in range(0,len(hand)):
    hand[x]
    if((hand[x] == 'J')or(hand[x] == 'Q')or(hand[x] == 'K')or(hand[x] == 'T')):
        val+=10
    elif(hand[x]=='9'):
        val+=9
    elif(hand[x]=='8'):
        val+=8
    elif(hand[x]=='7'):
        val+=7
    elif(hand[x]=='6'):
        val+=6
    elif(hand[x]=='5'):
        val+=5
    elif(hand[x]=='4'):
        val+=4
    elif(hand[x]=='3'):
        val+=3
    elif(hand[x]=='2'):
        val+=2
if('A' in hand):
    if(val>10):
        val+=1
    else:
        val+=11
print(val)

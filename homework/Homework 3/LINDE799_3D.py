#CSCI 1133 Homework 3
#Erik Lindeman
#Problem D

def move(moveVar,who):
    if(moveVar<=2):
        row1[moveVar] = who
    elif(moveVar<=5):
        row2[moveVar-3] = who
    else:
        row3[moveVar-6] = who
    print("",row1,'\n',row2,'\n',row3)

def score(moveVar, who):
    global win
    win = False
    column = True
    if(who == "x"):
        if not(moveVar == -1):
            for x in range(0,3):
                if (moveVar%3 == x):
                    scores1[x] += 1
                if((moveVar<(x+1)*3) and column):
                    scores1[x+3] += 1
                    column = False
            if(moveVar%4 == 0):
                scores1[6] +=1
            elif(moveVar%2 == 0):
                scores2[7] +=1
            for x in range(0,len(scores1)):
                if(scores1[x] >= 3):
                    win = True
    elif(who == "o"):
        if not(moveVar == -1):
            for x in range(0,3):
                if (moveVar%3 == x):
                    scores2[x] += 1
                if((moveVar<(x+1)*3) and column):
                    scores2[x+3] += 1
                    column = False
            if(moveVar%4 == 0):
                scores2[6] +=1
            elif(moveVar%2 == 0):
                scores2[7] +=1
            for x in range(0,len(scores2)):
                if(scores2[x] >= 3):
                    win = True

def main():
    global game
    global turn
    global used1
    global used2
    global row1
    global row2
    global row3
    global scores1
    global scores2
    global moveVar
    game = True
    turn = 1
    used1 = []
    used2 = []
    row1 = [' ',' ',' ']
    row2 = [' ',' ',' ']
    row3 = [' ',' ',' ']
    scores1 = [0,0,0,0,0,0,0,0]
    scores2 = [0,0,0,0,0,0,0,0]
    moveVar = -1
    #columns: 1,2,3, rows: 1,2,3, Diag: 1,2
    while(game):
        if(turn%2==1):
            moveVar = int(input("Player 1, where would you like to move?: "))
            if(not(moveVar in used1)and not(moveVar in used2)):
                who = "x"
                turn+=1
                actuallyMove = True
                used1.append(moveVar)
            else:
                print("This space has already been taken.  Please try again!")
                actuallyMove = False
        else:
            moveVar = int(input("Player 2, where would you like to move?: "))
            if(not(moveVar in used1)and not(moveVar in used2)):
                who = "o"
                turn+=1
                actuallyMove = True
                used2.append(moveVar)
            else:
                print("This space has already been taken.  Please try again!")
                actuallyMove = False
        if(actuallyMove):
            move(moveVar,who)
            score(moveVar, who)
        if(win):
            game = False
            if(who == "x"):
                winner = "1"
            else:
                winner = "2"
            print("Player {} wins!".format(winner))
        elif(turn>9):
            game = False
            print("The game was a tie")


if  __name__  == '__main__':
    main()

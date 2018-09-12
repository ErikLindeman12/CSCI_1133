#CSCI 1133 Homework 2
#Erik Lindeman
#Problem D

roundNumber = 1
oneWinCount = 0
twoWinCount = 0
endGame = False

while (endGame == False):
    print("Round #",roundNumber)
    oneChoice = input("Player 1's Choice: ")
    twoChoice = input("Player 2's Choice: ")

    if ((oneChoice == "R" or oneChoice == "r") and (twoChoice == "S" or twoChoice == "s")):
        oneWinCount += 1
        roundNumber += 1
        print("Player 1 wins this round")
    elif ((oneChoice == "P" or oneChoice == "p") and (twoChoice == "R" or twoChoice == "r")):
        oneWinCount += 1
        roundNumber += 1
        print("Player 1 wins this round")
    elif ((oneChoice == "S" or oneChoice == "s") and (twoChoice == "P" or twoChoice == "p")):
        oneWinCount += 1
        roundNumber += 1
        print("Player 1 wins this round")

    if ((twoChoice == "R" or twoChoice == "r") and (oneChoice == "S" or oneChoice == "s")):
        twoWinCount += 1
        roundNumber += 1
        print("Player 2 wins this round")
    elif ((twoChoice == "P" or twoChoice == "p") and (oneChoice == "R" or oneChoice == "r")):
        twoWinCount += 1
        roundNumber += 1
        print("Player 2 wins this round")
    elif ((twoChoice == "S" or twoChoice == "s") and (oneChoice == "P" or oneChoice == "p")):
        roundNumber += 1
        twoWinCount += 1
        print("Player 2 wins this round")

    if ((oneChoice == "R" or oneChoice == "r") and (twoChoice == "R" or twoChoice == "r")):
        print("No one wins this round")
        roundNumber += 1
    if ((oneChoice == "P" or oneChoice == "p") and (twoChoice == "P" or twoChoice == "p")):
        print("No one wins this round")
        roundNumber += 1
    if ((oneChoice == "S" or oneChoice == "s") and (twoChoice == "S" or twoChoice == "s")):
        print("No one wins this round")
        roundNumber += 1

    if (oneWinCount >= 2):
        print("Player 1 wins the game")
        endGame = True
    if (twoWinCount >= 2):
        print("Player 2 wins the game")
        endGame = True
    if(roundNumber >= 4):
        print("The game is a tie!")
        endGame = True

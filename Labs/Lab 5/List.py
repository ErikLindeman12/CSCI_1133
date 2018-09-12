def main():
    stop = False
    user = "nothing"
    List = []
    while(not stop):
        user = input("Put in a word: ")
        if(user == ""):
            stop = True
        else:
            lower = user.lower()
            firstLetter = lower[0]
            for x in range(1,len(user)):
                if (user[x] == firstLetter):
                    List.append(user)

    for x in range(0,len(List)):
        print(List[x])

if __name__ == "__main__":
    main()

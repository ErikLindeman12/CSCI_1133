import random
List = []
def ssort(List):
    y = 0
    while(y<=len(List)):
        for x in range(0,len(List)):
            if(List[x] == y):
                xval = List[x]
                List[x] = List[xval-1]
                List[y-1] = y
        y+=1
n = int(input("Choose a length for the List: "))
for x in range(1,n+1):
    List.append(x)
random.shuffle(List)
print(List)
ssort(List)
print(List)

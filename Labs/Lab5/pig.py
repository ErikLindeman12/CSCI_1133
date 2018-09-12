phrase = input("Your phrase? ")
phraseactual = phrase
phrase = phrase.lower()
up = phraseactual.upper()
end = []
start = []
upper = False
x=0
go = True
string = ""
mid = []
while((x<=len(phrase))and not(phraseactual[x]==" ")and go):
    if(not(phrase[x] == "e"))and(not(phrase[x] == "i"))and(not(phrase[x] == "o"))and(not(phrase[x] == "i"))and(not(phrase[x] == "a"))and(not(phrase[x] == "u")):
        end.append(phrase[x])
        if(not(phraseactual[x] == phrase[x])):
            upper = True
        else:
            upper = False
    else:
        go = False
        a=x+1
        Continue = True
        while(a<=len(phrase))and(Continue):
            if (phraseactual[a-1] == " "):
                Continue = False
            else:
                mid.append(phraseactual[a])
            a+=1
        if(not upper):
            start.append(phraseactual[x])
        else:
            start.append(up[x])
    x+=1

for y in range(0,len(start)):
    string += start[y]
for b in range(0,len(mid)):
    string += mid[b]
for z in range(0,len(end)):
    string+=end[y]
if not (end == []):
    string+="ay"
else:
    string+="way"
print(string)

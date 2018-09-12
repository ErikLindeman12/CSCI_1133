def suitCount(card):
  suit = {}
  rank = {}
  for x in range(0,len(card)):
      if(card[x][1] in suit):
          suit[card[x][1]] +=1
      else:
          suit[card[x][1]] =1
  for x in range(0,len(card)):
      if(card[x][0] in rank):
          rank[card[x][0]] +=1
      else:
          rank[card[x][0]] =1
  return suit

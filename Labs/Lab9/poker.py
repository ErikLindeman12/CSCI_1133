import cards
import cards2
card = [ 'AS', 'AD', '2C', 'TH', 'TS']
dictionary = {5:"flush, straight, straight, or high-card",4:"one pair",3:"two pair or three-of-a-kind",
2:"four-of-a-kind or full-house",1:"That's impossible!"}
rank = cards.rankCount(card)
suit = cards2.suitCount(card)
if(5 == len(rank)):
    cardinality = 5
elif(4 == len(rank)):
    cardinality = 4
elif(3 == len(rank)):
    cardinality = 3
elif(2 == len(rank)):
    cardinality = 2
elif(1 == len(rank)):
    cardinality = 1
else:
    cardinality = 1
print(dictionary[cardinality])

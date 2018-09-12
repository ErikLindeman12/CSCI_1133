def test(names, scores):
  Dict = {}
  for x in range(0,len(names)):
      currName = names[x]
      currScores = scores[x]
      Dict[currName] = currScores
  return Dict

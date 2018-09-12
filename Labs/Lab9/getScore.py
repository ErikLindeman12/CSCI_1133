def getScore(name, Dict):
  if(name in Dict):
    print("{} is in the Dictionary!".format(name))
    return 1
  else:
    print("{} is not in the Dictionary!".format(name))
    return -1

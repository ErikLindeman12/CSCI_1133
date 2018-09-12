def reverse(teststring):
  newstring = ""
  x = len(teststring)-1
  while x >=0:
      newstring+=teststring[x]
      x-=1
  return newstring

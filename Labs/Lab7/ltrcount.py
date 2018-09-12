def ltrcount(string):
  a = 0
  p = "abcdefghijklmnopqrstuvwxyz"
  stringg = string.lower()
  for x in stringg:
    if x in p:
      a+=1
  print(a)

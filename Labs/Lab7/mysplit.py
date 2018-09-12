def mysplit(string,delimiter):
  listerino = []
  b = 0
  a = 0

  while not(a == -1):
      a = string.find(delimiter)
      if not(a == -1):
          listerino.append("")
          for x in range(0,a):
              listerino[b]+=string[x]
          newstring = ""
          for y in range(a+len(delimiter),len(string)):
              newstring += string[y]
          string = newstring
          b+=1
  listerino.append(string)
  print(listerino)

def populate(m,n,value):
  actualmatrix = []
  xval = []
  yval = []
  import random
  for x in range(0,m):
      actualmatrix.append([])
  for x in range(0,m):
      for b in range(0,m):
          actualmatrix[x].append(b)
          actualmatrix[x][b]=0
  for z in range(0,n):
      xval.append(random.randint(0,m-1))
      yval.append(random.randint(0,m-1))
      actualmatrix[xval[z]][yval[z]]= value
  for a in range(0,len(actualmatrix)-1):
    print(actualmatrix[a])

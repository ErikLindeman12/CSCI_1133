def identity(n):
  actualmatrix = []

  for x in range(0,n):
      matrixlist = []
      for y in range(0,n):
        if(x==y):
            matrixlist.append(1)
        else:
            matrixlist.append(0)
      actualmatrix.append(matrixlist)
  for x in range(0,len(actualmatrix)):
    print(actualmatrix[x])

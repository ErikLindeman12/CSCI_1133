def matrix(n, init):
  matrixlist = []
  actualmatrix = []

  for y in range(0,n):
    matrixlist.append(init)
  for x in range(0,n):
    actualmatrix.append(list(matrixlist))
  for x in range(0,len(actualmatrix)):
    print(actualmatrix[x])
  return actualmatrix

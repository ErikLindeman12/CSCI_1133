def emul(a,b):
  if((a/b) != 1):
      neg = True
  else:
      neg = False
  a = abs(a)
  b = abs(b)
  sum=0
  while(b>0):
    if(b%2 == 1):
      sum+=a
    b/=2
    a*=2
    if(b-int(b)<0):
      b = int(b)-1
    else:
      b = int(b)
  if(neg):
      print(-sum)
  else:
      print(sum)

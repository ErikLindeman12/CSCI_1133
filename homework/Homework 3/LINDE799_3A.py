#CSCI 1133 Homework 3
#Erik Lindeman
#Problem A

def intvert(lst):
  inlst = []
  for x in range(0,len(lst)):
      if(type(lst[len(lst)-(x+1)]) is int):
          inlst.append(lst[len(lst)-(x+1)])
  print(inlst)

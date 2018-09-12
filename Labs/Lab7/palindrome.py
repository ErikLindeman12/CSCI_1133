import reverse

def ispalindrome(string):
  teststring = string.replace(" ","").replace("!","").replace(".","").replace(",","").replace("?","").replace("'","")
  teststring = teststring.lower()
  newstring = reverse.reverse(teststring)
  if(newstring == teststring):
    return True
  else:
    return False

go  = True
while go:
  string = input("Enter a string: ")
  palindrome = ispalindrome(string)
  if(palindrome):
    print("{0} is a palindrome".format(string))
  else:
    print("{0} is a not palindrome".format(string))
  Continue = input("Continue? (y/n): ")
  if Continue == "y":
    go = True
  else:
    go = False

#CSCI 1133 Homework 1
#Erik Lindeman
#Problem 1B

def euro(dollars):
  euros = dollars * .83
  eurosStr = format(euros, ".2f")
  return eurosStr

def yen(dollars):
  yens = dollars * 111.14
  yensStr = format(yens, ".2f")
  return yensStr
def bitcoin(dollars):
    bitcoins = dollars * .000076
    bitcoinsStr = format(bitcoins, '.2f')
    return bitcoinsStr

print("Welcome to the Currency Conversion Program!")
dollars = float(input("Enter an amount in U.S. Dollars: $"))
print("$", dollars, "=", euro(dollars), "euro")
print("$", dollars, "=", yen(dollars), "yen")
print("$", dollars, "=", bitcoin(dollars), "bitcoin")

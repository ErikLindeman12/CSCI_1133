def roundit():
  number = float(input("number: "))
  if(abs(number)/number) == 1:
    number = number + 0.5
    number = int(number)
    print(number)
  else:
    number = number - 0.5
    number = int(number)
    print(number)

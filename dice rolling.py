import random
a = "b"
while a == "b":
  roll = random.randint(1,6)
  if roll == 1:
    print("|       |")
    print("|   0   |")
    print("|       |")
  
  if roll == 2:
    print("|0      |")
    print("|   0   |")
    print("|       |")
  
  if roll == 3:
    print("|0       |")
    print("|   0    |")
    print("|       0|")
  
  if roll == 4:
    print("|0       0|")
    print("|         |")
    print("|0       0|")
  
  if roll == 5:
    print("|0       0|")
    print("|    0    |")
    print("|0       0|")
  
  
  if roll == 6:
    print("|0    0   0|")
    print("|          |")
    print("|0    0   0|")

  x = input("press b to roll again and n to exit")
  print("\n")



  
    
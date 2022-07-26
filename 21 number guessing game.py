#returns the nearest multiple to 4
def nearestMultiple(num):
  if num >= 4:
    near = num + (4 - (num % 4))
  else:
    near = 4
  return near
  
def losing():
  print("\n You loose")
  print("Better luck next time")
  exit(0)

#Checks if the numbers are consecutive
def check(abc):
  i =1
  while i < len(abc):
    if (abc[i] - abc[i-1]) != 1:
      return False
    i = i + 1
  return True

#starting the game
def start():
  abc = []
  last = 0
  while True:
    chance = input("Enter F to play First or S to play Second")
    if chance == "F":
      while True:
        if last == 20:
          losing()
        else:
          inp= int(input("How many numbers would you wish to play: "))
          if inp >0 and inp <= 3:
            comp = 4 - inp
          else:
            print("Wrong Input")
            losing()
          i,j =1,1
          print("Now enter the value:")
          while i <= inp:
            a= int(input("> "))
            abc.append(a)
            i =i +1
          #store the last value of abc
          last = abc[-1]
          #check if numbers are consecutive
          if check(abc) == True:
            if last == 21:
              losing()
            else:
            #computer's turn
              while j <= comp:
                abc.append(last + comp)
                j =j+1
              print("The order of numbers after the computers turn is \n", abc)
              last = abc[-1]
          else:
            print("\n Sorry you didn't input consecutive numbers")
            losing()
    #when the user takes the second chance
    elif chance == "S":
      comp =1
      last = 0
      while last < 20:
        #comp's turn
        j = 1
        while j <= comp:
          abc.append(last + j)
          j = j +1
        print("The order of numbers after the computers turn is \n", abc)
        if abc[-1] == 20:
          losing()
        else:
          print("\n it's your turn")
          inp= int(input("How many numbers would you wish to play: "))
          i = 1
          print("Enter the values:")
          while i <= inp:
            abc.append(int(input("> ")))
            i=i+1
          last = abc[-1]
          if check(abc) == True:
            near = nearestMultiple(last)
            comp = near- last
            if comp == 4:
              comp = 3
            else:
              comp =comp
          else:
            print("\n Sorry you didn't input consecutive numbers")
            losing()
      print("\n Congratulations you won")
      exit(0)
    else:
      print("Wrong Choice")
#Create a while loop to start the game
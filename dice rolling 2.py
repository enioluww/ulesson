import random
min = 1
max = 6
p_score=0
c_score=0
roll_again ="yes"
while roll_again =="yes" or roll_again=="y":
  print("The dice is rolling.....")
  player= random.randint(min,max)
  print("Player's choice is",player)
  computer=random.randint(min,max)
  print("Computer's choice is",computer)
  roll_again = input("Do you want to roll the dice: ")
  if player > computer:
    p_score +=1
    print("Your score is",p_score)
  else:
    c_score +=1
    print("computer's score is",c_score)

if c_score > 5 or p_score > 5:
  print("Game over")
  

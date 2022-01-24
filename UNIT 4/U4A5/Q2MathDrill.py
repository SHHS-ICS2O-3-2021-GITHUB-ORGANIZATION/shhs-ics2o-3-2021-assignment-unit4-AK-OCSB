import random

randomQuestion = random.randint(1,2)

import time
timer_length = float(input("How many seconds would you like you're timer to be set for? "))


if randomQuestion == 1:
  #time.sleep(timer_length)

  multiNum1 = random.randint(1,12)
  multiNum2 = random.randint(1,12)
  print("What is:" , multiNum1 , "*" , multiNum2 )
  multiAnswer = int(input("Please enter you answer: "))
  if multiAnswer == multiNum1 * multiNum2:
    print("You are correct yay!")
  else:
    print("You are wrong :(")
elif randomQuestion == 2:
  #time.sleep(timer_length)

  addNum1 = random.randint(1,100)
  addNum2 = random.randint(1,100)
  print("What is:" , addNum1 , "+" , addNum2)
  addAnswer = int(input("Please enter your answer: "))
  if addAnswer == addNum1 + addNum2:
    print("You are correct yay!")
  else:
    print("You are wrong :(")


#print("Done!")

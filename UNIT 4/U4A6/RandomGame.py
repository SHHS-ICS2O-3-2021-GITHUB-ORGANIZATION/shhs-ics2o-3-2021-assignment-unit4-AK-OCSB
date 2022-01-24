# NAME OF AUTHOR:Ashley Koza  
# NAME OF THE PROGRAM:
# DATE OF CREATION:
# PURPOSE OF PROGRAM: 

# VARIABLE DEFINITION

number1 = 0
number2 = 0
maxNumber = 0
minNumber = 0
rand1 = 0

import sys, time
 
def texttime(words):
	for c in words:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.1)
 
 

texttime("HI, welcome to the Random Number Game.\nThis game ask you to enter two numbers which will act as a range.\nThen you get to guess what number you think the computer choose.\n")

time.sleep(2)

playGame = input("Would you like to play.\nPlease enter 'y' for yes and 'n' for no:")

if playGame == 'y':
  #promt user for 2 intergers
  number1 = int(input("Please enter an integer: "))
  number2 = int(input("Please enter another integer: "))
  
  import random
  
  #define the max and min value as to not cause an error.
  maxNumber = max(number1 , number2)
  minNumber = min(number1 , number2)
  #Sets a range, then picks a random number between said range.
  rand1 = random.randint(minNumber, maxNumber)
  userAnswer = 0
  counter = 0
  
  while userAnswer != rand1:
    userAnswer = int(input("Please guess a number you think the computer choose: "))
    counter += 1
    if counter == 1:
      print("You got the correct answer. Wow it took you" , counter , "try.")
      break
    else:
      print("You got the correct answer. Wow it took you" , counter , "tries.")
      break
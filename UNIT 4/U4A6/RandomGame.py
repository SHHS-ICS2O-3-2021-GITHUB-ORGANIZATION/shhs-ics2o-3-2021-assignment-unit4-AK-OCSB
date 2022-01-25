# NAME OF AUTHOR:Ashley Koza  
# NAME OF THE PROGRAM:Guessing Game
# DATE OF CREATION:2022-01-24
# PURPOSE OF PROGRAM:Practice what we have learned in each lesson. Practice random modules.

# VARIABLE DEFINITION

number1 = 0
number2 = 0
maxNumber = 0
minNumber = 0
rand1 = 0
userAnswer = 0
counter = 0

#imports time and system specific parameters and functions
import sys, time
 
#define variable that will hold string
def texttime(words):
	
	#prints textime similar to type writer.
	for c in words:
		
		#writes the words in the range of c
		sys.stdout.write(c)
		
		#gets rid of the buffer
		sys.stdout.flush()
		
		#pause of time between each character apearing
		time.sleep(0.1)
 
 
#display to user what this program is
texttime("HI, welcome to the Random Number Game.\nThis game ask you to enter two numbers which will act as a range.\nThen you get to guess what number you think the computer choose.\n")

#pause 2 seconds before showing the code below
time.sleep(2)

#prompt user if they would like to play or not
playGame = input("\nWould you like to play.\nPlease enter 'y' for yes and 'n' for no:")

#if no the game will end
if playGame == 'n':
	print("bye bye")
	
#if yes the game will run
elif playGame == 'y':
	
  #promt user for 2 intergers
  number1 = int(input("Please enter an integer: "))
  number2 = int(input("Please enter another integer: "))

#import random module  
  import random
  
  #define the max and min value as to not cause an error.
  maxNumber = max(number1 , number2)
  minNumber = min(number1 , number2)
	
  #Sets a range, then picks a random number between said range.
  rand1 = random.randint(minNumber, maxNumber)

  #repeats the process only while the user's answer is not equal to the random number
  while userAnswer != rand1:
    userAnswer = int(input("Please guess a number you think the computer choose: "))

#add 1 to counter
    counter += 1
#if user answer equal to random number, inform user and display how many tries it took them
    if userAnswer ==rand1:
    	print("Wow, you guessed the number, it took you" , counter , "try(s) to get it right.")


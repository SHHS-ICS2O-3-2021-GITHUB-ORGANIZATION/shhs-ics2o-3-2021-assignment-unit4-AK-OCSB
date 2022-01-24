# NAME OF AUTHOR:Ashley Koza  
# NAME OF THE PROGRAM: Q1Length
# DATE OF CREATION:2022-01-24
# PURPOSE OF PROGRAM:Practice using different command on strings and exit codes.

#import time modules
import time 

#set playGame to y to start while loop right away
playGame = 'y'

#repeats process while playGame is equal to y
while playGame == 'y':

  #prompt user to enter a word
  userWord = input("Please enter any word: ")

  #caculate lenght of word
  userLength = len(userWord)

  #display to user their word and its length
  print("Your word" , userWord , "is" , userLength , "character(s) long")

#stall program below 2 seconds
  time.sleep(2)

#propmt user and ask if they would like to playagin
  playGame = input("Please type 'y' if you would like to play again.\nPlease type 'quit' if you don't want to play again.")

#if user input is equal to quit program will quit
if playGame == 'quit':
  quit("Goodbye")

#if user doesn't enter the proper words end program
else:
  print("You entered neither goodbye :(")
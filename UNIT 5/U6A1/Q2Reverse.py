# NAME OF AUTHOR:Ashley Koza  
# NAME OF THE PROGRAM: Q2Reverse
# DATE OF CREATION:2022-01-24
# PURPOSE OF PROGRAM:Practice using different command on strings. Practice time module.

#import time modules
import time

#propmt user for word
userWord = input("Please enter any word: ")

# Getting length of string
userLength = len(userWord)
  
# using reversed() function printing with a pause of 1 second
for i in reversed(range(0, userLength)):
    print(userWord[i])
    time.sleep(1)

#displaying to user program is over
print("\nGoodbye")
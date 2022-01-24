#NAME OF AUTHOR: Ashley Koza
#NAME OF PROGRAM: Q2MathDrills
#DATE OF CREATION: 2022-01-24
#PURPOSE OF PROGRAM: Practice conditional statements. Practice randoms modules.


#import random modules
import random



#set a range 1-2, then pick a random number between 1 and 2
randomQuestion = random.randint(1,2)



#if randomQuestion is 1 ask a multiplication question
if randomQuestion == 1:
  

 #set a range 1-12, then pick a number between 1-12
  multiNum1 = random.randint(1,12)
  multiNum2 = random.randint(1,12)
  

  #display multiplication question to user
  print("What is:" , multiNum1 , "*" , multiNum2 )
  

  #propmt user for answer to previous question
  multiAnswer = int(input("Please enter you answer: "))
  

  #if the user answer is equal to multiAnswer, inform the user they are correct
  if multiAnswer == multiNum1 * multiNum2:
    print("You are correct yay!")


   #if answer is anyhing else inform user they are wrong
  else:
    print("You are wrong :(")


 #if randomQuestion is equal to 2 ask an addition question 
elif randomQuestion == 2:
  

#set a range 1-100, then pick a number between 1 -100
  addNum1 = random.randint(1,100)
  addNum2 = random.randint(1,100)
  

  #display addition question to user
  print("What is:" , addNum1 , "+" , addNum2)
  

  #propmt user for the answer to the previous question
  addAnswer = int(input("Please enter your answer: "))
  

  #if the user answer is equal to addAnswer, inform user they are correct
  if addAnswer == addNum1 + addNum2:
    print("You are correct yay!")


   #if answer is anyhing else inform user they are wrong
  else:
    print("You are wrong :(")

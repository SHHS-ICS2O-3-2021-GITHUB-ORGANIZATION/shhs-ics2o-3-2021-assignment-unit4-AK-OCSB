# NAME OF AUTHOR:Ashley Koza  
# NAME OF THE PROGRAM: Q1 Counting
# DATE OF CREATION: 2022-01-18
# PURPOSE OF PROGRAM: Practice loops(while and for). 


# VARIABLE DEFINITION

num = 0
largeNum = 0
countNum = 0


# INPUT

#Prompt user to input numbers.
largeNum = int(input("Please enter a large integer to count up to: "))
countNum = int(input("Please enter a number to count by: "))


# PROCESSING/OUTPUT


#Counting up to the user number by 1.
while num < largeNum:
  print(num)
  num = num + 1

#Counting down to zero from largenum by a count of the user choice.
for i in range(num,0,-countNum):
  print(i)


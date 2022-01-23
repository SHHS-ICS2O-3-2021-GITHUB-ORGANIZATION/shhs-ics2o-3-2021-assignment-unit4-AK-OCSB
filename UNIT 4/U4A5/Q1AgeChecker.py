#NAME OF AUTHOUR: Ashley Koza
#NAME OF PROGRAM: Q1AgeChecker
#DATE OF CREATION: 2022-01-21
#PURPOSE OF PROGRAM: Practice conditional statements. Age caculator. 

#VARIBLES

age = 0

#INPUT

#Propmt user for age
age = int(input("Please enter your age: "))

#PROCESSING

#If age is less than 5 but greater or equal to zero
if age < 5 and age >= 0:
  print("You haven't started school yet :(")

#If age is less than zero.  
elif age < 0:
  print("What are you???")

#If age is greater than 4 but less than 12.
elif age > 4 and age < 12:
  print("You are in elementary school.")

#If age is greater than 11 but less than 15.
elif age > 11 and age < 15:
  print("You are in intermediate school.")

#If age is greater than 14 but less than 19.
elif age > 14 and age < 19:
  print("You are in HIGH SCHOOL.")

#If age is greater than 19.
else:
  print("Wow, you are either in university, college, or you are already in the work force.")
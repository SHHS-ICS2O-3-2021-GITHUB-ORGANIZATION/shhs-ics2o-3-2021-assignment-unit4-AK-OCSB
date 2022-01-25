# NAME OF AUTHOR:Ashley Koza  
# NAME OF THE PROGRAM: Q3WordTriangle
# DATE OF CREATION:2022-01-25
# PURPOSE OF PROGRAM:Practice using different programs on strings. Practice 'for' loops.


#prompt user for string
string = input("Please enter a word: ")

#determine the length of the user's string
strLength = len(string)

#for loop for row
for i in range(strLength):
  #for loop for coloums 
    for j in range(i + 1):
      #printing string with index of j and space
        print(string[j] , end = '')
    #seperates the rows
    print()
    
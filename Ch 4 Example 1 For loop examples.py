#Program name: Ch 4 Example 1 For loop examples.py

#Note the 'end = " "' at the end of the print statements.
#This will prevent a move to the next line before printing the next number.
#the escape sequence \n before subsequent headings forces a line feed.

# Sample range 1: print the numbers 1 to 5
print("Numbers from 1-5:" )
for number in range (1,6):
    print (number, end = " ")
    
# Sample range 2: print numbers in range 0 to 4
print("\nNumbers from 0-4:" )
for number in range (5):
    print (number, end = " ")
    
# Sample range 3: print every third number from 1 to 16
print("\nEvery third number from 1-16:" )
for number in range (1,17,3):
    print (number, end = " ")
    
# Sample range 4: print every number from 5 down to 1
print("\nEvery number from 5 down to 1:" )
for number in range (5,0,-1):
    print (number, end = " ")
   
input ("\n\nPress Enter to exit ")

#Program name: Level 6 Example 7 Formatting printed columns
import random
    
for index in range (20):
    num1 = random.random()      #returns a random number between 0 and 1
    num2 = num1 * 200           #returns a random number between 0 and 200
    num3 = num1 * 200  + 50     #returns a random number between 50 and 250

    #print num1 to 4 decimal places,
    #num2 to 2 decimal places, num3 to 1 decimal place
    
    #each number occupies 20 spaces and is right aligned     
    print("{:>20.4f}{:>20.2f}{:>20.1f}".format(num1,num2,num3))



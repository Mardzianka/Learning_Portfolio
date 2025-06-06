#Program name: Ch 3 Exercise 3 throw two dice.py

import random

num1 = random.randint(1,6)
num2 = random.randint(1,6)
print("You threw", num1, " and", num2)

score = num1 + num2
if num1 == num2:
    print("You threw a double")
    print ("Your score:", 2*score)
else:
    print ("Your score:", score)
           
    

#Program name: Ch 4 Exercise 1 10 random numbers.py
#This demonstrates the use of a for loop to generate 10 random numbers

import random
total = 0
for num in range(10):
    num = random.randint(1,10)
    print(num)
    total += num
print("Total =",total)

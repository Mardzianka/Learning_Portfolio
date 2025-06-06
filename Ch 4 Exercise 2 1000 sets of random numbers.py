#Program name: Ch 4 Exercise 2 1000 sets of 10 random numbers.py
"""
This demonstrates the use of nested for loops to generate a set of 10 
random numbers 1000 times.
The program demonstrates the "Monte Carlo method" for performing a calculation.
The calculated average using a formula is 55.
The answer given by the program should be close to this
if the random number generator is unbiassed.
The greater the number of tests, the more accurate the answer will be. 
"""
import random

overallTotal = 0
numberOfTests = 1000
for test in range(numberOfTests):
    total = 0
    for num in range(10):
        num = random.randint(1,10)
        total += num
#don't print if your number of test is more than about 100!
#    print("Total =",total)

    overallTotal += total
averageTotal = overallTotal/numberOfTests
print("\nAverage total =",averageTotal)

input("\nPress Enter to exit ")



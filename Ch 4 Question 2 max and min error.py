#Program name: Ch 4 Question 2 max and min error.py
#Find the maximum and minimum of a series of test results.
#The end of input is signalled by the user entering -1.


# Set maximum and minimum to first test result
maxResult = 0
minResult = 100
testResult = 0
while testResult != -1:
    testResult = int(input("Please enter test result (-1 to finish): "))
    if testResult > maxResult:
        maxResult = testResult
    if testResult < minResult:
        minResult = testResult
    

print ("\nMaximum test result = ", maxResult)
print ("Minimum test result = ", minResult)

input ("\nPress Enter to exit ")

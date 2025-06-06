#Program name: Ch 4 Question 3 max and min with string input.py
# Find the maximum and minimum of a series of test results.
#The end of input is signalled by the user entering -1.

testResult = input("Please enter test result (-1 to finish): ")

# Set maximum and minimum to first test result
maxResult = testResult
minResult = testResult

while testResult != "-1":
    if testResult > maxResult:
        maxResult = testResult
    if testResult < minResult:
        minResult = testResult
    testResult = input("Please enter test result (-1 to finish): ")


print ("\nMaximum test result = ", maxResult)
print ("Minimum test result = ", minResult)

input ("\nPress Enter to exit ")

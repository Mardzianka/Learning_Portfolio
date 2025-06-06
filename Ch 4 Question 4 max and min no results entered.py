#Program name: Ch 4 Question 4 max and min no results entered.py
# Find the maximum and minimum of a series of test results.
#The end of input is signalled by the user entering -1.

testResult = int(input("Please enter test result (-1 to finish): "))
if testResult == -1:
    noResultsEntered = True
else:
    noResultsEntered = False
# Set maximum and minimum to first test result
maxResult = testResult
minResult = testResult

while testResult != -1:
    if testResult > maxResult:
        maxResult = testResult
    if testResult < minResult:
        minResult = testResult
    testResult = int(input("Please enter test result (-1 to finish): "))

if noResultsEntered:
    print ("No results entered")
else:
    print ("\nMaximum test result = ", maxResult)
    print ("Minimum test result = ", minResult)

input ("\nPress Enter to exit")

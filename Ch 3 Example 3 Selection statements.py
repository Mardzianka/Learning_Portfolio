#Program name: Ch 3 Example 3 Selection statements.py
#Illustrates different selection statements

print("Example 3a")
      
weekendRate = False
day = input("Enter the day of the week: ")
if day == "Saturday" or day == "Sunday":
    weekendRate = True
print("WeekendRate",weekendRate)

print ("\nExample 3b: day = Sunday")
weekendRate = False
day = "Sunday"
if (not day == "Saturday") and (not day == "Sunday"):
    weekendRate = False
print("WeekendRate",weekendRate)

print ("\nExample 3c")
testResult = input("Enter test result, Pass or Fail: ")
interview = input("Enter interview result, Pass or Fail: ")
if interview == "Pass":
    interviewOK = True
else:
    interviewOK = False
if (testResult == "Pass") and (interviewOK):
    print ("Hired")
else:
    print ("Rejected")


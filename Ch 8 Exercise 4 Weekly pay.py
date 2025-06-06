#Program name: Ch 8 Exercise 4 Weekly pay.py
#Program accepts hours worked on each day of a week
#calculates total pay for the week

days = ["Monday","Tuesday","Wednesday",\
        "Thursday","Friday","Saturday","Sunday"]
hoursWorked = [0]*7
def calculatePay(hours, hourlyRate):
    
    total = 0
    for day in range(5):
        total = total + hours[day]*hourlyRate
    total = total + hours[5]* hourlyRate * 1.5
    total = total + hours[6]* hourlyRate * 2
    return total
    
#main program
employee = input ("Enter employee name: ")
payRate = float(input("Enter hourly pay rate: "))
totalHours = 0
for day in range(7):
    hoursWorked[day] = float(input("Enter hours worked on " + days[day]+": "))
    totalHours += hoursWorked[day]
totalPay = calculatePay(hoursWorked, payRate)
print("\nEmployee: ",employee)
print("\nTotal Hours worked: ", totalHours)
print("\nTotal pay: ${:.2f}".format(totalPay))

input("\nPress Enter to exit ")

#Program name: Ch 8 Exercise 3 max temperature.py
#Finds the maximum average daily temperature in a week

days = ["Sunday","Monday","Tuesday","Wednesday",\
        "Thursday","Friday","Saturday"]
def maxTemp(temps):
    maxTemp = temps[0]
    maxDay = 0
    for day in range(7):
        if temps[day] > maxTemp:
            maxTemp = temps[day]
            maxDay = day
    return maxTemp, maxDay

#main program
temperatures = [None]*7
for day in range(7):
    temperatures[day] = int(input("Enter temperature on "+days[day]+": "))
maxTemp, day = maxTemp(temperatures)
print("\nMaximum temperature was " + str(maxTemp) + " on "+ days[day])

input("Press Enter to exit ")

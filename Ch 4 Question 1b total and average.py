#Program name Ch 4 Question 1b total and average.py

total = 0
print("You will be asked to enter 5 numbers.\n")
for n in range(1,6):
    number = int(input("Enter number "+str(n)+ ": "))
    total += number # this is the same as 'total = total + number'

average = total/5
print("Total:",total,"\tAverage:",average)

input("\npress Enter to continue ")                 
                 

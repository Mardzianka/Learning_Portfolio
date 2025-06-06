#Program name: Ch 3 Exercise 5 car parking charges.py
#Program calculates the car parking charge and prints a ticket
#showing current time, time of expiry and charge
#Current time is imported using Python's library module

import time

startTimeInSecs = time.time()
startTimeFormatted = time.ctime(startTimeInSecs)

hours = int(input("Input hours parking required (2, 4 or 12): "))
numSecs = hours *60*60
if hours == 2:
    charge = 3.50
elif hours == 4:
    charge = 5.00
else:
    charge = 10.00
endTimeInSecs = startTimeInSecs + numSecs
print("\nTime now: ", startTimeFormatted)
endTimeFormatted = time.ctime(endTimeInSecs)
print ("Expires:  ", endTimeFormatted)
print("Charge = {:.2f}".format(charge))


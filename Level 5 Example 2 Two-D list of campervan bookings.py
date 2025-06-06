#Program name: Level 5 Example 2 two-D list of campervan bookings

booking = [ [57,68,100,124], [43,52,92,101], [72,78,84,90] ]
totalMay = 0

print(booking)

for row in range(3):
	totalMay = totalMay + booking[row][0]	
print ("Total bookings in May: ",totalMay) 

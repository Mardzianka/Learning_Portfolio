#Program name: Level 3 Example 4 Mobile battery
charge = int(input("Input battery charge %: "))
if charge <= 20:
	print ("Low battery. Charge required.")
elif charge == 100:
	print ("Fully charged.")
else:
	print ("Battery charge OK.")

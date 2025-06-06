#Program name: Level 3 Example 5 water park entry fee
#Program calculates entrance fee
#No validation of user entry is carried out

weekendRate = input("Weekend Rate? (Enter Y or N): ")
visitor = input("Enter J for Junior, S for Senior): ")
if weekendRate == "Y":
    if visitor == "J":
        entryFee = 2.00
    else:
        entryFee = 5.00
else: 
    if visitor == "J":
        entryFee = 1.00
    else:
        entryFee = 2.00
          
print("Entry Fee: ", entryFee) 
        

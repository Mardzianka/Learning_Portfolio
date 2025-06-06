#Program name: Ch6 Example 4.py
#program uses a regular expression to check for valid user ID
#Valid ID has two uppercase letters followed by three digits

import re   #imports regular expression module
userID = input ("Enter your user ID: ")
validID = re.match("[A-Z]{2}[0-9]{3}", userID)
if validID:
    print ("Valid ID entered")
else:
    print ("Invalid ID")

input("\nPress Enter to exit ")
    

#Program name: Ch6 Example 6 regular expression3.py
#program to check for at least one digit in a password
import re
password = input("Enter password: ")
validPassword = re.match("[a-zA-Z]*\d[a-zA-Z0-9]*",password)
if validPassword:
    print("Valid password")
else:
    print("Invalid password")

input("\nPress Enter to exit ")

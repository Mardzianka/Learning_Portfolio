#Program name: Ch6 Example 3 compare password.py
#Program to check a user's password

storedPassword = "Secret246"
passwordValid = False
attempt = 1

while attempt <= 3:
    password = input ("Input password: ")
    if password == storedPassword:
        passwordValid = True
        break
    else:
        print ("This password is not correct...")
        attempt += 1
        
if passwordValid:
    print("Password accepted")
else:
    print ("Log on unsuccessful")

input ("\n Press Enter to continue ")
